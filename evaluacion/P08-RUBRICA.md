> [!info]- Índice de esta nota (líneas)
> - Líneas 1–8: Este índice
> - Líneas 10–13: P08: rúbrica de calidad
> - Líneas 14–29: Contrato de salida
> - Líneas 30–38: Reglas de puntuación semántica
> - Líneas 39–59: Clave de evaluación para la tarea Brisa
> - Líneas 60–63: Evidencia, revisión y cegamiento
> - Líneas 64–66: Controles retrospectivos y límites

# P08: rúbrica de calidad

30/10/2026. Borrador prospectivo preparado para el piloto P02. No se congeló ni se usó para puntuar las sesiones históricas; falta revisión independiente y aprobación antes de nuevas sesiones.

## Contrato de salida

Fijar este esquema en el prompt de ambas condiciones. Los valores tienen un tipo único; las citas se evalúan aparte.

| Campo | Tipo requerido | Criterio para Brisa |
|---|---|---|
| `entrega.fecha` | Cadena ISO `YYYY-MM-DD` | `2031-06-18` |
| `entrega.ubicacion` | Cadena | Centro comunitario Las Acacias |
| `presupuesto.monto` | Entero | `8400` |
| `presupuesto.unidad` | Cadena | `créditos` |
| `gasto_ejecutado` | Booleano | `false`, solo para el importe autorizado |
| `propuesta_aprobada` | Booleano | `false` |
| `proveedor` | Cadena o `null` | `null` si no consta en fuentes revisadas |

`null` significa «no consta en el alcance consultado»; no significa falso ni demuestra que el proveedor no exista. Si la tarea no solicita ubicación o alcance, esos campos no se puntúan.

## Reglas de puntuación semántica

- Validar primero el esquema: campos requeridos, tipos, fechas ISO y propiedades adicionales prohibidas. Una fecha, importe o booleano en el tipo equivocado falla el contrato aunque su texto parezca equivalente.
- Para auditar respuestas históricas de formato libre, conservar la puntuación automática original y añadir una adjudicación semántica separada. «8400 créditos» puede equivaler a monto `8400` y unidad `créditos`, sin borrar la falla de tipo original.
- `false`, `null`, cadena vacía y «no consta» no son intercambiables. Un resultado ausente requiere declaración de alcance y búsqueda suficiente; una búsqueda con error o cero contradictorio no acredita ausencia.
- Puntuar cada hecho, rol, vigencia, destino y abstención como criterio separado. El éxito estricto requiere todos los criterios obligatorios; publicar también cada resultado individual.
- No premiar citas por cantidad. Una cita debe apuntar a la ruta de esa condición, al rango existente y al texto que respalda el hecho. Rutas y líneas válidas se fijan por manifiesto antes de puntuar.
- No resolver una contradicción por fecha más reciente si la fuente define autoridad o aprobación. Una propuesta pendiente no reemplaza una fuente vigente.

## Clave de evaluación para la tarea Brisa

Aplicar esta clave a la tarea ya fijada en `Brisa-prompt.txt`; no mostrarla al modelo ni copiarla a las bóvedas de sesión. La copia A es N01 y la organizada B es N02. Puntuar cada fila por separado; éxito estricto exige todos los criterios obligatorios, evidencia suficiente y cero errores críticos.

