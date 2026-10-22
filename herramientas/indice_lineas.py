#!/usr/bin/env python3
"""Índice de líneas para notas de Obsidian. Python estándar 3.8+.

Cada nota .md empieza (después de las propiedades) con un bloque:

    > [!info]- Índice de esta nota (líneas)
    > - Líneas 1–5: Propiedades
    > - Líneas 6–12: Este índice
    > - Líneas 14–40: <sección>

Los números son líneas del archivo completo, incluido el propio índice.

Uso:
    python -B indice_lineas.py check --boveda <carpeta> [--excluir PATRÓN ...]
    python -B indice_lineas.py check <nota> ...
    python -B indice_lineas.py apply <nota> ... [--abierto]

- check no escribe: lista cada nota sin índice (FALTA), con rangos viejos
  (DESACTUALIZADO) u omitida (OMITIDA: no es UTF-8), y un resumen.
- apply solo trabaja sobre las notas que se le pasan: así se respeta el plan aprobado.
- Si el índice ya existe con la misma cantidad de secciones, conserva sus descripciones
  y su encabezado (plegable «[!info]-» o abierto «[!info]»); solo actualiza los números.
- Un índice nuevo es plegable, salvo con --abierto.
"""
import argparse
import fnmatch
import os
import re
import sys

ENCABEZADO = "> [!info]- Índice de esta nota (líneas)"
ENCABEZADO_ABIERTO = "> [!info] Índice de esta nota (líneas)"
ES_ENCABEZADO = re.compile(r"^> \[!info\]-? Índice de esta nota")
IGNORAR = {"_archivo", "node_modules", "__pycache__", "venv", ".venv"}
TITULO = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
ENTRADA = re.compile(r"^>\s*-\s*Líneas\s+(\d+)\s*[–-]\s*(\d+):\s*(.*)$")


def leer(ruta):
    with open(ruta, "rb") as f:
        crudo = f.read()
    if crudo[:2] in (b"\xff\xfe", b"\xfe\xff"):
        raise ValueError("UTF-16")
    bom = crudo[:3] == b"\xef\xbb\xbf"
    return crudo.decode("utf-8-sig" if bom else "utf-8"), bom


def partir(texto):
    eol = "\r\n" if "\r\n" in texto else "\n"
    final = texto.endswith("\n")
    lineas = texto.replace("\r\n", "\n").split("\n")
    return (lineas[:-1] if final else lineas), eol, final


def largo_propiedades(lineas):
    if lineas and lineas[0].strip() == "---":
        for i in range(1, len(lineas)):
            if lineas[i].strip() == "---":
                return i + 1
    return 0


def buscar_bloque(lineas, desde):
    """(inicio, fin_exclusivo) del bloque existente, o None. Admite una línea de atribución antes."""
    for i in range(desde, min(len(lineas), desde + 3)):
        if ES_ENCABEZADO.match(lineas[i]):
            j = i + 1
            while j < len(lineas) and lineas[j].startswith(">"):
                j += 1
            return i, j
    return None


def secciones(cuerpo, nivel):
    salida, en_codigo = [], False
    for i, linea in enumerate(cuerpo):
        if linea.strip().startswith("```"):
            en_codigo = not en_codigo
            continue
        m = None if en_codigo else TITULO.match(linea)
        if m and len(m.group(1)) <= nivel:
            salida.append((i, m.group(2).strip()))
    return salida


def armar(pm, previo, resto, encabezado, viejas, nivel, con_previo):
    """Bloque nuevo para una forma de índice: hasta «nivel» de títulos, con o sin entrada previa."""
    secs = secciones(resto, nivel)
    entradas = []
    if secs and secs[0][0] > 0 and any(l.strip() for l in resto[:secs[0][0]]):
        entradas.append(("Introducción", 0, secs[0][0] - 1))
    elif not secs and resto:
        entradas.append(("Contenido", 0, len(resto) - 1))
    for k, (s, t) in enumerate(secs):
        entradas.append((t, s, secs[k + 1][0] - 1 if k + 1 < len(secs) else len(resto) - 1))
    llenas = [i for i, l in enumerate(previo) if l.strip()]
    fijas = [("Propiedades", 1, pm)] if pm else []
    if con_previo and llenas:
        fijas.append(("Atribución", pm + 1, pm + llenas[-1] + 1))
    largo = 1 + len(fijas) + 1 + len(entradas)
    inicio_bloque = pm + len(previo) + 1
    fijas.append(("Este índice", inicio_bloque, inicio_bloque + largo - 1))
    inicio_cuerpo = inicio_bloque + largo + 1
    filas = [(d, a, b) for d, a, b in fijas] + [(t, inicio_cuerpo + s, inicio_cuerpo + e) for t, s, e in entradas]
    if viejas is not None and len(viejas) == len(filas):
        filas = [(v, a, b) for v, (_, a, b) in zip(viejas, filas)]
    bloque = [encabezado] + [f"> - Líneas {a}–{b}: {d}" for d, a, b in filas]
    return bloque, len(filas)


