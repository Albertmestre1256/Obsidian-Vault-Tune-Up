"""Prueba de punta a punta de las herramientas sobre una bóveda desordenada ficticia.

Uso: python -B -m unittest discover -s tests
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERRAMIENTAS = Path(__file__).resolve().parent.parent / "herramientas"
sys.path.insert(0, str(HERRAMIENTAS))
sys.dont_write_bytecode = True
import indice_lineas  # noqa: E402


def correr(script, *args):
    return subprocess.run([sys.executable, "-B", str(HERRAMIENTAS / script), *map(str, args)],
                          capture_output=True, text=True, encoding="utf-8")


def escribir(raiz, rel, texto, **kw):
    ruta = raiz / rel
    ruta.parent.mkdir(parents=True, exist_ok=True)
    if "codificacion" in kw:
        ruta.write_bytes(texto.encode(kw["codificacion"]))
    else:
        ruta.write_text(texto, encoding="utf-8", newline=kw.get("newline", "\n"))
    return ruta


class BovedaDesordenada(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.boveda = self.tmp / "boveda"
        b = self.boveda
        escribir(b, "ideas sueltas.md", "# Ideas\n\nVer [[Proyecto X/plan]] y [[nota que no existe]].\n")
        escribir(b, "copia de ideas.md", "# Ideas\n\nVer [[Proyecto X/plan]] y [[nota que no existe]].\n")
        escribir(b, "Proyecto X/plan.md", "---\ntipo: plan\n---\n# Plan\n\nTexto.\n\n## Paso 1\n\nA.\n\n### Detalle\n\nB.\n")
        escribir(b, "Proyecto X/contacto.md", "# Contacto\n\nEscribir a persona@example.com.\n")
        escribir(b, "Proyecto X/windows.md", "﻿# Windows\r\n\r\nLínea.\r\n", newline="")
        escribir(b, "Proyecto X/viejo.md", "# Viejo\n\nTexto en UTF-16.\n", codificacion="utf-16")
        escribir(b, "Proyecto X/generado.md", "# Ofertas\n\n<!-- ofertas:inicio -->\n| a |\n<!-- ofertas:fin -->\n")
        escribir(b, ".obsidian/app.json", "{}")
        self.trabajo = self.tmp / "trabajo"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_recorrido_completo(self):
        r = correr("respaldo.py", self.boveda, self.tmp / "respaldo", self.trabajo)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((self.trabajo / "manifiesto-original.csv").exists())
        # No sobrescribe un respaldo existente
        self.assertEqual(correr("respaldo.py", self.boveda, self.tmp / "respaldo", self.trabajo).returncode, 1)

        r = correr("diagnostico.py", self.boveda, self.trabajo / "diagnostico-datos.json")
        self.assertEqual(r.returncode, 0, r.stderr)
        d = json.loads((self.trabajo / "diagnostico-datos.json").read_text(encoding="utf-8"))
        self.assertEqual(len(d["indices_linea"]["FALTA"]), 6)
        self.assertEqual(len(d["indices_linea"]["OMITIDA"]), 1)
        self.assertEqual([x["destino"] for x in d["enlaces"]["rotos"]], ["nota que no existe"] * 2)
        self.assertEqual(len(d["enlaces"]["bloques_generados"]), 1)
        self.assertEqual(len(d["duplicados"]["mismo_contenido"]), 1)
        self.assertIn("Proyecto X/contacto.md", d["datos_privados"]["ubicaciones"])
        self.assertNotIn("persona@example.com", json.dumps(d))
        self.assertIn("Proyecto X", d["nodos"]["carpetas_raiz_sin_indice"])
        self.assertIsNone(d["piezas"]["mapa"])
        # El diagnóstico no escribió en la bóveda
        self.assertFalse(any(p.name == "__pycache__" for p in self.boveda.rglob("*")))

        notas = [self.boveda / n for n in d["indices_linea"]["FALTA"]]
        self.assertEqual(correr("indice_lineas.py", "apply", *notas).returncode, 0)
        self.assertEqual(correr("indice_lineas.py", "check", *notas).returncode, 0)
        self.assertIn("sin cambios", correr("indice_lineas.py", "apply", notas[0]).stdout)
        crudo = (self.boveda / "Proyecto X/windows.md").read_bytes()
        self.assertTrue(crudo.startswith(b"\xef\xbb\xbf") and b"\r\n" in crudo and b"\n" not in crudo.replace(b"\r\n", b""))

        esperados = self.trabajo / "esperados.txt"
        esperados.write_text("\n".join(d["indices_linea"]["FALTA"]) + "\n", encoding="utf-8")
        r = correr("verificar.py", self.boveda, self.tmp / "respaldo", self.trabajo, esperados)
        self.assertEqual(r.returncode, 0, r.stdout)

        (self.boveda / ".obsidian/app.json").write_text('{"x": 1}', encoding="utf-8")
        r = correr("verificar.py", self.boveda, self.tmp / "respaldo", self.trabajo, esperados)
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn(".obsidian/app.json", r.stdout)


class IndiceDeLineas(unittest.TestCase):
    def armar(self, texto):
        lineas, _, _ = indice_lineas.partir(texto)
        return indice_lineas.construir(lineas)

    def test_rangos_correctos_y_estables(self):
        nuevo = self.armar("---\na: 1\n---\n# T\n\nx\n\n## S\n\ny\n")
        self.assertEqual(nuevo[3], indice_lineas.ENCABEZADO)
        self.assertIn("> - Líneas 1–3: Propiedades", nuevo)
        self.assertEqual(self.armar("\n".join(nuevo) + "\n"), nuevo)
        inicio_s = nuevo.index("## S") + 1
        self.assertTrue(any(l.startswith(f"> - Líneas {inicio_s}–") for l in nuevo))

    def test_conserva_atribucion_previa_y_forma_con_tres_niveles(self):
        texto = ("> **Crédito principal** a alguien.\n\n"
                 "> [!info] Índice de esta nota (líneas)\n"
                 "> - Líneas 1–1: Atribución\n> - Líneas 3–7: Este índice\n"
                 "> - Líneas 9–10: Uno\n> - Líneas 11–12: Dos\n\n"
                 "# Uno\n\n### Dos\n\nfin\n")
        nuevo = self.armar(texto)
        self.assertEqual(nuevo[0], "> **Crédito principal** a alguien.")
        self.assertEqual(nuevo[2], "> [!info] Índice de esta nota (líneas)")
        self.assertIn("> - Líneas 11–13: Dos", nuevo)

    def test_utf16_se_omite_sin_cortar(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = Path(d) / "a.md"
            ruta.write_bytes("# A\n".encode("utf-16"))
            self.assertEqual(indice_lineas.estado(str(ruta))[0], "OMITIDA")


if __name__ == "__main__":
    unittest.main()