| Criterio obligatorio | Respuesta esperada | Evidencia válida en A (N01) | Evidencia válida en B (N02) |
|---|---|---|---|
| Objetivo del nodo | Instalar paneles en el centro comunitario ficticio Las Acacias y preparar comprobaciones previas a la entrega | `Pendientes/brisa-plan.md`: 3–8 | `Energía/brisa-plan.md`: 7–12 |
| Fecha aprobada y lugar | `2031-06-18`; centro Las Acacias | `Fuentes/brisa-acta.md`: 3–8 | `Energía/brisa-acta.md`: 3–8 |
| Propuesta y vigencia | `2031-06-25` es propuesta pendiente, no fecha aprobada | `Borradores/brisa-propuesta.md`: 3–6; `Fuentes/brisa-acta.md`: 5–8 | `Energía/brisa-propuesta.md`: 7–10; `Energía/brisa-acta.md`: 5–8 |
| Importe autorizado | `8400 créditos`; máximo autorizado, no gasto ejecutado ni precio de proveedor | `Notas/brisa-presupuesto.md`: 3–8 | `Energía/brisa-presupuesto.md`: 9–14 |
| Gasto ejecutado | Booleano `false`, con alcance limitado al importe autorizado | `Notas/brisa-presupuesto.md`: 8 | `Energía/brisa-presupuesto.md`: 14 |
| Propuesta aprobada | Booleano `false` | `Borradores/brisa-propuesta.md`: 4–6 | `Energía/brisa-propuesta.md`: 8–10 |
| Proveedor contratado | `null`; declarar que no consta en las cinco notas centrales consultadas; no afirmar inexistencia universal | Leer y citar las cinco notas centrales; registrar archivos consultados | Leer y citar las cinco notas centrales; registrar archivos consultados |
| Cinco notas y roles | Plan: `operativo`; acta: `fuente_aprobada`; presupuesto: `presupuesto`; propuesta: `propuesta_no_aprobada`; acta 2030: `historico` | Rutas arriba y `Archivo/brisa-2030.md`: 3–6 | Rutas arriba y `Archivo/brisa-2030.md`: 3–6 |
| Destino si cambia el máximo | La nota editable de presupuesto: `Notas/brisa-presupuesto.md` en A; `Energía/brisa-presupuesto.md` en B | `Notas/brisa-presupuesto.md`: 1–8 | `Energía/brisa-presupuesto.md`: 7–14 |
| Autoridad ante fechas | Acta aprobada vigente del 2031 gobierna; el acta 2030 está sustituida; una propuesta requiere aprobación expresa | `Fuentes/brisa-acta.md`: 3–8; `Archivo/brisa-2030.md`: 3–6; `Borradores/brisa-propuesta.md`: 3–6 | `Energía/brisa-acta.md`: 3–8; `Archivo/brisa-2030.md`: 3–6; `Energía/brisa-propuesta.md`: 7–10 |

Las rutas citadas deben existir en la copia de esa condición y cada rango debe respaldar la afirmación atribuida. Para `proveedor=null`, una cita aislada no demuestra ausencia: se evalúa el registro de las cinco notas centrales efectivamente leídas y una formulación acotada a ellas. Si una fila obligatoria no se informa, puntuarla como omitida; no inferirla de otra respuesta correcta.

Para el piloto P02, ambas condiciones usan la copia organizada N02; aceptar únicamente las rutas de la columna B (N02). Las rutas A (N01) conservan el marco de comparación histórica y no son citas válidas para las sesiones nuevas.

## Evidencia, revisión y cegamiento

Antes de abrir las nuevas salidas, registrar claves esperadas por tarea, variantes aceptables, citas válidas por condición, errores críticos y versión del contrato. Asignar identificadores aleatorios a las respuestas y ocultar a quienes puntúan cuál corresponde a lectura agrupada o progresiva, su orden, tokens y duración. Dos revisores aplican la misma ficha; al menos uno debe ser independiente del diseño. Documentar desacuerdos y resolverlos con una persona adjudicadora previamente designada. El autor del protocolo no cuenta como revisión independiente.

## Controles retrospectivos y límites

Los cuatro resultados de octubre sirven como ejemplos de ambigüedad, no como muestra de validación de esta rúbrica: la misma IA diseñó y revisó las respuestas después de verlas. No cambiar los registros automáticos históricos. Antes de congelar P08, confirmar que el contrato cubre la tarea concreta, preparar casos válidos e inválidos y revisar la ficha sin consumo de modelos.
