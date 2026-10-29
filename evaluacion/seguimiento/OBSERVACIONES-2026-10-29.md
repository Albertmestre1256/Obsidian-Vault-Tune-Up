> [!info]- Índice de esta nota (líneas)
> - Líneas 1–9: Este índice
> - Líneas 11–14: Observaciones del aumento de entrada
> - Líneas 15–27: Resultados observados
> - Líneas 28–37: Brisa: navegación y búsqueda filtrada
> - Líneas 38–43: Nexo: lectura completa del manual
> - Líneas 44–56: Texto adicional y búsquedas amplias
> - Líneas 57–62: Límites que deben conservarse
> - Líneas 63–67: Fuentes y reproducción

# Observaciones del aumento de entrada

Instantánea del 29/10/2026. Cuatro sesiones con corpus ficticio: Brisa A/B y Nexo B/A. A es la instantánea anterior; B, una aplicación previa del kit preparada el 25/10. No se evaluó una reorganización nueva. Modelo reportado claude-sonnet-5-5, esfuerzo solicitado high, Claude Code 2.1.304. El commit registrado antes de ejecutar fue ba6d0d8bf51f0df9638f56fb2a2adefd90e9c75a; 386b8aa incorporó documentación posterior. Ninguno acredita por sí solo el productor histórico de B.

## Resultados observados

| Sesión | Nodo y condición | Entrada acumulada | Solicitudes | Pico por solicitud | Tiempo total |
|---|---|---:|---:|---:|---:|
| N01 | Brisa A | 28.959 | 4 | 9.243 | 17,809 s |
| N02 | Brisa B | 50.542 | 6 | 11.427 | 24,875 s |
| N03 | Nexo B | 56.366 | 5 | 19.015 | 20,291 s |
| N04 | Nexo A | 53.914 | 5 | 17.742 | 21,836 s |

Entrada A total: 82.873. Entrada B total: 106.908. Diferencia: 24.035 tokens (+29,00 %). Brisa aporta 21.583 tokens del aumento (89,80 %); Nexo, 2.452. Las primeras solicitudes de A/B coincidieron: 5.096 tokens para Brisa y 5.057 para Nexo. La diferencia se acumuló durante la recuperación, no en esa primera entrada.

Las cuatro respuestas resolvieron los campos semánticos, roles, vigencia y destino de trabajo requeridos, según revisión de la misma IA que preparó el ensayo, sin revisión humana independiente. Tres campos correctos de Brisa requirieron adjudicación porque el comparador exigía tipos que el prompt no había fijado. Las copias conservaron sus hashes. No hubo nuevas llamadas a modelos para el diagnóstico posterior.

## Brisa: navegación y búsqueda filtrada

N01 leyó reglas, mapa y las cinco notas centrales en una misma ronda de herramientas, después de la entrada inicial. N02 separó reglas, mapa e índice temático de la lectura de las cinco notas. Esa secuencia agregó una ronda al modelo. Después ocurrió un reintento de búsqueda.

N02-T11, solicitud 4: Grep con patrón proveedor|contratad|Brisa, salida content, búsqueda sin distinguir mayúsculas y glob !Versiones conservadas/** devolvió cero coincidencias. N02-T12, solicitud 5, con el mismo patrón y sin ese glob devolvió 25 líneas, cinco de ellas del índice conservado. Localizadores en F02: líneas JSONL 25–26 y 28–29, respectivamente.

Una comprobación offline con rg sobre la misma copia y esa exclusión encontró 20 líneas. F06 conserva comando, versión y salida. Esto prueba una discrepancia entre el resultado observado de Grep y esa referencia; no reproduce la implementación interna de Grep. No se ha establecido si la causa es su interpretación del glob, el cliente u otra condición. Por eso el reintento no se declara innecesario ni se propone quitarlo sin resolver primero la anomalía (P01).

La suma de las primeras cuatro solicitudes de B supera a las cuatro de A en 130 tokens; las solicitudes 5–6 de B aportan 21.453. Es una reconciliación contable por ordinal: las etapas no son equivalentes, y eliminar dos solicitudes cambiaría el resto del historial. No equivale a un ahorro causal de 21.453 tokens.

## Nexo: lectura completa del manual

N03 y N04 realizaron cinco solicitudes cada una. En ambas, Read recibió la ruta del manual sin offset ni limit: no se seleccionaron rangos. N03-T07 leyó Datos/nexo-manual.md; N04-T07, Apuntes/nexo-manual.md. Sus llamadas y resultados están en líneas JSONL 16–17 de F03 y F04. Read informó 297 y 276 líneas, respectivamente, incluido el salto final reportado.

B añadió navegación e índices, pero el agente no evitó la lectura completa. Esto respalda probar selección de secciones (P04); no demuestra que todos los demás pasajes fueran prescindibles para comprender el nodo ni atribuye una cifra exacta de tokens al índice.

## Texto adicional y búsquedas amplias

Las cuatro sesiones ejecutaron Glob **/* al comenzar: 35 archivos listados en A y 44 en B. Las búsquedas de B mezclaron el nombre del nodo con términos de datos ausentes, recuperando títulos, referencias y versiones conservadas. N03-T09 devolvió 13 líneas, tres del índice anterior, con checksum|sha|hash|Nexo; ver F03, líneas 21–22.

| Sesión | Navegación Read | Contenido Read | Resultados Grep | Resultados Glob |
|---|---:|---:|---:|---:|
| N01 | 2.169 | 1.325 | 301 | 810 |
| N02 | 3.098 | 1.921 | 2.217 | 1.201 |
| N03 | 3.061 | 24.803 | 1.071 | 1.201 |
| N04 | 2.169 | 23.762 | 802 | 810 |

Unidades: caracteres, no tokens. Navegación y contenido usan el cuerpo devuelto por Read; Grep y Glob usan el texto visible de sus resultados. No se suman estas columnas para estimar tokens ni para atribuir causalidad. La clasificación y las operaciones individuales están en F05.

## Límites que deben conservarse

La entrada acumulada suma input_tokens, cache_creation_input_tokens y cache_read_input_tokens de Claude. La suma por solicitudes únicas coincide con el resultado final; no se agregan nuevamente modelUsage ni el desglose de duración de caché. Incluye instrucciones, herramientas e historial reprocesado. Los tokens exclusivos de documentos quedan N/D.

Hay dos nodos, una repetición y caché sin vaciar; no se aisló cada componente. Los resultados no prueban mínimo suficiente, eficacia general ni velocidad pura del disco. La coherencia se contrastó en estas respuestas; enlaces resolubles no certifican comprensión. Ver también [método de eficiencia](../EFICIENCIA-NODOS.md).

## Fuentes y reproducción

F01–F04: eventos originales N01–N04; F05: desglose derivado; F06: reproducción de búsqueda; F07: plan, calidad y recursos del ensayo; F08: planilla y verificaciones. El anexo local descrito en [Leer primero](LEER-PRIMERO.md) relaciona cada ID con rutas y SHA-256. Las trazas permanecen privadas por sus posibles metadatos de cuenta.

La [referencia oficial de Grep](https://code.claude.com/docs/en/tools-reference#grep-tool-behavior), consultada el 29/10/2026, describe filtros glob, pero no establece por sí sola qué ocurrió con la exclusión de esta sesión. Toda explicación causal nueva debe enlazar una reproducción y registrarse como seguimiento, sin sustituir los resultados históricos de esta nota.
