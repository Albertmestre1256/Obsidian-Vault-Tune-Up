# Pruebas y límites

## Qué verificar

- Rechazo de sobrescritura y captura estable del origen.
- Copia independiente con origen intacto, incluidos flujos NTFS en Windows.
- Índices exactos, descripciones de hasta diez palabras, cuerpo intacto y aplicación idempotente.
- Movimientos con origen/destino y contenido conservado; esperados.txt no autoriza ausencias.
- Detección de cambios ajenos, pérdida de flujos e índices pendientes.
- Rechazo de sobreescrituras de originales aun cuando sus rutas figuren como esperadas.
- Reparaciones de wikilinks y enlaces Markdown según los movimientos, conservando destino, etiqueta y fragmento. El código literal no se interpreta como navegación.
- Diagnóstico sin valores privados; las notas excluidas no se abren para analizar su texto.
- Recorrido: preferencias → reglas aprobadas → copia → organización → conexiones → compactación conservadora → índices → carpeta/ZIP comprobado.

## Ejecutar como desarrollador

`python -B -m unittest discover -s tests -v`

La suite usa bóvedas ficticias y temporales. Nunca probar sobre un original personal. Guardar evidencias fuera del repo y usar una copia nueva con respaldo y plan acordado.

## Límites

La suite no acredita una entrevista útil, clasificación correcta, matices conservados en una síntesis, ahorro de tokens de un modelo, compatibilidad con todas las IA web ni calidad visual en Obsidian. Los manifiestos prueban integridad de bytes antes de transformar; los movimientos e índices se contrastan después. Una consolidación requiere además comparar contenido contra originales conservados.

El recorrido web requiere recepción, extracción segura, edición, ZIP y extracción/comparación del resultado en un entorno compatible. Un ZIP común no transporta flujos NTFS: se necesitan archivos de preservación e inventario cuando existan. Registrar por separado las pruebas con sesión limpia y con personas; no inventar resultados.

## Comprobaciones de esta iteración

- 21 pruebas automáticas correctas en Windows con Python 3.13.
- Copia y diagnóstico sobre una copia de una bóveda real, con preservación comprobada de sus flujos NTFS; sin reorganizar las notas reales.
- Ejemplo ficticio de entrega: agrupación temática, Sin clasificar, duplicado íntegro conservado bajo demanda, diez notas indexadas, carpeta independiente y ZIP extraído idéntico por SHA-256.
- Pendientes: pruebas de aceptación completas con otros usuarios, recorrido completo en una IA web concreta, sesión de contexto limpio y revisión visual.

## Ensayo temático sobre una copia real

Con entrevista y aprobación real de agrupaciones y reglas por el dueño de la bóveda antes de actuar: nueve nodos reorganizados, 101 archivos con movimiento trazado, 344 destinos de enlaces reparados y 1.102 entradas originales conservadas, incluidos dos flujos NTFS. El original y el respaldo permanecieron idénticos a la captura.

Resultado parcial: tras una excepción explícita aprobada por el dueño, se repararon 62 destinos adicionales en 23 notas protegidas, con versiones previas, etiquetas y cuerpos conservados; el total es 406 destinos corregidos. Quedan cinco referencias preexistentes en el diagnóstico del alcance y una referencia archivada detectada por la comparación de movimientos, fuera de esos 62 cambios. Hay dos excepciones de índice y dos diferencias con el comprobador heredado. No se acredita una sesión de contexto limpio ni revisión visual.

En un recorrido documental definido, incluyendo reglas complementarias, molécula, mapa por rangos, tema, nodo y ficha, se midieron 44.154 → 36.649 caracteres (17 % menos). Es una medición de ese recorrido; no tokens reales de API ni una garantía general. La lectura completa de los tres archivos raíz aumentó. No se publican la bóveda ni sus evidencias privadas.

## Revisión posterior de índices y referencias

En dos protocolos, cercas de código anidadas produjeron segmentaciones distintas entre el auxiliar y el comprobador heredado. Se corrigió una descripción heredada que apuntaba a otro contenido, conservando el cuerpo y sus rangos. Las dos diferencias de compatibilidad siguen declaradas; no se modificaron cercas ni herramientas de la bóveda. La consistencia del recálculo no prueba el sentido de una descripción, y la orden del paso 9 ahora exige contrastarlo expresamente.

