"""Servidor MCP mínimo, solo lectura, confinado a una carpeta de bóveda de prueba.

Herramienta de evaluación, no parte del flujo de la persona usuaria. Sirve a las
sesiones medidas cuando el cliente bloquea la lectura por shell: en vez de
permitir comandos, expone tres herramientas de lectura sobre la copia del ensayo.

Uso (lo configura el ejecutor de la sesión, no una persona):
    python -I servidor_lectura_boveda.py --root "<carpeta de la copia>"

Sin dependencias: JSON-RPC 2.0 por stdio, un mensaje por línea.
Herramientas: listar_directorio, leer_archivo, buscar_texto. No hay escritura.
Cualquier ruta que salga de --root (absoluta, con '..' o por enlace simbólico) se rechaza.
Las notas grandes admiten rangos acotados; búsqueda/listado continúan con offset.
Solo texto UTF-8: los errores de lectura no se presentan como ausencia de datos.
La raíz debe ser una instantánea estable. Esta comprobación de rutas no es un
sandbox del proceso ni protege contra cambios concurrentes del sistema de archivos.
"""
import argparse
import json
import os
import sys
from pathlib import Path

PROTOCOLO = "2024-11-05"
MAX_BYTES = 200_000
MAX_RESULTADOS = 200
EXTENSIONES_BUSQUEDA = (".md", ".txt")

HERRAMIENTAS = [
    {
        "name": "listar_directorio",
        "description": "Lista archivos y carpetas de una ruta relativa dentro de la bóveda.",
        "inputSchema": {
            "type": "object",
            "properties": {"ruta": {"type": "string"}, "offset": {"type": "integer", "minimum": 0}},
            "additionalProperties": False,
        },
    },
    {
        "name": "leer_archivo",
        "description": "Lee UTF-8 con líneas exactas. Para notas grandes, indicar desde y hasta. Respuesta acotada.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "ruta": {"type": "string"},
                "desde": {"type": "integer", "minimum": 1},
                "hasta": {"type": "integer", "minimum": 1},
            },
            "required": ["ruta"],
            "additionalProperties": False,
        },
    },
    {
        "name": "buscar_texto",
        "description": "Busca un texto literal, sin distinguir mayúsculas, en archivos .md y .txt.",
        "inputSchema": {
            "type": "object",
            "properties": {"texto": {"type": "string"}, "offset": {"type": "integer", "minimum": 0}},
            "required": ["texto"],
            "additionalProperties": False,
        },
    },
]

# Metadatos para políticas que permiten lectura y piden aprobación para escritura.
# El confinamiento real sigue en dentro(); estas anotaciones no lo reemplazan.
for herramienta in HERRAMIENTAS:
    herramienta["annotations"] = {
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    }


def dentro(raiz, relativa):
    if not isinstance(relativa, str):
        raise ValueError("ruta debe ser texto")
    if relativa in ("", "."):
        return raiz
    ruta = Path(relativa)
    if ruta.is_absolute():
        raise PermissionError("ruta absoluta no permitida")
    destino = (raiz / ruta).resolve()
    if destino != raiz and raiz not in destino.parents:
        raise PermissionError("ruta fuera de la bóveda")
    return destino


def entero(args, nombre, defecto, minimo):
    valor = args.get(nombre, defecto)
    if type(valor) is not int or valor < minimo:
        raise ValueError(f"{nombre} debe ser un entero mayor o igual a {minimo}")
    return valor


def lineas_texto(archivo):
    """Lectura incremental; una línea gigante tampoco se carga sin límite."""
    with archivo.open(encoding="utf-8-sig") as fuente:
        n = 0
        while True:
            linea = fuente.readline(MAX_BYTES + 1)
            if not linea:
                break
            if len(linea.encode("utf-8")) > MAX_BYTES:
                raise ValueError("una línea supera el límite de lectura; consulta incompleta")
            n += 1
            yield n, linea.rstrip("\r\n")


def pagina(filas, offset):
    salida, tam = [], 0
    for posicion, fila in enumerate(filas):
        if posicion < offset:
            continue
        peso = len((fila + "\n").encode("utf-8"))
        if peso > MAX_BYTES:
            raise ValueError("un resultado supera el límite; consulta incompleta")
        if len(salida) >= MAX_RESULTADOS or tam + peso > MAX_BYTES:
            return "\n".join(salida) + f"\n(resultados truncados; continuar con offset={offset + len(salida)})"
        salida.append(fila)
        tam += peso
    return "\n".join(salida)


def listar_directorio(raiz, args):
    base = dentro(raiz, args.get("ruta", ""))
    if not base.is_dir():
        raise FileNotFoundError("no es una carpeta")
    def filas():
        for hijo in sorted(base.iterdir()):
            rel = hijo.relative_to(raiz).as_posix()
            try:
                seguro = dentro(raiz, rel)
            except PermissionError:
                continue
            yield rel + ("/" if seguro.is_dir() else "")
    return pagina(filas(), entero(args, "offset", 0, 0)) or "(sin entradas en esta página)"


