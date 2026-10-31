> [!info]- Índice de esta nota (líneas)
> - Líneas 1–15: Este índice
> - Líneas 17–20: Problemas de eficiencia y trabajo pendiente
> - Líneas 21–37: Estado general
> - Líneas 38–41: Cómo actualizar una ficha
> - Líneas 42–54: P01 — Búsqueda filtrada devuelve cero
> - Líneas 55–66: P02 — Más rondas de navegación
> - Líneas 67–78: P03 — Búsquedas demasiado amplias
> - Líneas 79–90: P04 — Manual completo pese a índices
> - Líneas 91–102: P05 — Navegación e índices agregan texto
> - Líneas 103–114: P06 — Inventario completo al comenzar
> - Líneas 115–126: P07 — Historial y caché mezclados con documentos
> - Líneas 127–138: P08 — Tipos de salida ambiguos
> - Líneas 139–150: P09 — Dos nodos y una repetición
> - Líneas 151–161: P10 — Versión de creación de B incompleta

# Problemas de eficiencia y trabajo pendiente

Registro vivo iniciado el 29/10/2026. Fuente inicial: planilla y desglose del diagnóstico. No regenerar este archivo desde la planilla sobre ediciones posteriores. Conservar los IDs y el historial de decisiones.

## Estado general

P01 tiene mitigación local validada e instrucción implementada; falta validación con agente y el fallo original persiste. P02–P10 siguen abiertos. Las observaciones se respaldan en [la instantánea](OBSERVACIONES-2026-10-29.md); los relevos e intentos, en [el registro](REGISTRO.md).

| ID | Prioridad | Etapa | Responsable | Tema |
|---|---|---|---|---|
| P01 | Alta | Mitigado localmente | Sin asignar | Espacios en glob de Grep |
| P02 | Alta | Diseñar prueba | Sin asignar | Más rondas de navegación |
| P03 | Alta | Diseñar prueba | Sin asignar | Búsquedas demasiado amplias |
| P04 | Alta | Diseñar prueba | Sin asignar | Manual completo pese a índices |
| P05 | Media | Diseñar prueba | Sin asignar | Navegación e índices agregan texto |
| P06 | Media | Diseñar prueba | Sin asignar | Inventario completo al comenzar |
| P07 | Alta | Documentar | Sin asignar | Historial y caché mezclados con documentos |
| P08 | Media | Diseñar prueba | Sin asignar | Tipos de salida ambiguos |
| P09 | Alta | Documentar | Sin asignar | Dos nodos y una repetición |
| P10 | Media | Documentar | Sin asignar | Versión de creación de B incompleta |

## Cómo actualizar una ficha

Al tomar trabajo, reemplazar Sin asignar por IA, herramienta y fecha; indicar el alcance y añadir una entrada en REGISTRO.md. Al salir, dejar el resultado y próxima acción, y liberar o acordar el relevo. Mantener coherentes la tabla y la ficha. Un estado Cerrado exige el criterio de aceptación y evidencia enlazada; si solo se documentó una limitación, declararlo sin afirmar una mejora del kit.

## P01 — Espacios en glob de Grep

- Prioridad: Alta.
- Etapa: Mitigado localmente; validación con agente pendiente. Responsable activo: Sin asignar. Último trabajo: IA:Codex, 29/10/2026.
- Evidencia actual: reproducción nativa en Claude Code 2.1.304, sin modelo. El patrón con espacio devuelve cero; el caso de dos archivos reproduce el fallo. Un patrón alternativo validado recupera las veinte coincidencias del corpus B.
- Mecanismo respaldado: el espacio se interpreta como separador de patrones; varios globs separados funcionan como lista y el escape con barra inversa produce un error sobre el prefijo truncado. No se inspeccionó el código interno del cliente.
- Localizador: [informe P01](../P01-GREP.md); expediente local p01-grep-2026-10-29-01; registro R002. Los hechos históricos N02-T11/T12 se conservan.
- Dependencias: P08 y P09 antes de probar ahorro y comprensión con un agente.
- Próxima acción: evaluar la instrucción del paso 2 en un flujo acotado con rúbrica fija; registrar si evita el cero falso y cuánto cuesta verificar el filtro.
- Criterio de aceptación: Grep nativo encuentra casos positivos conocidos con el filtro acordado; no confunde cero con ausencia y registra límites. La mitigación local lo satisface en los controles probados; falta su adopción por el agente.
- Implementación y validación: orientación acotada añadida al paso 2. Cinco controles pasaron en dos repeticiones; el filtro positivo coincide exactamente en rutas, líneas y texto con el esperado. Copias intactas. No se cambió el ejecutable ni se corrigió el comportamiento original; no cerrar como fallo del cliente resuelto.
- Registro de intentos: R002 conserva positivos, rojos, error explícito de escape y pruebas de mitigación. La planilla anterior sigue como instantánea.

