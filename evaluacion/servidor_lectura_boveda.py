"""Servidor MCP mínimo, solo lectura, confinado a una carpeta de bóveda de prueba.

Herramienta de evaluación, no parte del flujo de la persona usuaria. Sirve a las
sesiones medidas cuando el cliente bloquea la lectura por shell: en vez de
permitir comandos, expone tres herramientas de lectura sobre la copia del ensayo.

Uso (lo configura el ejecutor de la sesión, no una persona):
    python -I servidor_lectura_boveda.py --root "<carpeta de la copia>"

Sin dependencias: JSON-RPC 2.0 por stdio, un mensaje por línea.
Herramientas: listar_directorio, leer_archivo, buscar_texto. No hay escritura.
Cualquier ruta que salga de --root (absoluta, con '..' o por enlace simbólico) se rechaza.
"""
import argparse
import json
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
            "properties": {"ruta": {"type": "string"}},
            "additionalProperties": False,
        },
    },
    {
        "name": "leer_archivo",
        "description": "Lee un archivo de texto con numeración de líneas. Permite un rango.",
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
            "properties": {"texto": {"type": "string"}},
            "required": ["texto"],
            "additionalProperties": False,
        },
    },
]


def dentro(raiz, relativa):
    if relativa in ("", "."):
        return raiz
    ruta = Path(relativa)
    if ruta.is_absolute():
        raise PermissionError("ruta absoluta no permitida")
    destino = (raiz / ruta).resolve()
    if destino != raiz and raiz not in destino.parents:
        raise PermissionError("ruta fuera de la bóveda")
    return destino


def listar_directorio(raiz, args):
    base = dentro(raiz, args.get("ruta", ""))
    if not base.is_dir():
        raise FileNotFoundError("no es una carpeta")
    filas = []
    for hijo in sorted(base.iterdir()):
        rel = hijo.relative_to(raiz).as_posix()
        filas.append(rel + ("/" if hijo.is_dir() else ""))
    return "\n".join(filas[:MAX_RESULTADOS]) or "(vacía)"


def leer_archivo(raiz, args):
    archivo = dentro(raiz, args["ruta"])
    if not archivo.is_file():
        raise FileNotFoundError("no es un archivo")
    if archivo.stat().st_size > MAX_BYTES:
        raise ValueError("archivo demasiado grande; pedí un rango de líneas")
    lineas = archivo.read_text(encoding="utf-8", errors="replace").splitlines()
    desde = args.get("desde", 1)
    hasta = args.get("hasta", len(lineas))
    return "\n".join(f"{n}: {t}" for n, t in enumerate(lineas[desde - 1:hasta], start=desde))


def buscar_texto(raiz, args):
    texto = args["texto"].lower()
    if not texto:
        raise ValueError("texto vacío")
    hallazgos = []
    for archivo in sorted(raiz.rglob("*")):
        if not archivo.is_file() or archivo.suffix.lower() not in EXTENSIONES_BUSQUEDA:
            continue
        try:
            dentro(raiz, archivo.relative_to(raiz).as_posix())
        except PermissionError:
            continue
        rel = archivo.relative_to(raiz).as_posix()
        lineas = archivo.read_text(encoding="utf-8", errors="replace").splitlines()
        for n, linea in enumerate(lineas, start=1):
            if texto in linea.lower():
                hallazgos.append(f"{rel}:{n}: {linea.strip()}")
                if len(hallazgos) >= MAX_RESULTADOS:
                    return "\n".join(hallazgos) + "\n(resultados truncados)"
    return "\n".join(hallazgos) or "Sin coincidencias."


FUNCIONES = {
    "listar_directorio": listar_directorio,
    "leer_archivo": leer_archivo,
    "buscar_texto": buscar_texto,
}


def responder(msg, raiz):
    if "id" not in msg:
        return None  # las notificaciones (p. ej. notifications/initialized) no reciben respuesta
    rid = msg["id"]
    metodo = msg.get("method")
    try:
        if metodo == "initialize":
            resultado = {
                "protocolVersion": PROTOCOLO,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "boveda-lectura", "version": "1.0"},
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
            continue
        salida = responder(msg, raiz)
        if salida is not None:
            sys.stdout.write(json.dumps(salida, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
