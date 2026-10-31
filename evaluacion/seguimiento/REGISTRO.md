> [!info]- Índice de esta nota (líneas)
> - Líneas 1–14: Este índice
> - Líneas 16–19: Registro de coordinación y resultados
> - Líneas 20–29: R001 — Documentación inicial — 2026-10-29
> - Líneas 30–40: R002 — P01: reproducción y mitigación local — 2026-10-29
> - Líneas 41–50: R003 — P02: auditoría offline de navegación — 2026-10-30
> - Líneas 51–59: R004 — P08/P09: borradores de rúbrica y prerregistro — 2026-10-30
> - Líneas 60–69: R005 — P02: especificación de preludio y clave Brisa —
> - Líneas 70–79: R006 — P02: auditoría de secuencia y guion — 2026-10-30
> - Líneas 80–87: R007 — P02: ficha para revisión independiente — 2026-10-30
> - Líneas 88–97: R008 — P02: despejar conflicto del preludio — 2026-10-31
> - Líneas 98–107: R009 — P02: alinear cegamiento y citas prospectivas — 2026-10-31
> - Líneas 108–128: Plantilla para una nueva entrada
> - Líneas 129–133: Requisitos de una entrada de cierre

# Registro de coordinación y resultados

Añadir entradas fechadas; no borrar intentos fallidos ni reemplazar conclusiones anteriores. Referir siempre los IDs P01–P10 de [problemas](PROBLEMAS.md). El estado actual se actualiza allí; este archivo explica cómo se llegó a él.

## R001 — Documentación inicial — 2026-10-29

- Autor: IA:Codex (aplicación Codex; modelo no acreditado en este registro).
- Alcance: observaciones históricas y fichas P01–P10 respaldadas en Markdown a pedido de Albert.
- Resultado: diagnóstico trasladado desde el expediente y la planilla, con localizadores; entrada de lectura breve y reglas de relevo preparadas.
- Evidencia: OBSERVACIONES-2026-10-29.md; anexo local FUENTES-LOCALES.md. Base del repositorio al retomar: 386b8aa31f1c865c46be8c4a21baec5a9c02ba8f.
- Cambios de producto: ninguno. No se implementaron soluciones ni se iniciaron modelos para probarlas.
- Responsable activo: ninguno; las diez fichas quedan libres para una asignación posterior.
- Siguiente acción: tomar P01 y preparar reproducción nativa de la búsqueda; atender P08 antes de nuevas comparaciones de calidad.

## R002 — P01: reproducción y mitigación local — 2026-10-29

- Autor: IA:Codex (Codex desktop), a pedido de Albert: «comenza por p01».
- Alcance: herramienta Grep nativa de Claude Code 2.1.304 expuesta por MCP; copias ficticias nuevas, sin invocar un modelo. Se preservó el arranque inicial sin respuesta y cada intento posterior.
- Hecho: original 0 frente a 20 esperados; sin filtro 25. Caso reducido a dos archivos: 0 frente a 1 esperado. Negaciones sin espacio funcionan; una ruta con espacios funciona mediante path.
- Hipótesis contrastadas: división del glob por espacios, exclusión de carpeta existente y particularidades del corpus B. La primera explica el caso mínimo, la lista de patrones y el error de prefijo al escapar el espacio; las otras no explican esos controles.
- Resultado: filtro positivo de alcance conocido y controles pasaron dos veces; sus veinte rutas, líneas y textos coinciden con rg. Todos los manifiestos de copias comparados conservaron contenido.
- Implementación: paso 2 indica verificar ceros contradictorios y usar path exacto para carpetas con espacios; no sustituirlos por comodines. Informe en evaluacion/P01-GREP.md; código experimental y trazas fuera del repositorio.
- Límite: mitigación local, no reparación del cliente ni prueba de que una IA siga la instrucción. Sin ahorro de tokens acreditado. Reversión del kit: retirar el párrafo añadido al paso 2, conservando evidencia e historial.
- Estado al salir: P01 mitigado localmente, responsable liberado; continuar con P08/P09 antes de una prueba con agente. La entrada de Obsidian coordina responsables; este registro describe implementación y resultados y no se sincroniza automáticamente.

## R003 — P02: auditoría offline de navegación — 2026-10-30