## P02 — Más rondas de navegación

- Prioridad: Alta.
- Etapa: Diseño preparado; comparación controlada pendiente. Responsable activo: Sin asignar. Último trabajo: IA:Codex (Codex desktop), 30/10/2026.
- Evidencia actual: N01 tiene 4 solicitudes del modelo, 11 invocaciones y 28.959 tokens de entrada acumulada; N02, 6 solicitudes, 12 invocaciones y 50.542 tokens. Una solicitud adicional corresponde a leer el índice temático antes de las cinco notas centrales; la otra, al reintento tras el cero falso de P01. N02 también leyó un índice más. El aumento (+74,5 % de entrada) es descriptivo del par y no se atribuye causalmente a la navegación.
- Localizador: N01 vs N02, hoja Llamadas. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: P01 mitigado localmente; P08 y P09 antes de evaluar comprensión y ahorro.
- Próxima acción: Comparar lectura agrupada y progresiva con la misma tarea, corpus, objetivos y archivos; eludir el glob defectuoso o usar el filtro P01 validado.
- Criterio de aceptación: Menos rondas o menor entrada sin perder objetivo, roles, vigencia, rutas ni evidencia en tareas nuevas.
- Implementación y validación: diagnóstico descriptivo; el par N01/N02 no aísla causas ni acredita ahorro. No se ejecutaron sesiones nuevas. Diseño en P02-NAVEGACION.md.
- Registro de intentos: R003 documenta la auditoría y relevo; comparación experimental pendiente de P08, P09 y presupuesto nuevo.

## P03 — Búsquedas demasiado amplias

- Prioridad: Alta.
- Etapa: Diseñar prueba. Responsable: Sin asignar.
- Evidencia actual: Mecanismo observado. N02/N03 agregan el nombre del nodo a los patrones para datos ausentes y recuperan índices e historia.
- Localizador: N02-T12; N03-T09. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: P01 para validar búsquedas filtradas.
- Próxima acción: Separar descubrimiento por tema de verificación dirigida de ausencias.
- Criterio de aceptación: Búsqueda dirigida responde la ausencia correctamente; historia queda accesible cuando pueda cambiar la respuesta.
- Implementación y validación: pendientes. Añadir reproducción, resultados, diff/commit y conservación cuando existan; no marcar como realizado lo que solo está propuesto.
- Registro de intentos: sin entradas específicas todavía; ver R001 para el alta documental.

## P04 — Manual completo pese a índices

- Prioridad: Alta.
- Etapa: Diseñar prueba. Responsable: Sin asignar.
- Evidencia actual: Mecanismo observado. Nexo usa Read sin offset/limit en ambos brazos; B añade índice pero también lee todo el manual.
- Localizador: N03-T07; N04-T07. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: P08 y P09 antes de comparar comprensión.
- Próxima acción: Probar índice primero y secciones acotadas; exigir comprensión equivalente.
- Criterio de aceptación: Rangos recuperan todos los hechos y relaciones requeridos; una sección omitida no introduce errores de vigencia.
- Implementación y validación: pendientes. Añadir reproducción, resultados, diff/commit y conservación cuando existan; no marcar como realizado lo que solo está propuesto.
- Registro de intentos: sin entradas específicas todavía; ver R001 para el alta documental.

## P05 — Navegación e índices agregan texto

- Prioridad: Media.
- Etapa: Diseñar prueba. Responsable: Sin asignar.
- Evidencia actual: Mecanismo observado. B devuelve más texto de reglas, índice temático y notas indexadas. No hay tokenización documental aislada.
- Localizador: Herramientas: categoría Navegación. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: P04 para medir beneficio neto.
- Próxima acción: Medir el coste propio de navegación frente al contexto útil que permite evitar.
- Criterio de aceptación: Beneficio neto de navegación medido con uso real y mismo nivel de comprensión; originales e índices exactos conservados.
- Implementación y validación: pendientes. Añadir reproducción, resultados, diff/commit y conservación cuando existan; no marcar como realizado lo que solo está propuesto.
- Registro de intentos: sin entradas específicas todavía; ver R001 para el alta documental.

## P06 — Inventario completo al comenzar

