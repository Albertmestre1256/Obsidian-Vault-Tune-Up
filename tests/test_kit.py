"""Prueba de punta a punta de las herramientas sobre una bóveda desordenada ficticia.

Uso: python -B -m unittest discover -s tests
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

HERRAMIENTAS = Path(__file__).resolve().parent.parent / "herramientas"
sys.path.insert(0, str(HERRAMIENTAS))
sys.dont_write_bytecode = True
import indice_lineas  # noqa: E402
import respaldo  # noqa: E402


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
        self.assertEqual(self.tmp.resolve().parent, Path(tempfile.gettempdir()).resolve())
        shutil.rmtree(self.tmp, ignore_errors=True)

    def preparar_verificacion(self):
        self.assertEqual(correr("respaldo.py", self.boveda, self.tmp / "respaldo", self.trabajo).returncode, 0)
        r = correr("diagnostico.py", self.boveda, self.trabajo / "diagnostico-datos.json")
        self.assertEqual(r.returncode, 0, r.stderr)
        d = json.loads((self.trabajo / "diagnostico-datos.json").read_text(encoding="utf-8"))
        self.esperados = self.trabajo / "esperados.txt"
        faltantes = d["indices_linea"]["FALTA"]
        self.assertEqual(correr("indice_lineas.py", "apply", *(self.boveda / n for n in faltantes)).returncode, 0)
        self.esperados.write_text("\n".join(faltantes), encoding="utf-8")
        return faltantes

    def test_un_archivo_esperado_no_puede_desaparecer(self):
        self.preparar_verificacion()
        (self.boveda / "ideas sueltas.md").unlink()
        r = correr("verificar.py", self.boveda, self.tmp / "respaldo", self.trabajo, self.esperados)
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("ideas sueltas.md", r.stdout)

    def test_movimiento_a_sin_clasificar_conserva_contenido(self):
        permitidos = self.preparar_verificacion()
        origen, destino = "ideas sueltas.md", "Sin clasificar/ideas sueltas.md"
        (self.boveda / "Sin clasificar").mkdir()
        (self.boveda / origen).rename(self.boveda / destino)
        self.esperados.write_text("\n".join(permitidos + [destino]), encoding="utf-8")
        movimientos = self.trabajo / "movimientos.json"
        movimientos.write_text(json.dumps({origen: destino}), encoding="utf-8")
        args = (self.boveda, self.tmp / "respaldo", self.trabajo, self.esperados, "--movimientos", movimientos)
        r = correr("verificar.py", *args)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        # Un destino existente con texto perdido tampoco acredita un movimiento correcto.
        contenido = (self.boveda / destino).read_text(encoding="utf-8")
        (self.boveda / destino).write_text(contenido.replace("Ver [[Proyecto X/plan]]", "Perdido"), encoding="utf-8")
        r = correr("verificar.py", *args)
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("contenido no conservado: ['ideas sueltas.md']", r.stdout)

    def test_indices_pendientes_impiden_cierre(self):
        self.preparar_verificacion()
        nueva = escribir(self.boveda, "pendiente.md", "# Pendiente\n\nContenido.\n")
        with self.esperados.open("a", encoding="utf-8") as f:
            f.write("\n" + nueva.name)
        r = correr("verificar.py", self.boveda, self.tmp / "respaldo", self.trabajo, self.esperados)
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("FALTA: pendiente.md", r.stdout)

    def test_movimiento_con_propiedades_y_blancos_conserva_texto(self):
        origen, destino = "Proyecto X/plan.md", "Sin clasificar/plan.md"
        (self.boveda / origen).write_text("---\ntipo: plan\n---\n\n# Plan\n\nTexto original.\n", encoding="utf-8")
        permitidos = self.preparar_verificacion()
        (self.boveda / "Sin clasificar").mkdir()
        (self.boveda / origen).rename(self.boveda / destino)
        self.esperados.write_text("\n".join(permitidos + [destino]), encoding="utf-8")
        movimientos = self.trabajo / "movimientos.json"
        movimientos.write_text(json.dumps({origen: destino}), encoding="utf-8")
        r = correr("verificar.py", self.boveda, self.tmp / "respaldo", self.trabajo, self.esperados,
                   "--movimientos", movimientos)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_movimientos_no_admiten_escape(self):
        self.preparar_verificacion()
        movimientos = self.trabajo / "movimientos.json"
        movimientos.write_text(json.dumps({"ideas sueltas.md": "../fuera.md"}), encoding="utf-8")
        r = correr("verificar.py", self.boveda, self.tmp / "respaldo", self.trabajo, self.esperados,
                   "--movimientos", movimientos)
        self.assertEqual(r.returncode, 2)
        self.assertIn("sin escapes", r.stderr)

    def test_respaldo_rechaza_origen_que_cambia_al_copiar(self):
        copia_real = shutil.copytree

        def copiar_y_cambiar(origen, destino, *args, **kw):
            resultado = copia_real(origen, destino, *args, **kw)
            if Path(origen) == self.boveda:
                (Path(origen) / "ideas sueltas.md").write_text("Otra sesión cambió el origen", encoding="utf-8")
            return resultado

        with mock.patch.object(sys, "argv", ["respaldo.py", str(self.boveda), str(self.tmp / "respaldo"), str(self.trabajo)]):
            with mock.patch.object(respaldo.shutil, "copytree", side_effect=copiar_y_cambiar), mock.patch("builtins.print"):
                self.assertEqual(respaldo.main(), 2)

    @unittest.skipUnless(os.name == "nt", "Los flujos NTFS solo existen en Windows")
    def test_flujo_ntfs_no_se_puede_perder_aunque_el_archivo_este_en_el_plan(self):
        flujo = Path(str(self.boveda / "ideas sueltas.md") + ":texto-oculto")
        flujo.write_bytes(b"Contenido original oculto")
        self.preparar_verificacion()
        copia_flujo = Path(str(self.tmp / "respaldo" / "ideas sueltas.md") + ":texto-oculto")
        self.assertEqual(copia_flujo.read_bytes(), b"Contenido original oculto")
        flujo.write_bytes(b"Contenido alterado")
        r = correr("verificar.py", self.boveda, self.tmp / "respaldo", self.trabajo, self.esperados)
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("ideas sueltas.md:texto-oculto", r.stdout)

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

    def test_descripcion_maximo_diez_palabras_y_cuerpo_intacto(self):
        cuerpo = "# Uno dos tres cuatro cinco seis siete ocho nueve diez once doce\n\nTexto original.\n"
        nuevo = self.armar(cuerpo)
        for linea in nuevo:
            entrada = indice_lineas.ENTRADA.match(linea)
            if entrada:
                self.assertLessEqual(len(entrada.group(3).split()), 10)
        bloque = indice_lineas.buscar_bloque(nuevo, 0)
        self.assertEqual("\n".join(nuevo[bloque[1] + 1:]) + "\n", cuerpo)
        self.assertEqual(self.armar("\n".join(nuevo) + "\n"), nuevo)

    def test_titulos_dentro_de_cercas_no_son_secciones(self):
        cuerpo = "# Real\n\n~~~~md\n## Falso\n~~~\n## También falso\n~~~~\n\n````\n## Falso otra vez\n```\n## Aún falso\n````\n\n## Final\n\nTexto\n"
        nuevo = self.armar(cuerpo)
        descripciones = [m.group(3) for m in map(indice_lineas.ENTRADA.match, nuevo) if m]
        self.assertEqual(descripciones, ["Este índice", "Real", "Final"])
        self.assertEqual(self.armar("\n".join(nuevo) + "\n"), nuevo)

    def test_etiqueta_larga_no_deja_enlace_roto_en_indice(self):
        nuevo = self.armar("# [[ruta|Uno dos tres cuatro cinco seis siete ocho nueve diez once]]\n\nTexto\n")
        entradas = [m.group(3) for m in map(indice_lineas.ENTRADA.match, nuevo) if m]
        self.assertEqual(entradas[-1], "Uno dos tres cuatro cinco seis siete ocho nueve diez")


if __name__ == "__main__":
    unittest.main()
