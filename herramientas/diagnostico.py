#!/usr/bin/env python3
"""Paso 2: diagnóstico de solo lectura de una bóveda de Obsidian. Python estándar 3.8+.

Uso:
    python -B diagnostico.py <boveda> <salida.json> [--referencia ATOMO.md]
        [--mapa NOTA] [--entrada NOTA] [--registro NOTA] [--excluir PATRÓN ...]

- No escribe en la bóveda: solo <salida.json>, que debe quedar fuera de ella.
- Reconoce los nombres de Obsidian Genesis (INDICE.md, LEER_PRIMERO.md,
  00_CORE/logs/registro-cambios.md) y otros comunes; con --mapa, --entrada y --registro
  se indican los de la bóveda si son distintos.
- Los datos privados se informan como archivo, tipo y línea; nunca el valor.
- El resultado es materia prima: la IA revisa los casos dudosos antes de escribir el informe.
"""
import argparse
import collections
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
OCULTAS_IGNORADAS = {".git"}
NO_PROPIAS = {"_archivo", "node_modules", "__pycache__"}
MARCA_INDICE = re.compile(r"^> \[!info\]-? Índice de esta nota", re.M)
ATOMO = "00_CORE/atoms/00_vault-rules.md"
CANDIDATOS = {
    "mapa": ["INDICE.md", "00 - Índice General.md", "Índice General.md", "Index.md"],
    "entrada": ["LEER_PRIMERO.md", "00 - Leer primero.md", "Leer primero.md", "README.md"],
    "registro": ["00_CORE/logs/registro-cambios.md", "Historial de Cambios/registro.md"],
    "procedencia": ["Historial de Cambios/procedencia.md", "00_CORE/logs/procedencia.md"],
}
INSTRUCCIONES = {"AGENTS.MD", "CLAUDE.MD", "GEMINI.MD", "AI-INSTRUCTIONS.MD", "README.MD"}
PRIVADOS = {
    "correo": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
    "telefono": re.compile(r"(?<![\w+])\+\d{1,3}[ -]?\(?\d{1,4}\)?[ -]?\d{3,4}[ -]?\d{3,4}(?!\d)"),
    "tarjeta": re.compile(r"(?<!\d)\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}(?!\d)"),
    "iban": re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,30}\b"),
    "clave": re.compile(r"(?i)\b(contraseña|password|passwd|api[_ -]?key|secret|token)\b\s*[:=]"),
}
ENLACE = re.compile(r"!?\[\[([^\]\n]+?)\]\]")
FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")
FECHA = re.compile(r"(\d{4})-(\d{2})-(\d{2})|(\d{2})/(\d{2})/(\d{4})")
BLOQUE_GENERADO = re.compile(r"<!--\s*([\w-]+):inicio\s*-->")
NOMBRE_INVALIDO = re.compile(r'[:*?"<>|]')
# Plantillas: sus enlaces son marcadores y sus índices no son nodos.
PLANTILLA = re.compile(r"(^|/)(PROJECT_TEMPLATE|[Pp]lantillas?|[Tt]emplates?)(/|$)|(^|/)TEMPLATE_")


