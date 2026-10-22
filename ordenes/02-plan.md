# Fase 2: plan con IDs (sin escribir en la bóveda)

**Objetivo:** convertir el diagnóstico en una lista de acciones con ID. La persona aprueba por ID; lo que no se aprueba no se hace.

**Regla:** el plan se guarda en la carpeta de trabajo como `plan-AAAA-MM-DD.md`, fuera de la bóveda.

## Preguntas previas

Si el diagnóstico no las respondió, se le hacen a la persona:

1. ¿Qué carpetas son proyectos o colecciones, y cuáles son recursos o archivo?
2. ¿Qué no se toca nunca?
3. ¿Dónde se guarda el respaldo (fase 3)? Tiene que estar fuera de la bóveda y de la sincronización.
4. ¿Qué hacer con las contradicciones de reglas?
5. ¿Hay otra IA, persona o herramienta que escriba en la bóveda (incluidos los bloques generados)?

## Correspondencias típicas

Son un punto de partida. Cada caso se decide con la persona.

| Situación | Acción propuesta | Riesgo |
|---|---|---|
| Faltan reglas, entrada o mapa | Crearlos desde `plantillas/` | Bajo |
| Carpeta de proyecto sin índice | Crear el índice desde `plantillas/indice-nodo.md` | Bajo |
| Proyecto sin ficha | Crear la ficha solo con lo que dicen las notas; lo dudoso queda «pendiente de confirmar» | Medio |
| Reglas en `README`, `AGENTS.md` u otras guías | Dejarlas donde están y enlazarlas desde la entrada | Bajo |
| Notas sueltas en la raíz | Mover a un nodo existente o proponer uno (pregunta) | Medio |
| Notas sin índice de líneas o desactualizadas | Fase 6 | Bajo |
| Espacios de alineación en tablas | Compactar sin cambiar el texto (fase 7) | Bajo |
| Descripción del mapa que contradice las reglas | Corregir la descripción (mandan las reglas). Cambia texto: necesita aprobación específica | Bajo |
| Enlace roto con destino inequívoco | Corregir el enlace | Bajo |
| Enlace roto dentro de un bloque generado | Preguntar qué herramienta lo genera; quizá se renombra el archivo y no el enlace | Medio |
| Nombre con `:` (contenido en un flujo alternativo) | Recuperar el texto en una nota con nombre válido y mandar el archivo vacío a `_archivo/` | Medio |
| Duplicados exactos | Conservar uno; el otro a `_archivo/` (aprobación por caso) | Medio |
| Notas con el mismo nombre y distinto contenido | Listar; la persona decide | — |
| Material obsoleto | Mover a `_archivo/` (nunca borrar) | Medio |
| Ficha o índice muy pesado | Pasar el historial a una nota de avance (fase 7) | Alto |
| Registro con filas repetidas o fuera de orden | Solo informar: es histórico | — |
| Datos privados | Solo listar; decide la persona | Alto |
| Herramientas propias y bloques generados | No tocar | — |

## Formato de cada acción

```markdown
### P-001 — <título corto>
- **Tipo:** mover / crear / indexar / enlazar / optimizar / editar contenido
- **Origen:** <ruta relativa> · **Destino:** <ruta relativa>
- **Motivo:** <sección del diagnóstico>
- **Riesgo:** bajo / medio / alto
- **Reversión:** <cómo se deshace>
- **Depende de:** P-00X o «ninguna»
- **Estado:** pendiente
```

## Orden del plan

1. Carpetas faltantes (sin mover nada).
2. Reglas, entrada y mapa.
3. Registro.
4. Movimientos a nodos o a `_archivo/`.
5. Índices y fichas de cada nodo.
6. Índices de líneas.
7. Optimización (opcional; cada acción se aprueba aparte).
8. Verificación (fase 8, sin cambios).

## Aprobación

El plan termina con este bloque, que la persona completa en el chat:

```text
Aprobado: P-001 a P-0xx
Excluido: P-0xx (motivo)
Pendiente de decisión: P-0xx
```

- Sin ese bloque, no se ejecuta nada.
- Un «sí, adelante» general no alcanza: hay que nombrar los IDs o un rango.
- Las acciones de riesgo alto, las que cambian texto y todo lo de la fase 7 se aprueban una por una.
- Si al ejecutar aparece un riesgo que el plan no vio, la acción se reclasifica y vuelve a «pendiente de decisión».

## Criterio de salida

Todas las acciones tienen ID, riesgo, reversión y dependencia, y la persona aprobó al menos un bloque.
