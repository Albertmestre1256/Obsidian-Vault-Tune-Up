"""Fase 3 del kit de adaptación: copia una bóveda y verifica la copia con un manifiesto SHA-256.

Uso: python -B respaldo.py <boveda> <carpeta-de-respaldo-nueva> <carpeta-de-trabajo>

- No escribe en la bóveda.
- No sobrescribe: si la carpeta de respaldo ya existe, se detiene.
- En Windows incluye en el manifiesto los flujos alternativos de NTFS («archivo:flujo»),
  que aparecen cuando un nombre lleva «:» y que Obsidian y git no ven.
Salida: <trabajo>/manifiesto-original.csv. Código 0 si la copia coincide, 2 si no.
"""
import csv
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path


def flujos_alternativos(raiz):
    """Devuelve [(ruta_relativa, flujo)] de los flujos alternativos (solo Windows)."""
    if os.name != "nt":
        return []
    ps = ("[Console]::OutputEncoding=[Text.Encoding]::UTF8; "
          f"Get-ChildItem -LiteralPath '{raiz}' -Recurse -File -Force | "
          "ForEach-Object { Get-Item -LiteralPath $_.FullName -Stream * } | "
          "Where-Object { $_.Stream -ne ':$DATA' -and $_.Stream -ne 'Zone.Identifier' } | "
          "ForEach-Object { $_.FileName + '|' + $_.Stream }")
    r = subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                       capture_output=True, text=True, encoding="utf-8")
    salida = []
    for linea in (r.stdout or "").splitlines():
        if "|" in linea:
            ruta, flujo = linea.rsplit("|", 1)
            salida.append((Path(ruta).resolve().relative_to(raiz).as_posix(), flujo))
    return salida


def manifiesto(raiz):
    datos = {}
    for p in sorted(raiz.rglob("*")):
        if p.is_file():
            datos[p.relative_to(raiz).as_posix()] = (p.stat().st_size, hashlib.sha256(p.read_bytes()).hexdigest())
    for ruta, flujo in flujos_alternativos(raiz):
        contenido = Path(f"{raiz / ruta}:{flujo}").read_bytes()
        datos[f"{ruta}:{flujo}"] = (len(contenido), hashlib.sha256(contenido).hexdigest())
    return datos


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        return 1
    origen, destino, trabajo = (Path(a).resolve() for a in sys.argv[1:])
    if destino.exists():
        print("La carpeta de respaldo ya existe; no se sobrescribe:", destino)
        return 1
    if origen in destino.parents or origen in trabajo.parents or origen == trabajo:
        print("El respaldo y la carpeta de trabajo deben estar fuera de la bóveda.")
        return 1
    trabajo.mkdir(parents=True, exist_ok=True)
    shutil.copytree(origen, destino)
    m_orig, m_copia = manifiesto(origen), manifiesto(destino)
    with open(trabajo / "manifiesto-original.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ruta", "bytes", "sha256"])
        for ruta, (tam, h) in m_orig.items():
            w.writerow([ruta, tam, h])
    faltan = sorted(set(m_orig) - set(m_copia))
    sobran = sorted(set(m_copia) - set(m_orig))
    distintos = sorted(r for r in set(m_orig) & set(m_copia) if m_orig[r] != m_copia[r])
    ocultos = [r for r in m_orig if ":" in r]
    print(f"original={len(m_orig)} copia={len(m_copia)} faltan={len(faltan)} sobran={len(sobran)} "
          f"distintos={len(distintos)} flujos_alternativos={len(ocultos)}")
    for r in (faltan + sobran + distintos)[:20]:
        print("  diferencia:", r)
    for r in ocultos:
        print("  flujo alternativo (contenido oculto):", r)
    return 0 if not (faltan or sobran or distintos) else 2


if __name__ == "__main__":
    sys.exit(main())
