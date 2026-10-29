# Cambios

## Eficiencia de nodos — 2026-10-29

- Definición de eficiencia centrada en comprender contexto, notas, vigencia y lugar de trabajo con la menor entrada suficiente; tiempo y coherencia se informan por separado.
- Procedimiento para comparar consumo libre y presupuestos de contexto, distinguir pico de entrada de acumulado y conservar la evaluación de calidad antes de mirar recursos.
- Cuatro sesiones exploratorias sobre copias ficticias, sin ahorro observado: +29,00 % de entrada acumulada en B y tiempos mixtos. Trazas privadas fuera del repositorio; no se agregan auxiliares al flujo de la persona usuaria.

## Calibración de lectura — 2026-10-28

- Claude Code con cuenta directa y Sonnet 5.5: consulta de calibración correcta con citas verificadas en las dos condiciones; sin afirmar eficiencia del kit.
- Codex: bloqueo MCP por aprobación pendiente, conservado como fallo de acceso. Detectado y documentado un error en la regla de parada del ejecutor experimental externo.
- Lector MCP 1.2: anotaciones de lectura sin efectos destructivos. Preparada una configuración que permite únicamente las tres herramientas de lectura, sin ampliar permisos de shell o escritura; pendiente de comprobar dentro de Codex.

## Revisión del lector de evaluación — 2026-10-28

- Lectura real por rangos en notas grandes, validación de límites y numeración, y salida acotada.
- Continuación con offset en búsqueda/listado; errores de codificación o acceso explícitos para no inferir ausencias falsas.
- Recuperación del transporte stdio tras mensajes inválidos y prueba de confinamiento con junctions NTFS.
- 36 pruebas ejecutadas: 35 correctas y una omitida por permisos de enlaces simbólicos. Sin nuevas sesiones de modelos.

## Sin publicar — 0.3-borrador (2026-10-27)

- Evaluación: `evaluacion/servidor_lectura_boveda.py`, un servidor MCP de solo lectura confinado a la copia del intento. Sirve cuando el cliente bloquea comandos de lectura; no es parte del flujo de la persona usuaria.
- Protocolo: una sesión medida se acepta solo si el modelo reportado coincide con el solicitado; un destino local que no responde se registra como fallo técnico de infraestructura; el fallo de acceso no cuenta como medición de calidad.
- Pruebas: 27 pruebas automáticas (21 previas y 6 nuevas del servidor de lectura). Una prueba de enlaces simbólicos se omite si la máquina no permite crearlos.

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
