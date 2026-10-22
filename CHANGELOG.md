# Cambios

## v0.2 — 2026-10-21

Primera versión preparada para publicarse. Todavía no se publicó.

- Probada sobre la copia de una bóveda real de unas 300 notas: fases 1 a 8, dos acciones de riesgo bajo ejecutadas y verificadas, y seis que quedaron esperando decisión.
- La prueba encontró 13 problemas del borrador, que se corrigieron:
  - Las reglas de la bóveda mandan sobre las del kit.
  - Contenido oculto en flujos alternativos de NTFS (nombres con `:`): ahora se detecta en el diagnóstico y se incluye en el respaldo.
  - Bloques generados (`<!-- x:inicio -->`): zona intocable.
  - Recalcular el índice del registro después de escribir en él.
  - Excepciones declaradas de los índices de líneas.
  - Formato sin pérdida (alineación de tablas) como optimización.
  - Comparar líneas, no hashes, para los datos privados.
  - Medir el arranque también leyendo por rangos.
  - Una sola sesión escribiendo.
  - Ruido de sesión (`workspace.json`, `__pycache__`, diario del conector) separado en la verificación.
- Herramientas: `diagnostico.py`, `respaldo.py`, `indice_lineas.py` y `verificar.py`, solo con Python estándar.
  - `indice_lineas.py` es compatible con las dos formas de índice probadas (títulos hasta `##` o `###`, con atribución previa) y omite las notas que no son UTF-8 sin cortar la revisión.
- Plantillas de reglas, entrada, mapa, índice de nodo, ficha y registro, con los nombres de Obsidian Genesis.
- Prueba automática de punta a punta sobre una bóveda desordenada ficticia.

## v0.1 — 2026-10-21

Borrador de las órdenes en markdown (fases 0 a 8), sin herramientas ni pruebas.
