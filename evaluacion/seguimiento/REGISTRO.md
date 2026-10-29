> [!info]- Índice de esta nota (líneas)
> - Líneas 1–7: Este índice
> - Líneas 9–12: Registro de coordinación y resultados
> - Líneas 13–22: R001 — Documentación inicial — 2026-10-29
> - Líneas 23–33: R002 — P01: reproducción y mitigación local — 2026-10-29
> - Líneas 34–54: Plantilla para una nueva entrada
> - Líneas 55–59: Requisitos de una entrada de cierre

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