def leer_archivo(raiz, args):
    archivo = dentro(raiz, args["ruta"])
    if not archivo.is_file():
        raise FileNotFoundError("no es un archivo")
    desde = entero(args, "desde", 1, 1)
    hasta = entero(args, "hasta", sys.maxsize, 1)
    if hasta < desde:
        raise ValueError("hasta debe ser mayor o igual a desde")
    if archivo.stat().st_size > MAX_BYTES and "hasta" not in args:
        raise ValueError("archivo demasiado grande; pedí un rango acotado con desde y hasta")
    filas, tam = [], 0
    for n, texto in lineas_texto(archivo):
        if n > hasta:
            break
        if n >= desde:
            fila = f"{n}: {texto}"
            tam += len((fila + "\n").encode("utf-8"))
            if tam > MAX_BYTES:
                raise ValueError("respuesta demasiado grande; pedí un rango menor")
            filas.append(fila)
        if n == hasta:
            break
    return "\n".join(filas)


def buscar_texto(raiz, args):
    texto = args["texto"]
    if not isinstance(texto, str) or not texto:
        raise ValueError("texto vacío")
    texto = texto.lower()
    def fallo_recorrido(error):
        raise OSError("no se pudo recorrer una carpeta; búsqueda incompleta") from error
    def hallazgos():
        for base, carpetas, archivos in os.walk(raiz, followlinks=False, onerror=fallo_recorrido):
            permitidas = []
            for nombre in sorted(carpetas):
                carpeta = Path(base) / nombre
                try:
                    dentro(raiz, carpeta.relative_to(raiz).as_posix())
                except PermissionError:
                    continue
                # Incluye junctions NTFS, incluso en versiones sin Path.is_junction.
                if carpeta.is_symlink() or getattr(carpeta.lstat(), "st_file_attributes", 0) & 0x400:
                    continue
                permitidas.append(nombre)
            carpetas[:] = permitidas
            for nombre in sorted(archivos):
                archivo = Path(base) / nombre
                if archivo.suffix.lower() not in EXTENSIONES_BUSQUEDA:
                    continue
                rel = archivo.relative_to(raiz).as_posix()
                try:
                    seguro = dentro(raiz, rel)
                except PermissionError:
                    continue
                for n, linea in lineas_texto(seguro):
                    if texto in linea.lower():
                        yield f"{rel}:{n}: {linea.strip()}"
    return pagina(hallazgos(), entero(args, "offset", 0, 0)) or "Sin coincidencias en esta página."


FUNCIONES = {
    "listar_directorio": listar_directorio,
    "leer_archivo": leer_archivo,
    "buscar_texto": buscar_texto,
}


def responder(msg, raiz):
    if not isinstance(msg, dict) or msg.get("jsonrpc") != "2.0" or not isinstance(msg.get("method"), str):
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "solicitud inválida"}}
    if "id" not in msg:
        return None  # las notificaciones (p. ej. notifications/initialized) no reciben respuesta
    rid = msg["id"]
    metodo = msg.get("method")
    try:
        if metodo == "initialize":
            resultado = {
                "protocolVersion": PROTOCOLO,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "boveda-lectura", "version": "1.2"},
            }
        elif metodo == "tools/list":
            resultado = {"tools": HERRAMIENTAS}
        elif metodo == "tools/call":
            nombre = msg["params"]["name"]
            args = msg["params"].get("arguments", {})
            funcion = FUNCIONES.get(nombre)
            if funcion is None:
                raise ValueError(f"herramienta desconocida: {nombre}")
            try:
                if not isinstance(args, dict):
                    raise ValueError("arguments debe ser un objeto")
                esquema = next(h["inputSchema"] for h in HERRAMIENTAS if h["name"] == nombre)
                if set(args) - set(esquema["properties"]) or any(k not in args for k in esquema.get("required", [])):
                    raise ValueError("argumentos desconocidos o faltantes")
                texto, es_error = funcion(raiz, args), False
            except Exception as error:  # el error vuelve como resultado de la herramienta, no tumba el servidor
                texto, es_error = f"Error: {error}", True
            resultado = {"content": [{"type": "text", "text": texto}], "isError": es_error}
        elif metodo == "ping":
            resultado = {}
        else:
            return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "método no soportado"}}
        return {"jsonrpc": "2.0", "id": rid, "result": resultado}
    except Exception as error:
        return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32603, "message": str(error)}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    raiz = Path(ap.parse_args().root).resolve()
    if not raiz.is_dir():
        sys.exit("la raíz no existe")
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue
        try:
            msg = json.loads(linea)
        except ValueError:
            salida = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "JSON inválido"}}
        else:
            salida = responder(msg, raiz)
        if salida is not None:
            sys.stdout.write(json.dumps(salida, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
