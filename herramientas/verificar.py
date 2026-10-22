#!/usr/bin/env python3
"""Paso 10: compara la copia organizada con su respaldo. Solo lectura. Python estándar 3.8+.

Uso:
    python -B verificar.py <boveda> <respaldo> <trabajo> <esperados.txt>
        [--movimientos movimientos.json] [--excluir PATRÓN ...]

- <trabajo> tiene manifiesto-original.csv (paso 5) y diagnostico-datos.json (paso 2).
- <esperados.txt>: rutas relativas que el plan aprobado cambia, crea o mueve, una por línea.
Comprueba: cambios fuera del plan, herramientas y átomo, flujos alternativos de NTFS,
líneas con datos privados e índices de línea; y mide el contexto de arranque.
Código 0 si pasan estas comprobaciones automáticas, 2 si alguna falla.
No certifica por sí solo la conservación semántica de una consolidación.
"""
import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

import indice_lineas

AQUI = Path(__file__).resolve().parent
PROTEGIDAS = re.compile(r"^(\.[^/]+|_archivo)/|^00_CORE/atoms/|^[^/]+\.(py|js|sh|ps1)$")
# Cambian solos al abrir Obsidian, usar un conector o correr Python: se informan aparte.
RUIDO = re.compile(r"^\.obsidian/workspace[^/]*\.json$|(^|/)__pycache__/|^\.obsidian-mcp/transactions/")
ATOMO = "00_CORE/atoms/00_vault-rules.md"
ENTRADAS = ["LEER_PRIMERO.md", "00 - Leer primero.md", "Leer primero.md"]
MAPAS = ["INDICE.md", "00 - Índice General.md", "Índice General.md"]


def manifiesto_actual(raiz):
    return {p.relative_to(raiz).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in raiz.rglob("*") if p.is_file()}


def rango_tabla(texto):
    """La parte del mapa que indica su índice de línea para los nodos o proyectos; si no, todo."""
    m = re.search(r"Líneas (\d+)[–-](\d+):[^\n]*(Nodos|Proyectos|Mapa de nodos)", texto)
    lineas = texto.splitlines()
    return "\n".join(lineas[int(m.group(1)) - 1:int(m.group(2))]) if m else texto


def ruta_relativa(ruta):
    return (isinstance(ruta, str) and bool(ruta) and "\\" not in ruta and ":" not in ruta
            and not PurePosixPath(ruta).is_absolute() and ".." not in PurePosixPath(ruta).parts)