def flujos_alternativos(raiz):
    """Flujos alternativos de NTFS (Windows): contenido que Obsidian y git no ven."""
    if os.name != "nt":
        return []
    ps = ("[Console]::OutputEncoding=[Text.Encoding]::UTF8; "
          f"Get-ChildItem -LiteralPath '{raiz}' -Recurse -File -Force | "
          "Where-Object { $_.FullName -notlike '*\\.git\\*' } | "
          "ForEach-Object { Get-Item -LiteralPath $_.FullName -Stream * } | "
          "Where-Object { $_.Stream -ne ':$DATA' -and $_.Stream -ne 'Zone.Identifier' } | "
          "ForEach-Object { $_.FileName + '|' + $_.Stream + '|' + $_.Length }")
    r = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True, encoding="utf-8")
    salida = []
    for linea in (r.stdout or "").splitlines():
        if linea.count("|") >= 2:
            ruta, flujo, tam = linea.rsplit("|", 2)
            salida.append({"archivo": Path(ruta).resolve().relative_to(raiz).as_posix(), "flujo": flujo, "bytes": int(tam)})
    return salida


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("boveda")
    p.add_argument("salida")
    p.add_argument("--referencia", help="átomo de reglas del kit, para compararlo con el de la bóveda")
    for clave in ("mapa", "entrada", "registro"):
        p.add_argument(f"--{clave}", help=f"ruta relativa de la nota de {clave}, si no es una de las habituales")
    p.add_argument("--excluir", action="append", default=[], help="patrón de ruta relativa a tratar como ajena")
    a = p.parse_args()
    raiz, salida = Path(a.boveda).resolve(), Path(a.salida).resolve()
    if raiz in salida.parents:
        sys.exit("La salida debe quedar fuera de la bóveda.")

    todos = [x for x in raiz.rglob("*") if x.is_file() and x.relative_to(raiz).parts[0] not in OCULTAS_IGNORADAS]
    rels = {x.relative_to(raiz).as_posix(): x for x in todos}

    def es_propia(r):
        partes = r.split("/")
        return (not any(x.startswith(".") or x in NO_PROPIAS for x in partes[:-1])
                and not any(fnmatch.fnmatch(r, pat) for pat in a.excluir))

    textos = {}
    for r, x in rels.items():
        if r.endswith(".md"):
            try:
                textos[r] = x.read_text(encoding="utf-8-sig")
            except UnicodeDecodeError:
                textos[r] = None
    propias = sorted(r for r in textos if es_propia(r))
    piezas = {c: (getattr(a, c, None) or next((n for n in v if n in rels), None)) for c, v in CANDIDATOS.items()}

    def texto(r):
        return (textos.get(r) or "") if r else ""

    d = {"piezas": piezas}
    # 2. Inventario
    d["inventario"] = {
        "archivos_sin_git": len(todos),
        "por_extension": dict(collections.Counter((x.suffix.lower() or "(sin)") for x in todos).most_common()),
        "raiz_archivos": sorted(r for r in rels if "/" not in r),
        "carpetas_ocultas": sorted(x.name for x in raiz.iterdir() if x.is_dir() and x.name.startswith(".")),
        "notas_md": len(textos),
        "notas_propias": len(propias),
        "no_utf8": sorted(r for r, t in textos.items() if t is None),
        "nombres_invalidos_windows": sorted(r for r in rels if NOMBRE_INVALIDO.search(r)),
        "flujos_alternativos": flujos_alternativos(raiz),
    }
    # 3. Reglas, entrada y mapa
    atomo = raiz / ATOMO
    d["reglas"] = {
        "atomo_existe": atomo.exists(),
        "instrucciones_en_raiz": sorted(r for r in rels if "/" not in r and r.upper() in INSTRUCCIONES),
    }
    if atomo.exists() and a.referencia and Path(a.referencia).exists():
        d["reglas"]["atomo_igual_a_referencia"] = (
            hashlib.sha256(atomo.read_bytes()).digest() == hashlib.sha256(Path(a.referencia).read_bytes()).digest())

    # Resolución de enlaces al estilo de Obsidian (ruta, ruta parcial o nombre único)
    rels_lower = {r.lower() for r in rels}
    nombres = set()
    for r in rels:
        nombres.add(Path(r).name.lower())
        if r.endswith(".md"):
            nombres.add(Path(r).stem.lower())

    def destino_de(enlace, origen):
        t = enlace.split("|")[0].split("#")[0].split("^")[0].rstrip("\\").strip()
        if not t:
            return origen
        carpeta = Path(origen).parent.as_posix()
        for c in (t, t + ".md"):
            c = c.lower()
            if c in rels_lower:
                return c
            if f"{carpeta}/{c}".lower() in rels_lower:
                return f"{carpeta}/{c}".lower()
            if "/" in c:
                hit = next((x for x in rels_lower if x.endswith("/" + c)), None)
                if hit:
                    return hit
        if "/" not in t and (t.lower() in nombres or t.lower() + ".md" in nombres):
            return t.lower()
        return None

    # 4. Nodos: notas índice, fichas y su presencia en el mapa
    indices = [r for r in propias if Path(r).name.startswith("00 - Índice") and r != piezas["mapa"] and not PLANTILLA.search(r)]
    fichas = sorted(r for r in rels if r.startswith("00_CORE/cells/") and not Path(r).name.startswith("TEMPLATE"))
    enlazados = set()
    for m in ENLACE.finditer(texto(piezas["mapa"])):
        dest = destino_de(m.group(1), piezas["mapa"])
        if dest:
            enlazados.add(dest)
    menciones = texto(piezas["mapa"]) + "".join(texto(r) for r in indices)
    d["nodos"] = {
        "indices": len(indices),
        "fichas": len(fichas),
        "indices_no_enlazados_desde_el_mapa": sorted(
            r for r in indices if r.lower() not in enlazados and Path(r).stem.lower() not in enlazados),
        "fichas_no_mencionadas": sorted(r for r in fichas if Path(r).name not in menciones and Path(r).stem not in menciones),
        "carpetas_raiz_sin_indice": sorted(
            c.name for c in raiz.iterdir() if c.is_dir() and not c.name.startswith(".") and c.name not in NO_PROPIAS
            and c.name != "00_CORE" and not any(r.startswith(c.name + "/") for r in indices)),
    }

    # 5. Índices de línea (con indice_lineas.py del kit)
    args = [sys.executable, "-B", str(AQUI / "indice_lineas.py"), "check", "--boveda", str(raiz)]
    for pat in a.excluir:
        args += ["--excluir", pat]
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
    estado = collections.defaultdict(list)
    for linea in r.stdout.splitlines():
        if ": " in linea and not linea.startswith("resumen"):
            st, ruta = linea.split(": ", 1)
            estado[st].append(ruta.replace("\\", "/"))
    resumen = re.search(r"'OK': (\d+)", r.stdout)
    d["indices_linea"] = {"OK": int(resumen.group(1)) if resumen else 0, **estado}

    # 6. Registro
    reg = texto(piezas["registro"])
    info = {"nota": piezas["registro"], "procedencia": piezas["procedencia"]}
    if reg:
        filas, cuerpos = [], collections.defaultdict(list)
        for i, linea in enumerate(reg.splitlines(), 1):
            m = FECHA.search(linea[:40]) if linea.startswith("|") else None
            if m:
                f = m.groups()
                filas.append((i, (f[0], f[1], f[2]) if f[0] else (f[5], f[4], f[3])))
                cuerpos[re.sub(r"[`\\\s]", "", linea.split("|", 3)[-1])[:200]].append(i)
        info.update({
            "bytes": len(reg.encode("utf-8")),
            "filas_con_fecha": len(filas),
            "filas_fuera_de_orden": [i for (i, f), (_, g) in zip(filas[1:], filas[:-1]) if f < g],
            "filas_repetidas": [v for v in cuerpos.values() if len(v) > 1],
        })
    info["rotacion_declarada"] = [
        {"nota": n, "linea": i, "dias": int(m.group(1))}
        for n in {ATOMO, piezas["mapa"], piezas["registro"]} if n
        for i, linea in enumerate(texto(n).splitlines(), 1)
        for m in re.finditer(r"(\d+) días", linea) if re.search(r"bloque|período|periodo|rota", linea, re.I)]
    d["registro"] = info

    # 7. Enlaces rotos y bloques generados
    rotos, generados = [], []
    for r in propias:
        t = textos[r]
        if not t or PLANTILLA.search(r):
            continue
        limpio = INLINE.sub("", FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), t))
        for i, linea in enumerate(limpio.splitlines(), 1):
            for m in ENLACE.finditer(linea):
                e = m.group(1)
                if not any(x in e for x in ("<", "{{", "...", "…")) and destino_de(e, r) is None:
                    rotos.append({"nota": r, "linea": i, "destino": e.split("|")[0].rstrip("\\")})
        lineas = t.splitlines()
        for i, linea in enumerate(lineas, 1):
            m = BLOQUE_GENERADO.search(linea)
            if m:
                fin = next((j for j in range(i, len(lineas) + 1) if f"{m.group(1)}:fin" in lineas[j - 1]), None)
                generados.append({"nota": r, "bloque": m.group(1), "lineas": [i, fin]})
    d["enlaces"] = {"rotos": rotos, "bloques_generados": generados}

    # 8. Duplicados
    por_hash, por_nombre = collections.defaultdict(list), collections.defaultdict(list)
    for r, x in rels.items():
        if es_propia(r) and x.stat().st_size > 0:
            por_hash[hashlib.sha256(x.read_bytes()).hexdigest()].append(r)
    for r in propias:
        por_nombre[Path(r).name].append(r)
    d["duplicados"] = {
        "mismo_contenido": sorted(sorted(v) for v in por_hash.values() if len(v) > 1),
        "mismo_nombre_md": {k: sorted(v) for k, v in sorted(por_nombre.items()) if len(v) > 1},
    }

    # 9. Peso de contexto
    arranque = [x for x in (ATOMO, piezas["entrada"], piezas["mapa"]) if x and x in rels]
    total = sum(len(texto(x) or rels[x].read_text(encoding="utf-8-sig", errors="replace")) for x in arranque)
    tablas = [l for l in texto(piezas["mapa"]).splitlines() if l.startswith("|")]
    d["contexto"] = {
        "arranque": {x: len(texto(x)) for x in arranque},
        "arranque_total": total,
        "arranque_tokens_aprox": total // 4,
        "espacios_de_alineacion_en_tablas_del_mapa": sum(len(l) - len(re.sub(r" {2,}", " ", l)) for l in tablas),
        "indices_mas_pesados": sorted(((r, len(texto(r))) for r in indices), key=lambda x: -x[1])[:10],
        "fichas_mas_pesadas": sorted(((r, rels[r].stat().st_size) for r in fichas), key=lambda x: -x[1])[:10],
        "notas_mas_de_10000": [[r, len(texto(r)), bool(MARCA_INDICE.search(texto(r)))]
                               for r in propias if len(texto(r)) > 10000],
    }

    # 10. Datos privados: archivo, tipo y líneas (indicativo: hay falsos positivos)
    priv = collections.defaultdict(lambda: collections.defaultdict(list))
    for r, x in rels.items():
        if not es_propia(r) or x.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".csv", ".txt"}:
            continue
        t = textos.get(r)
        if t is None:
            try:
                t = x.read_text(encoding="utf-8-sig")
            except (UnicodeDecodeError, OSError):
                continue
        for i, linea in enumerate(t.splitlines(), 1):
            for tipo, rx in PRIVADOS.items():
                if rx.search(linea):
                    priv[r][tipo].append(i)
    d["datos_privados"] = {
        "archivos": len(priv),
        "por_tipo": dict(collections.Counter(t for v in priv.values() for t in v)),
        "ubicaciones": {r: dict(v) for r, v in sorted(priv.items())},
    }

    # 11. Zonas intocables
    d["intocables"] = {
        "carpetas_ocultas": d["inventario"]["carpetas_ocultas"],
        "scripts_en_raiz": sorted(r for r in rels if "/" not in r and r.endswith((".py", ".js", ".sh", ".ps1", ".json"))),
        "archivos_en_archivo": sum(1 for r in rels if "_archivo/" in "/" + r),
        "excluidos_por_patron": sorted(r for r in rels if any(fnmatch.fnmatch(r, pat) for pat in a.excluir))[:50],
        "bloques_generados": len(generados),
    }

    salida.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({
        "piezas": piezas,
        "archivos": len(todos),
        "notas_propias": len(propias),
        "indices_linea": {k: (v if isinstance(v, int) else len(v)) for k, v in d["indices_linea"].items()},
        "indices": len(indices),
        "indices_no_enlazados_desde_el_mapa": len(d["nodos"]["indices_no_enlazados_desde_el_mapa"]),
        "fichas_no_mencionadas": len(d["nodos"]["fichas_no_mencionadas"]),
        "carpetas_raiz_sin_indice": d["nodos"]["carpetas_raiz_sin_indice"],
        "enlaces_rotos": len(rotos),
        "bloques_generados": len(generados),
        "flujos_alternativos": len(d["inventario"]["flujos_alternativos"]),
        "no_utf8": len(d["inventario"]["no_utf8"]),
        "grupos_duplicados": len(d["duplicados"]["mismo_contenido"]),
        "arranque_tokens_aprox": total // 4,
        "privados_archivos": len(priv),
        "registro_fuera_de_orden": len(info.get("filas_fuera_de_orden", [])),
        "registro_filas_repetidas": len(info.get("filas_repetidas", [])),
        "rotacion_dias_declarada": sorted({x["dias"] for x in info["rotacion_declarada"]}),
        "atomo_igual_a_referencia": d["reglas"].get("atomo_igual_a_referencia"),
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    main()