def construir(lineas, abierto=False):
    pm = largo_propiedades(lineas)
    bloque = buscar_bloque(lineas, pm)
    viejas, encabezado = None, (ENCABEZADO_ABIERTO if abierto else ENCABEZADO)
    if bloque:
        encabezado = lineas[bloque[0]]
        viejas = [m.group(3) for m in map(ENTRADA.match, lineas[bloque[0] + 1:bloque[1]]) if m]
        fin = bloque[1] + (1 if bloque[1] < len(lineas) and not lineas[bloque[1]].strip() else 0)
        previo, resto = lineas[pm:bloque[0]], lineas[fin:]
    else:
        previo, resto = [], lineas[pm:]
    while resto and not resto[0].strip():
        resto = resto[1:]
    # Las bóvedas usan formas distintas (títulos hasta ## o ###, con o sin atribución previa):
    # se conserva la forma cuyo número de entradas coincide con el índice existente.
    primero = None
    for nivel, con_previo in ((2, True), (3, True), (2, False), (3, False)):
        nuevo, n = armar(pm, previo, resto, encabezado, viejas, nivel, con_previo)
        if primero is None:
            primero = nuevo
        if viejas is not None and n == len(viejas):
            return lineas[:pm] + previo + nuevo + [""] + resto
    return lineas[:pm] + previo + primero + [""] + resto


def estado(ruta):
    try:
        texto, _ = leer(ruta)
    except (ValueError, UnicodeDecodeError) as error:
        return "OMITIDA", str(error)
    lineas, _, _ = partir(texto)
    if not buscar_bloque(lineas, largo_propiedades(lineas)):
        return "FALTA", ""
    return ("OK", "") if construir(lineas) == lineas else ("DESACTUALIZADO", "")


def aplicar(ruta, abierto):
    texto, bom = leer(ruta)
    lineas, eol, final = partir(texto)
    nuevo = construir(lineas, abierto)
    if nuevo == lineas:
        return False
    salida = eol.join(nuevo) + (eol if final else "")
    with open(ruta, "w", encoding="utf-8-sig" if bom else "utf-8", newline="") as f:
        f.write(salida)
    return True


def notas_de(boveda, excluir):
    for base, carpetas, archivos in os.walk(boveda):
        carpetas[:] = sorted(c for c in carpetas if not c.startswith(".") and c not in IGNORAR)
        for nombre in sorted(archivos):
            ruta = os.path.join(base, nombre)
            rel = os.path.relpath(ruta, boveda).replace(os.sep, "/")
            if nombre.endswith(".md") and not any(fnmatch.fnmatch(rel, p) for p in excluir):
                yield ruta


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("modo", choices=["check", "apply"])
    p.add_argument("notas", nargs="*")
    p.add_argument("--boveda", help="revisar todas las notas de esta carpeta (solo con check)")
    p.add_argument("--excluir", action="append", default=[], help="patrón de ruta relativa a omitir, p. ej. '*/plantillas/*'")
    p.add_argument("--abierto", action="store_true", help="índices nuevos sin plegar")
    a = p.parse_args(argv)
    if bool(a.notas) == bool(a.boveda) or (a.modo == "apply" and a.boveda):
        p.error("check: notas o --boveda (no ambos). apply: solo notas concretas.")
    if a.modo == "apply":
        for ruta in a.notas:
            print(("actualizada: " if aplicar(ruta, a.abierto) else "sin cambios: ") + ruta)
        return 0
    rutas = list(notas_de(a.boveda, a.excluir)) if a.boveda else a.notas
    cuenta = {}
    for ruta in rutas:
        st, msg = estado(ruta)
        cuenta[st] = cuenta.get(st, 0) + 1
        if st != "OK":
            print(f"{st}: {os.path.relpath(ruta, a.boveda) if a.boveda else ruta}{' (' + msg + ')' if msg else ''}")
    print("resumen:", cuenta)
    return 1 if cuenta.get("FALTA") or cuenta.get("DESACTUALIZADO") else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
