> [!info]- Índice de esta nota (líneas)
> - Líneas 1–9: Este índice
> - Líneas 11–14: Registro de coordinación y resultados
> - Líneas 15–24: R001 — Documentación inicial — 2026-10-29
> - Líneas 25–35: R002 — P01: reproducción y mitigación local — 2026-10-29
> - Líneas 36–45: R003 — P02: auditoría offline de navegación — 2026-10-30
> - Líneas 46–54: R004 — P08/P09: borradores de rúbrica y prerregistro — 2026-10-30
> - Líneas 55–75: Plantilla para una nueva entrada
> - Líneas 76–80: Requisitos de una entrada de cierre

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
