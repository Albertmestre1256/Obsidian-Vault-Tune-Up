# P02: ficha de revisión independiente

> [!info]- Índice de esta nota (líneas)
> - Líneas 3–8: Este índice
> - Líneas 10–13: Propósito y alcance
> - Líneas 14–27: Lista de comprobación
> - Líneas 28–31: Formato de devolución
> - Líneas 32–34: Reglas de independencia

## Propósito y alcance

Ficha para revisar antes de congelar el piloto de factibilidad P02. Revisar [el diagnóstico](P02-NAVEGACION.md), [la rúbrica P08](P08-RUBRICA.md), [el prerregistro P09](P09-PREREGISTRO-P02.md) y [los textos de interacción](P02-INTERACCIONES-BRISA.md). No puntuar respuestas históricas ni acceder a consumo, futuras respuestas o claves privadas.

## Lista de comprobación

- [ ] La pregunta y el estimando se limitan a lectura agrupada frente a progresiva en esta tarea/corpus.
- [ ] N02 y el SHA-256 de su manifiesto identifican el mismo corpus para todas las sesiones; las copias se verifican antes y después.
- [ ] Las nueve notas y el resultado Glob son iguales en todas las sesiones; el preludio común queda dentro del consumo total y también se informa separado.
- [ ] Los mensajes de tarea/preludio son idénticos; agrupada y progresiva difieren solo por la secuencia prevista. El mensaje adicional progresivo se cuenta como parte del tratamiento.
- [ ] Grep queda excluido de la comparación principal; la tarea limita el juicio sobre proveedor a las cinco notas centrales.
- [ ] P08 cubre todos los campos requeridos, tipos, abstención, notas/roles, vigencia, destinos y evidencia por condición; las citas aceptables respaldan los hechos.
- [ ] El esquema JSON y el mapeo de roles del guion coinciden exactamente con los tipos y la clave de evaluación P08.
- [ ] `false`, `null` y ausencia textual se distinguen; `proveedor=null` no se generaliza más allá del corpus evaluado.
- [ ] El conteo evita duplicar acumulados y llamadas; caché, entrada/salida, wall time y tiempo API se presentan por separado.
- [ ] Dos pares se etiquetan como factibilidad; no se presentan como evidencia de causalidad o eficacia general.
- [ ] La política de parada conserva fallos y no permite reemplazos silenciosos; faltan antes de ejecutar presupuesto y configuración exacta aprobados.

## Formato de devolución

Indicar versión/hash revisados, dictamen (**aprobable**, **aprobable con cambios** o **requiere rediseño**), criterio por criterio (**cumple**, **no cumple** o **N/D**), ubicación del problema y cambio requerido. No editar los documentos originales durante la revisión. El responsable del protocolo registra la devolución y decide cómo responder antes de congelar.

## Reglas de independencia

La persona revisora no debe haber diseñado P08/P09 ni visto las salidas y el consumo de nuevas sesiones. El autor del protocolo no cuenta como revisor independiente. Si la revisión usa otra IA o servicio, su coste y configuración requieren autorización y registro aparte.
