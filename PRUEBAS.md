# Pruebas y límites

## Qué verificar

- Rechazo de sobrescritura y captura estable del origen.
- Copia independiente con origen intacto, incluidos flujos NTFS en Windows.
- Índices exactos, descripciones de hasta diez palabras, cuerpo intacto y aplicación idempotente.
- Movimientos con origen/destino y contenido conservado; esperados.txt no autoriza ausencias.
- Detección de cambios ajenos, pérdida de flujos e índices pendientes.
- Rechazo de sobreescrituras de originales aun cuando sus rutas figuren como esperadas.
- Reparaciones de wikilinks y enlaces Markdown según los movimientos, conservando destino, etiqueta y fragmento. El código literal no se interpreta como navegación.
- Diagnóstico sin valores privados.
- Recorrido: preferencias → reglas aprobadas → copia → organización → conexiones → compactación conservadora → índices → carpeta/ZIP comprobado.

## Ejecutar como desarrollador

`python -B -m unittest discover -s tests -v`

La suite usa bóvedas ficticias y temporales. Nunca probar sobre un original personal. Guardar evidencias fuera del repo y usar una copia nueva con respaldo y plan acordado.

## Límites

La suite no acredita una entrevista útil, clasificación correcta, matices conservados en una síntesis, ahorro de tokens de un modelo, compatibilidad con todas las IA web ni calidad visual en Obsidian. Los manifiestos prueban integridad de bytes antes de transformar; los movimientos e índices se contrastan después. Una consolidación requiere además comparar contenido contra originales conservados.

El recorrido web requiere recepción, extracción segura, edición, ZIP y extracción/comparación del resultado en un entorno compatible. Un ZIP común no transporta flujos NTFS: se necesitan archivos de preservación e inventario cuando existan. Registrar por separado las pruebas con sesión limpia y con personas; no inventar resultados.

## Comprobaciones de esta iteración

- 20 pruebas automáticas correctas en Windows con Python 3.13.
- Copia y diagnóstico sobre una copia de una bóveda real, con preservación comprobada de sus flujos NTFS; sin reorganizar las notas reales.
- Ejemplo ficticio de entrega: agrupación temática, Sin clasificar, duplicado íntegro conservado bajo demanda, diez notas indexadas, carpeta independiente y ZIP extraído idéntico por SHA-256.
- Pendientes: entrevista con una persona real, recorrido completo en una IA web concreta, sesión de contexto limpio y revisión visual.
