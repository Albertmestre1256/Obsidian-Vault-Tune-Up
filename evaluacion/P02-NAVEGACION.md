> [!info]- Índice de esta nota (líneas)
> - Líneas 1–8: Este índice
> - Líneas 10–13: P02: rondas de navegación
> - Líneas 14–33: Resultado que muestran las trazas
> - Líneas 34–37: Pregunta experimental
> - Líneas 38–47: Diseño propuesto
> - Líneas 48–53: Medidas y evaluación
> - Líneas 54–58: Parada y límites

# P02: rondas de navegación

30/10/2026. Estado: análisis de trazas N01/N02 completado; comparación controlada pendiente. No se iniciaron nuevas sesiones de Claude Code; dos revisiones internas de solo lectura contrastaron el desglose.

## Resultado que muestran las trazas

| Sesión | Solicitudes del modelo | Invocaciones de herramientas | Tokens entrada / salida | Agrupación de lecturas |
|---|---:|---:|---:|---|
| N01, Brisa A | 4 | 11 | 28.959 entrada / 2.315 salida | Reglas, índice y cinco notas centrales en una respuesta |
| N02, Brisa B | 6 | 12 | 50.542 entrada / 2.717 salida | Primero reglas, índice y un índice temático; después cinco notas |

La entrada acumulada sube 21.583 tokens (+74,5 %) y las solicitudes suben dos (+50 %) en este par; son diferencias descriptivas, no efectos causales de la estructura temática. La entrada se calcula en cada `result.usage` de Claude sumando `input_tokens`, `cache_creation_input_tokens` y `cache_read_input_tokens`; la salida es `output_tokens`. El conteo incluye historial, instrucciones y herramientas, y la lectura desde caché sigue siendo entrada procesada: no representa tokens exclusivos de los archivos.

La cuenta de solicitudes usa identificadores `request_id` distintos de `eventos.jsonl`; varias invocaciones de herramientas pueden pertenecer a una sola respuesta del modelo. Por eso 4 frente a 6 solicitudes no equivale a 4 frente a 6 herramientas.

La diferencia observada de dos solicitudes se divide en dos hechos distintos:

1. **Lectura progresiva:** N02 leyó el índice temático antes de las cinco notas. Esa etapa separó las lecturas de notas en otra solicitud del modelo e hizo una invocación `Read` adicional.
2. **Reintento P01:** N02-T11 devolvió cero con `glob: !Versiones conservadas/**`; N02-T12 repitió la búsqueda sin ese filtro. La búsqueda adicional ocupó otra solicitud del modelo.

El primer mecanismo es el objeto de P02. El segundo es un fallo de búsqueda identificado en P01 y no debe contarse como coste de navegación. La suma de entrada y el tiempo son diferencias descriptivas de un solo par, no ahorros causales: cambian las copias, los resultados de herramientas y el historial posterior.

El tiempo de pared del expediente es 17,809 s en N01 y 24,875 s en N02 (`estado.json`). El evento `result` registra además `duration_ms` de 16.286 y 24.021 ms, respectivamente, y `duration_api_ms` de 15.997 y 23.645 ms. Son contadores distintos; no intercambiarlos ni inferir que miden solo lectura. Los hashes SHA-256 de `eventos.jsonl` son `a8b0b9119b09c85bb01f8a1afe4e21150dcd1857d4610b0b4e8f3f4502ba207a` (N01) y `393f2e376e37f64d7d1896882ed18e21f28dda4bcd01aeb955887831483e7646` (N02). Fuentes privadas locales: `I:\Obsidian Tune Up\eficiencia-nodos-2026-10-29-01\N01|N02\eventos.jsonl`, `estado.json` y `tiempos-eventos.json`.

## Pregunta experimental

Con el mismo corpus, tarea y lecturas necesarias, ¿agrupar lecturas independientes reduce solicitudes o entrada acumulada frente a leer primero índices y luego notas, sin deteriorar la respuesta?

## Diseño propuesto

Comparar dos ejecuciones aisladas sobre copias nuevas e idénticas de la bóveda ficticia organizada N02, fijada por manifiesto. Mantener iguales versión y modelo, esfuerzo, prompt, herramientas, instrucciones, objetivo, manifiesto de rutas y conjunto de ocho archivos medidos (reglas, índice general, índice temático y cinco notas centrales). `LEER_PRIMERO.md` es preludio común adicional: se lee en ambas condiciones, se cuenta dentro del consumo total y se informa también por separado; por tanto, se prevén nueve archivos leídos por sesión. La lista fija de rutas aísla el orden de lectura; no evalúa descubrimiento de rutas. Mantener esta limitación explícita.

- **Agrupada:** tras el mismo contexto inicial, pedir reglas, índice general, índice temático y cinco notas centrales en una respuesta del modelo.
- **Progresiva:** tras ese mismo contexto, pedir reglas, índice general e índice temático; en la siguiente respuesta, pedir las mismas cinco notas centrales.
- **Preludio común:** leer primero `LEER_PRIMERO.md` en cada sesión. Contarlo dentro del total de cada sesión y reportar su coste por separado; las instrucciones y la tarea se mantienen idénticas.
- **P01 controlado:** no usar Grep en la comparación central. Si una búsqueda resulta imprescindible, aplicar en ambas condiciones el mismo `path` exacto y filtro positivo previamente verificado; nunca usar el glob con espacios que produjo el cero falso.
- **Conservación:** iniciar cada ejecución desde la misma fuente inmutable; verificar manifiesto antes y después. No editar notas ni reutilizar historiales entre condiciones.

## Medidas y evaluación

Contar por separado solicitudes del modelo (`request_id`), invocaciones de herramientas, archivos y caracteres leídos, entrada, creación y lectura de caché, salida, tiempo total y duración de API cuando esté disponible. No inferir tokens documentales de caracteres ni sumar categorías solapadas.

Antes de una comparación de comprensión, fijar P08: respuestas esperadas y rúbrica de hechos, roles, vigencia, rutas y evidencia. Fijar en P09 número de repeticiones, orden balanceado, revisión independiente, modelo, presupuesto y criterios de exclusión. Una sola pareja solo verifica que el protocolo funciona; no sustenta una mejora general. Informar por separado calidad, solicitudes, tokens y tiempo. Menos solicitudes no equivale automáticamente a eficiencia si aumenta la entrada o cae la calidad.

## Parada y límites

El tope exploratorio anterior de cuatro sesiones ya se consumió. No ejecutar nuevas sesiones hasta fijar P08/P09 y autorizar presupuesto nuevo. Registrar cualquier error y conservar la corrida; un cero falso invalida la comparación de navegación, se etiqueta como P01 y no se elimina del historial.

La evidencia actual permite explicar el par histórico, no afirmar que agrupar siempre reduzca tokens o tiempo. Localizadores: `OBSERVACIONES-2026-10-29.md`, N01/N02 y referencias F01/F02 en el expediente local; resumen técnico en `evaluacion/seguimiento/PROBLEMAS.md` y R003.