- Prioridad: Media.
- Etapa: Diseñar prueba. Responsable: Sin asignar.
- Evidencia actual: Observado; ahorro hipotético. Las cuatro sesiones ejecutan Glob **/*: 35 archivos en A, 44 en B.
- Localizador: N01–N04, primer Glob. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: P08 y P09 antes de comparar calidad.
- Próxima acción: Comparar descubrimiento dirigido con inventario completo; conservar vías de respaldo.
- Criterio de aceptación: Descubrimiento dirigido cubre notas centrales; si el mapa falla, activa respaldo explícito sin inventar rutas.
- Implementación y validación: pendientes. Añadir reproducción, resultados, diff/commit y conservación cuando existan; no marcar como realizado lo que solo está propuesto.
- Registro de intentos: sin entradas específicas todavía; ver R001 para el alta documental.

## P07 — Historial y caché mezclados con documentos

- Prioridad: Alta.
- Etapa: Documentar. Responsable: Sin asignar.
- Evidencia actual: Límite de medición. Cada solicitud procesa instrucciones e historial. Más entrada acumulada no significa igual cantidad de información nueva.
- Localizador: Llamadas F:H; recursos.json. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: Ninguna.
- Próxima acción: Mantener entrada por solicitud y acumulada; documentos exclusivos N/D.
- Criterio de aceptación: Suma por solicitudes únicas coincide con uso final; caché sin duplicación y tokens documentales N/D si no observables.
- Implementación y validación: pendientes. Añadir reproducción, resultados, diff/commit y conservación cuando existan; no marcar como realizado lo que solo está propuesto.
- Registro de intentos: sin entradas específicas todavía; ver R001 para el alta documental.

## P08 — Tipos de salida ambiguos

- Prioridad: Media.
- Etapa: Rúbrica en borrador con clave Brisa y citas por condición; congelación pendiente. Responsable: IA:Codex. Último trabajo: IA:Codex (Codex desktop), 30/10/2026.
- Evidencia actual: Defecto del evaluador. Tres campos correctos de Brisa fallan por tipo en comparación exacta; el prompt permitía texto o número.
- Localizador: calidad-sin-consumo.json; revisión semántica. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: Ninguna.
- Próxima acción: Revisar y congelar P08 para la tarea Brisa de P02; asignar revisión independiente antes de abrir nuevas salidas.
- Criterio de aceptación: Valores equivalentes reciben la misma nota en A/B; tipos y casos límite fijados antes de nuevas sesiones.
- Implementación y validación: contrato semántico redactado; no se modificó el evaluador ni se re-puntuaron sesiones históricas. Diseño en P08-RUBRICA.md.
- Registro de intentos: R004 documenta el borrador; R005 añade la clave Brisa; congelación y aplicación pendientes.

## P09 — Dos nodos y una repetición

- Prioridad: Alta.
- Etapa: Prerregistro P02 y guion de interacción en borrador; presupuesto y revisión independiente pendientes. Responsable: IA:Codex. Último trabajo: IA:Codex (Codex desktop), 30/10/2026.
- Evidencia actual: Límite de inferencia. No aísla componentes ni establece causalidad, mínimo de contexto o eficacia general.
- Localizador: plan.json; N01–N04. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: P07 y P08; cuatro sesiones exploratorias previas agotadas.
- Próxima acción: Revisar P08/P09 y el guion de interacción, congelar hashes/modelo/entorno y asignar revisor; pedir presupuesto nuevo antes de ejecutar.
- Criterio de aceptación: Preregistro y presupuesto fijados; revisión sin consumo y al menos una revisión independiente antes de afirmar mejora.
- Implementación y validación: diseño de factibilidad propuesto con dos pares contrabalanceados, preludio común y guion de interacción; no congelado ni ejecutado. Diseño en P09-PREREGISTRO-P02.md y P02-INTERACCIONES-BRISA.md.
- Registro de intentos: R004 documenta el borrador; R005 aclara corpus y lecturas; R006 registra la auditoría de secuencia y el guion; no hubo sesiones nuevas.

## P10 — Versión de creación de B incompleta

- Prioridad: Media.
- Etapa: Documentar. Responsable: Sin asignar.
- Evidencia actual: Brecha de procedencia. Se conoce el hash de B y el commit al consultar; ese commit no certifica qué versión produjo B el 25/10.
- Localizador: plan.json; manifiesto-B.json. Las referencias locales se resuelven mediante F01–F08 en OBSERVACIONES-2026-10-29.md.
- Dependencias: Ninguna.
- Próxima acción: Archivar manifiesto, versión productora, reglas y transformaciones por separado.
- Criterio de aceptación: Cada B futura tiene commit productor, reglas, mapa y manifiesto; la brecha histórica se declara si no se recupera.
- Implementación y validación: pendientes. Añadir reproducción, resultados, diff/commit y conservación cuando existan; no marcar como realizado lo que solo está propuesto.
- Registro de intentos: sin entradas específicas todavía; ver R001 para el alta documental.