- Autor: IA:Codex (Codex desktop, GPT-6), por indicación de Albert de continuar con P02.
- Alcance: revisar eventos N01/N02 y separar rondas del modelo, invocaciones de herramientas y el reintento P01. Sin sesiones nuevas con Claude Code ni cambios a las bóvedas; dos revisiones internas fueron de solo lectura.
- Base: commit 70b81d04e96217ef3c4a7d701c5ad7406cd1b48d; rama `codex/flujo-10-pasos`; copia y trazas preexistentes bajo I:.
- Hecho: 4 frente a 6 solicitudes del modelo; 11 frente a 12 invocaciones de herramientas. Una solicitud extra es lectura progresiva del índice temático y las cinco notas; la otra, el reintento del Grep con cero falso de P01.
- Límite: un solo par con corpus, historial y salidas distintos; la descomposición describe esas trazas, no predice ahorro causal.
- Resultado: [diseño P02](../P02-NAVEGACION.md) fija una comparación futura con corpus y objetivos constantes, y condiciones de lectura agrupada/progresiva. No se afirma eficacia.
- Responsable al inicio: IA:Codex; liberado al salir. P02 sigue abierto: P08/P09 y presupuesto nuevo preceden a la comparación; el tope exploratorio previo de cuatro sesiones ya se consumió.

## R004 — P08/P09: borradores de rúbrica y prerregistro — 2026-10-30

- Autor: IA:Codex (Codex desktop, GPT-6), por indicación de Albert de continuar el diagnóstico.
- Alcance: preparar el contrato de puntuación semántica P08 y un prerregistro de factibilidad específico para P02. Solo documentación; sin sesiones nuevas ni cambios a las bóvedas.
- Resultado: P08 separa tipos, equivalencia semántica, evidencia y abstención, y prohíbe alterar las puntuaciones automáticas históricas. P09 propone dos pares balanceados (cuatro sesiones), exclusivamente para factibilidad; no permite afirmar eficacia.
- Límite: ambos borradores esperan revisión/congelación; aún falta revisor independiente, hash/configuración final y nuevo presupuesto autorizado. El tope previo de cuatro sesiones está consumido.
- Referencias: [rúbrica P08](../P08-RUBRICA.md); [prerregistro P09 para P02](../P09-PREREGISTRO-P02.md). No se ejecutaron pruebas ni modelos.
- Responsable liberado: IA:Codex. Próximo paso: revisar y congelar alcance con Albert; obtener revisor y autorización antes de sesiones.

## R005 — P02: especificación de preludio y clave Brisa — 2026-10-30

- Autor: IA:Codex (Codex desktop, GPT-6), por indicación de Albert de continuar.
- Alcance: corregir ambigüedad documental del conjunto de lecturas y hacer puntuable la tarea P02 sin ejecutar sesiones.
- Hecho observado: P02/P09 fijaban ocho archivos comparados, pero no distinguían `LEER_PRIMERO.md`; P08 no cubría objetivo, cinco roles, vigencia, destino ni evidencia por condición.
- Cambio: N02 queda propuesto como corpus fijo; preludio común `LEER_PRIMERO.md` más ocho archivos medidos; P08 añade clave de Brisa y rangos válidos para N01/N02. Se acota `proveedor=null` a las cinco notas centrales efectivamente leídas.
- Resultado: solo borradores; no se ejecutaron modelos, pruebas ni cambios de bóvedas. Revisión independiente y presupuesto continúan pendientes; sin autorización no se ejecutarán sesiones.
- Referencias: [P02](../P02-NAVEGACION.md), [P08](../P08-RUBRICA.md), [P09](../P09-PREREGISTRO-P02.md). La clave remite a datos sintéticos ya presentes en el expediente local.
- Responsable: IA:Codex. Próximo paso: revisar independientemente P08/P09, corregir objeciones, congelar calendario/manifiestos y solicitar autorización de presupuesto.

## R006 — P02: auditoría de secuencia y guion — 2026-10-30

- Autor: IA:Codex (Codex desktop, GPT-6), por indicación de Albert de continuar.
- Alcance: contrastar la interacción P02 con las trazas originales y redactar un guion fijo para el piloto sin iniciar sesiones.
- Hecho observado: N01 y N02 leen `LEER_PRIMERO.md` y generan `Glob("**/*")` en el mismo `request_id`; luego N01 lee reglas, índice y cinco notas, mientras N02 lee además el índice temático antes de esas notas.
- Cambio: el inventario Glob se fija como parte del preludio común; se define N02 como corpus para aislar secuencia. Se redacta mensaje base, preludio, orden agrupado y dos fases progresivas; la variante P02 prohíbe Grep y acota la abstención de proveedor.
- Resultado: guion en borrador en [P02-INTERACCIONES-BRISA.md](../P02-INTERACCIONES-BRISA.md); no se ejecutaron modelos ni pruebas. Revisión independiente, hash final y presupuesto nuevo pendientes.
- Referencias: [P02](../P02-NAVEGACION.md), [P08](../P08-RUBRICA.md), [P09](../P09-PREREGISTRO-P02.md). Evidencia original: N01/N02 `eventos.jsonl` en expediente privado.
- Responsable: IA:Codex. Próximo paso: revisión independiente del guion y protocolo; no iniciar sesión antes de autorización de presupuesto.

