# Fase 1: diagnóstico (solo lectura)

**Objetivo:** describir la bóveda tal como está, sin cambiar nada. El resultado es un informe que sirve de base para el plan.

**Regla:** no se escribe en la bóveda. El informe se guarda en la carpeta de trabajo como `diagnostico-AAAA-MM-DD.md`, con la plantilla de abajo.

**Con Python (recomendado):**

```text
python -B herramientas/diagnostico.py <bóveda> <trabajo>/diagnostico-datos.json --referencia plantillas/00_vault-rules.md
```

Hace los pasos 2 a 11 en segundos. Opciones útiles:

- `--mapa`, `--entrada` y `--registro`: si la bóveda usa otros nombres.
- `--excluir '<patrón>'`: para carpetas de terceros.

El script da materia prima: la IA revisa a mano cada caso dudoso antes de pasarlo al informe. En una prueba sobre una bóveda real de unas 300 notas:

- 7 hallazgos automáticos no eran problemas: subnodos que sí estaban en el mapa, excepciones declaradas y una fila sin hora.
- 2 tenían una causa distinta de la aparente: contenido oculto y un bloque generado.

Sin Python, se hacen los mismos pasos con las herramientas de archivos; con más de unas decenas de notas no es viable.

## Pasos

Se hacen en orden. Si un paso no se puede hacer, se anota y se sigue.

### 1. Ubicación y acceso
- Confirmar la ruta de la bóveda y que se puede leer.
- Anotar si hay `.git/` (sirve de respaldo, pero no se toca).
- Anotar si hay sincronización (OneDrive, Dropbox, iCloud, Google Drive, Obsidian Sync).
- Mirar las fechas de modificación más recientes. Si hay cambios de la última hora, otra sesión puede estar escribiendo: avisar (regla 15).

### 2. Inventario
- Estructura de carpetas. De las ocultas, solo los nombres.
- Archivos por extensión y notas más grandes. Archivos sueltos en la raíz.
- Notas que no son UTF-8 (por ejemplo, UTF-16): las herramientas las omiten.
- **Nombres con `:` `*` `?` `"` `<` `>` `|`.** En Windows, un nombre con `:` crea un archivo vacío y guarda el texto en un flujo alternativo de NTFS, que Obsidian y git no ven. Se anota cada uno con su tamaño: es contenido oculto para recuperar.

### 3. Reglas, entrada y mapa
- ¿Hay reglas propias? ¿Dónde? ¿Coinciden con la plantilla del kit?
- ¿Hay una nota de entrada (`LEER_PRIMERO.md` u otra) y un mapa general (`INDICE.md` u otro)?
- Otras instrucciones para IA en la raíz (`AGENTS.md`, `CLAUDE.md`, `README.md`): una línea cada una.
- Contradicciones entre reglas, o entre el mapa y las reglas (por ejemplo, dos plazos distintos para lo mismo).

### 4. Nodos (proyectos o colecciones)
- Carpetas que son proyectos o colecciones, y si tienen nota índice.
- Si cada índice está enlazado desde el mapa, incluidas las tablas de subnodos.
- Si hay fichas de proyecto (`00_CORE/cells/` u otro lugar) y a qué nodo corresponden.
- Estado aparente de cada nodo. Si no está escrito, «no determinado».

### 5. Índices de líneas
Primero hay que leer las **excepciones declaradas** de la bóveda: una nota exceptuada sin índice no es un problema. Después, por cada nota propia: correcto, falta, desactualizado u omitido (no es UTF-8). Se excluyen las plantillas, `_archivo/` y los archivos de terceros.

### 6. Registro
- ¿Existe? Tamaño, última fecha y regla de rotación declarada. Comparar esa regla con la de las reglas y la del mapa.
- Filas repetidas o fuera de orden. No se corrigen: el registro es histórico.

### 7. Enlaces rotos y bloques generados
- Enlaces `[[...]]` que no resuelven, con nota, línea y destino.
- Si el enlace roto está dentro de un **bloque generado**, no se corrige a mano sin saber qué herramienta lo escribe.

### 8. Duplicados
- Mismo contenido (mismo SHA-256) y mismo nombre en carpetas distintas. Esto último confunde los enlaces cortos `[[nombre]]`.
- No se decide cuál se conserva.

### 9. Peso de contexto
- Contexto de arranque: reglas + entrada + mapa. Medirlo de dos formas: leyendo todo, y leyendo el mapa solo por el rango de su tabla de nodos.
- Tokens: estimación de caracteres / 4.
- Espacios de alineación en las tablas del mapa. Obsidian no los muestra y pueden ser una parte grande del archivo.
- Índices y fichas más pesados, y notas de más de 10 000 caracteres: ¿tienen índice de líneas?

### 10. Datos privados
- Patrones de correos, teléfonos, tarjetas, cuentas y claves. Se informa solo **archivo, tipo y línea**, nunca el valor.
- El conteo es indicativo: hay falsos positivos.
- No se cambia nada.

### 11. Zonas intocables
Listar lo que protege la regla 10 de la fase 0 y lo que hay en esta bóveda.

## Plantilla del informe

```markdown
# Diagnóstico de <bóveda> — AAAA-MM-DD

**IA:** <nombre> (<herramienta>, <modelo>)
**Ruta:** <ruta> · **Sincronización:** sí/no · **git:** sí/no · **Otra sesión activa:** sí/no/no determinado

## Resumen
- Archivos: <n> (<n> notas propias) · Nodos: <n> · Índices de líneas correctos: <n> de <n>
- Enlaces rotos: <n> · Contenido oculto: <n> · Duplicados: <n> · Datos privados (ubicaciones): <n>
- Contradicciones de reglas: <n> · Arranque: ≈ <n> tokens (≈ <n> leyendo por rangos)

## 1 a 11
(una sección por paso, con los hallazgos revisados)

## Preguntas para la persona
1. …
```

## Criterio de salida

Cada paso tiene hallazgos revisados o la nota «sin hallazgos». No se pasa a la fase 2 con pasos sin hacer.
