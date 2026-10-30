> [!info]- Índice de esta nota (líneas)
> - Líneas 1–7: Este índice
> - Líneas 9–12: Propósito y estado
> - Líneas 13–28: Contrato de salida
> - Líneas 29–37: Reglas de puntuación semántica
> - Líneas 38–41: Evidencia, revisión y cegamiento
> - Líneas 42–44: Controles retrospectivos y límites

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

## Evidencia, revisión y cegamiento

Antes de abrir las nuevas salidas, registrar claves esperadas por tarea, variantes aceptables, citas válidas por condición, errores críticos y versión del contrato. Revisar la salida con etiquetas A/B ocultas y sin tokens, duración ni orden de ejecución visibles. Dos revisores aplican la misma ficha; al menos uno debe ser independiente del diseño. Documentar desacuerdos y resolverlos con una persona adjudicadora previamente designada. El autor del protocolo no cuenta como revisión independiente.

## Controles retrospectivos y límites

Los cuatro resultados de octubre sirven como ejemplos de ambigüedad, no como muestra de validación de esta rúbrica: la misma IA diseñó y revisó las respuestas después de verlas. No cambiar los registros automáticos históricos. Antes de congelar P08, confirmar que el contrato cubre la tarea concreta, preparar casos válidos e inválidos y revisar la ficha sin consumo de modelos.