## R007 — P02: ficha para revisión independiente — 2026-10-30

- Autor: IA:Codex (Codex desktop, GPT-6), por indicación de Albert de continuar.
- Alcance: hacer verificable la revisión de P08/P09 y del guion sin abrir sesiones de modelo.
- Cambio: se añadió una lista de control y formato de devolución en [P02-REVISION-INDEPENDIENTE.md](../P02-REVISION-INDEPENDIENTE.md); P09 y el seguimiento enlazan la ficha.
- Resultado: material listo para revisión; no equivale a una revisión independiente ni congela el protocolo. No hubo sesiones, pruebas ni cambios en bóvedas.
- Próximo paso: asignar persona revisora independiente, registrar objeciones y responder antes de congelar; presupuesto nuevo sigue pendiente.

## R008 — P02: despejar conflicto del preludio — 2026-10-31

- Autor: IA:Codex (Codex desktop), por indicación de Albert de continuar.
- Alcance: autorrevisión del guion, P08/P09 y ficha; sin ejecutar modelos.
- Hecho observado: el mensaje común pedía JSON final mientras el preludio pedía responder solo `PRELUDIO_LISTO`.
- Cambio: el guion ahora condiciona el JSON a recibir la fase de respuesta final; la ficha independiente incluye este chequeo. Hash candidato del guion: `cb83fdea71e3de9b5e17a6c5101b5f68e91e9027e254d592124324326de7830e`.
- Verificación: `indice_lineas.py check` OK en guion, ficha y P09; `git diff --check` limpio. El hash del manifiesto N02 se cotejó y conservó.
- Límites: autorrevisión, no revisión independiente; no se congeló el protocolo ni se ejecutaron sesiones. El presupuesto nuevo sigue pendiente.
- Próximo paso: revisor independiente aplica la ficha a guion, P08 y P09; resolver observaciones antes de congelar.

## R009 — P02: alinear cegamiento y citas prospectivas — 2026-10-31

- Autor: IA:Codex (Codex desktop), por indicación de Albert de continuar.
- Alcance: autorrevisión cruzada de P08, P09 y la ficha de revisión; sin nuevas sesiones.
- Hecho observado: P08 describía el cegamiento histórico A/B; el piloto propuesto usa N02 en ambos brazos y compara agrupada/progresiva.
- Cambio: se limitó la evidencia aceptable futura a rutas N02; N01 queda histórica. Los revisores recibirán respuestas con IDs aleatorios sin condición, orden, tokens ni duración visibles. La ficha ahora exige verificar esos límites.
- Verificación: `indice_lineas.py check` OK en tres documentos y `git diff --check` limpio.
- Límites: revisión propia, no independiente; no se congeló el protocolo ni se consumieron sesiones. Presupuesto nuevo pendiente.
- Próximo paso: revisor independiente aplica la ficha actualizada y registra dictamen y objeciones.

## Plantilla para una nueva entrada

Usar el siguiente número R disponible y un título con problema y fecha. Completar solo lo que ocurrió; declarar N/D donde falte evidencia.

```text
R___ — P__ — fecha y zona
IA, herramienta y modelo acreditado si se conoce:
Responsable anterior / relevo acordado:
Alcance tomado y archivos que editará:
Commit base / rama / carpeta de trabajo:
Hecho observado y fuente con hash/localizador:
Hipótesis y alternativa que se intenta distinguir:
Prueba, configuración, entradas y límites fijados:
Resultado real, incluidos fallos y consumo:
Comprensión, evidencia y conservación verificadas:
Decisión: mantener, modificar, descartar o seguir investigando:
Diff / commit implementado / documentación afectada:
Reversión o recuperación prevista:
Estado al salir / responsable siguiente / próxima acción:
```

## Requisitos de una entrada de cierre

Indicar la ficha y el criterio satisfecho; enlazar reproducción, resultado antes/después, implementación y documentación actualizada. Distinguir cierre de un defecto concreto de una afirmación de ahorro general. Si solo se descartó una hipótesis o se documentó una limitación, dejar explícito ese alcance.

Actualizar responsable y estado de la ficha en el mismo cambio. Antes de guardar, releer los archivos y el estado de Git para detectar trabajo concurrente. Un texto de intención, una prueba preparada o un commit sin validar no cierran el problema.