La excepción para los 62 destinos incluyó comprobación de archivos de destino, hashes contra cambios concurrentes, versiones previas por nota y comparación exacta de cambios de enlaces e índices. Las cinco referencias preexistentes y la referencia archivada pendiente quedan fuera de la excepción.

En el cierre aparecieron dos diferencias de estado de interfaz en la copia (escala del gráfico y paneles), preservadas sin restaurar. El comprobador estricto conserva esas diferencias declaradas: 938 entradas idénticas y 162 transformaciones demostradas, cero faltantes; las otras dos entradas siguen recuperables en el respaldo íntegro. La comparación actual del original muestra diferencias solo en esos dos archivos de interfaz; no hubo escritura del agente en el original y no se atribuye la autoría de esos cambios. No se certifica igualdad total de configuración.

## Medición reproducible de eficiencia

El [protocolo de evaluación](evaluacion/PROTOCOLO.md) separa conservación, calidad y coste; compara antes/después con tareas pareadas y sesiones nuevas. Distingue el estudio del kit completo de los ensayos de referencias e índices. Incluye coste de organización y mantenimiento, intentos fallidos, caché, datos faltantes y límites estadísticos. Las plantillas de [preregistro](evaluacion/preregistro.json) e [intento](evaluacion/intento.json) se completan antes de ejecutar.

Es una metodología preparada, no un ensayo de modelos ya realizado. La evaluación principal usa archivos y trazas; no requiere control visual de la computadora. La revisión visual opcional evalúa presentación y no demuestra eficiencia.

## Revisión del lector de evaluación — 28/10/2026

El lector MCP incorporado el 27/10 permite lectura de archivos dentro de la copia del intento sin habilitar comandos de shell. La revisión posterior corrigió el rechazo de rangos pequeños en notas grandes y la aceptación de rangos inválidos que producían numeración falsa. Búsqueda y listado pueden continuar con `offset`; los resultados tienen un presupuesto explícito. Los errores de codificación o recorrido no se presentan como datos ausentes, y mensajes JSON inválidos no terminan el servidor.

Resultado en Windows: 36 pruebas ejecutadas, 35 correctas y una omitida por falta de permiso para crear enlaces simbólicos. La prueba con una junction NTFS sí verificó que no permite leer, listar o buscar contenido externo. La raíz debe permanecer estable; el servidor comprueba rutas, pero no constituye un sandbox de proceso contra cambios concurrentes del sistema de archivos.

Esto verifica la herramienta sin llamadas a modelos. Sigue pendiente comprobar su integración en una sesión medida de Codex y resolver el servicio configurado para Claude. No demuestra ahorro de tokens ni autoriza nuevos intentos: las cuatro sesiones de calibración previas continúan agotadas.

## Segunda calibración — 28/10/2026

Tras el pedido de continuar se inició otra calibración limitada a cuatro sesiones, todas sobre copias nuevas del corpus ficticio. Claude Code, usando la cuenta directa del usuario, reportó `claude-sonnet-5-5` tanto al inicio como en el resultado; se solicitó esfuerzo alto. En A y B respondió correctamente la única consulta de calibración y citó rangos comprobados contra el archivo efectivamente leído. Hubo uso registrado y ninguna modificación de las copias.

Codex llegó al lector MCP, pero la llamada exigió aprobación mientras la sesión usaba la política never; no leyó los documentos. Ambos intentos se conservan como fallos de acceso. La regla del ejecutor confundió una llamada intentada con una lectura completada y por eso no canceló el segundo intento de Codex; se documentó el desvío y se preparó la corrección sin consumir sesiones adicionales. No se excedió el total de cuatro.

El lector 1.2 declara las tres herramientas como solo lectura. La configuración preparada para la siguiente comprobación limita los nombres permitidos y usa el modo MCP writes, que solicita aprobación para herramientas sin marca de lectura. No habilita shell ni escritura, y todavía no se comprobó con un modelo. La suite de 36 pruebas sigue correcta con una omisión por permisos de symlinks.

La consulta de calibración se excluye del piloto. Dos respuestas correctas de una misma consulta no acreditan ahorro ni calidad general del kit; las cantidades de entrada incluyen historial, instrucciones, herramientas y caché, no solo texto de notas. El piloto de 96 sesiones por entorno no se ejecutó. Las trazas y metadatos privados se mantienen fuera del repositorio.