def contenido_conservado(origen, destino):
    if origen.read_bytes() == destino.read_bytes():
        return True
    if origen.suffix.lower() != ".md" or destino.suffix.lower() != ".md":
        return False
    # Un movimiento puede ir seguido por el recálculo del índice, nunca por pérdida de texto.
    def sin_indice(ruta):
        texto, _ = indice_lineas.leer(ruta)
        lineas, _, _ = indice_lineas.partir(texto)
        bloque = indice_lineas.buscar_bloque(lineas, indice_lineas.largo_propiedades(lineas))
        if bloque:
            inicio, fin = bloque
            if fin < len(lineas) and not lineas[fin].strip():
                fin += 1
            lineas = lineas[:inicio] + lineas[fin:]
        pm = indice_lineas.largo_propiedades(lineas)
        while pm < len(lineas) and not lineas[pm].strip():
            del lineas[pm]
        return "\n".join(lineas).strip("\n")
    try:
        return sin_indice(origen) == sin_indice(destino)
    except (ValueError, UnicodeDecodeError):
        return False


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("boveda")
    p.add_argument("respaldo")
    p.add_argument("trabajo")
    p.add_argument("esperados")
    p.add_argument("--movimientos", help="JSON de rutas relativas: origen → destino")
    p.add_argument("--excluir", action="append", default=[])
    a = p.parse_args()
    boveda, respaldo, trabajo = (Path(x).resolve() for x in (a.boveda, a.respaldo, a.trabajo))
    esperados = {l.strip() for l in Path(a.esperados).read_text(encoding="utf-8").splitlines() if l.strip()}
    with open(trabajo / "manifiesto-original.csv", encoding="utf-8") as f:
        original = {fila["ruta"]: fila["sha256"] for fila in csv.DictReader(f)}
    movimientos = {}
    if a.movimientos:
        movimientos = json.loads(Path(a.movimientos).read_text(encoding="utf-8"))
        if (not isinstance(movimientos, dict)
                or not all(ruta_relativa(o) and ruta_relativa(d) for o, d in movimientos.items())
                or len(set(movimientos.values())) != len(movimientos)):
            p.error("Movimientos: usar rutas relativas sin escapes y destinos únicos.")
        if not all(o in esperados and d in esperados and o in original for o, d in movimientos.items()):
            p.error("Cada movimiento debe estar en el manifiesto y ambas rutas en el plan.")
    falla = False

    base = {k: v for k, v in original.items() if ":" not in k}
    ruido = sum(1 for k in base if RUIDO.search(k))
    base = {k: v for k, v in base.items() if not RUIDO.search(k)}
    actual = {k: v for k, v in manifiesto_actual(boveda).items() if not RUIDO.search(k)}
    faltan = sorted(set(base) - set(actual) - set(movimientos))
    nuevos = sorted(set(actual) - set(base))
    cambiados = sorted(r for r in set(base) & set(actual) if base[r] != actual[r])
    fuera = sorted((set(cambiados) | set(nuevos)) - esperados)
    ok = not faltan and not fuera
    falla |= not ok
    print(f"[{'ok' if ok else 'falla'}] 1 archivos: cambiados {len(cambiados)}, nuevos {len(nuevos)}, "
          f"faltan sin plan {len(faltan)}, fuera del plan {len(fuera)} "
          f"(se ignoran {ruido} archivos de sesión: workspace, __pycache__, diario del conector)")
    for r in (faltan + fuera)[:20]:
        print("    revisar:", r)
    if not ok:
        print("    Si nadie más editó la bóveda, son cambios fuera del plan. Si otra sesión o persona "
              "la editó, pará y compará con ella antes de seguir.")

    incorrectos = []
    for origen, destino in movimientos.items():
        if (destino not in actual or not (respaldo / origen).is_file()
                or not contenido_conservado(respaldo / origen, boveda / destino)):
            incorrectos.append(origen)
    falla |= bool(incorrectos)
    print(f"[{'ok' if not incorrectos else 'falla'}] movimientos: "
          f"{len(movimientos)} declarados; contenido no conservado: {incorrectos or 0}")

    tocadas = [r for r in cambiados + nuevos + faltan if PROTEGIDAS.search(r) and r not in esperados]
    falla |= bool(tocadas)
    print(f"[{'ok' if not tocadas else 'falla'}] 10 átomo y herramientas: {tocadas or 'sin cambios fuera del plan'}")

    perdidos = []
    for clave in (k for k in original if ":" in k):
        ruta, flujo = clave.rsplit(":", 1)
        try:
            destino = movimientos.get(ruta, ruta)
            h = hashlib.sha256(Path(f"{boveda / destino}:{flujo}").read_bytes()).hexdigest()
        except OSError:
            h = None
        if h != original[clave]:
            perdidos.append(clave)
    falla |= bool(perdidos)
    print(f"[{'ok' if not perdidos else 'falla'}] flujos alternativos: "
          f"{sum(':' in k for k in original)} en el manifiesto; cambiados o perdidos: {perdidos or 0}")

    diag = json.loads((trabajo / "diagnostico-datos.json").read_text(encoding="utf-8"))
    ubic = diag["datos_privados"]["ubicaciones"]
    alteradas = []
    for r in cambiados:
        if r in ubic:
            antes = (respaldo / r).read_text(encoding="utf-8-sig").splitlines()
            despues = set((boveda / r).read_text(encoding="utf-8-sig").splitlines())
            if any(antes[i - 1] not in despues for ls in ubic[r].values() for i in set(ls) if i <= len(antes)):
                alteradas.append(r)
    falla |= bool(alteradas)
    print(f"[{'ok' if not alteradas else 'falla'}] 9 datos privados: {sum(r in ubic for r in cambiados)} archivos "
          f"cambiados los contienen; con líneas privadas alteradas: {alteradas or 0}")

    args = [sys.executable, "-B", str(AQUI / "indice_lineas.py"), "check", "--boveda", str(boveda)]
    for pat in a.excluir:
        args += ["--excluir", pat]
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
    pendientes = [l for l in r.stdout.splitlines() if l.startswith(("FALTA", "DESACTUALIZADO"))]
    falla |= r.returncode != 0 or bool(pendientes)
    resumen = r.stdout.strip().splitlines()
    print(f"[{'ok' if r.returncode == 0 and not pendientes else 'falla'}] 9 índices de línea: "
          f"{resumen[-1] if resumen else 'comprobador sin resultado'}")
    for l in pendientes[:10]:
        print("    ", l, "(¿excepción declarada?)")

    for nombre, raiz in (("antes", respaldo), ("después", boveda)):
        def leer(rel):
            x = raiz / rel
            return x.read_text(encoding="utf-8-sig") if rel and x.is_file() else ""
        entrada = next((n for n in ENTRADAS if (raiz / n).is_file()), "")
        mapa = leer(next((n for n in MAPAS if (raiz / n).is_file()), ""))
        fijo = len(leer(ATOMO)) + len(leer(entrada))
        completo, rango = fijo + len(mapa), fijo + len(rango_tabla(mapa))
        print(f"[medida] 12 arranque {nombre}: completo {completo} car (≈{completo // 4} tok); "
              f"mapa por rango {rango} car (≈{rango // 4} tok)")
    return 2 if falla else 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    sys.exit(main())
