> [!info]- Índice de esta nota (líneas)
> - Líneas 1–8: Este índice
> - Líneas 10–13: Propósito y estado
> - Líneas 14–19: Pregunta, estimando y unidad
> - Líneas 20–29: Condiciones y controles
> - Líneas 30–35: Medidas y análisis
> - Líneas 36–41: Muestra, presupuesto y revisión
> - Líneas 42–44: Exclusiones y parada

# P09: prerregistro del piloto P02

30/10/2026. Borrador de protocolo, no congelado. No autoriza sesiones. La autorización exploratoria previa de cuatro sesiones ya se consumió.

## Pregunta, estimando y unidad

En una tarea fija sobre una bóveda ficticia, ¿la lectura agrupada reduce la entrada acumulada o las solicitudes frente a la lectura progresiva sin perder comprensión? El estimando futuro sería la diferencia pareada observada entre condiciones en este protocolo; no una mejora universal del kit. Unidad: un par de sesiones nuevas que resuelve la misma tarea y comparte corpus, prompt base, modelo y configuración.

Primera fase propuesta: piloto de factibilidad, dos pares (cuatro sesiones), un nodo y una tarea: Brisa, con el prompt exacto identificado por SHA-256 `3314fbd1330bed36537c361810dc2b4e3fcf6b7d75beee4116040ca5d778a504`. El corpus de partida es la instantánea organizada N02; SHA-256 de `N02/manifiesto-inicial.json`: `31951d3a622dbaf487b675a379a53a46ff305236f828b088ed4b51e7382221a9`. Cada sesión usa una copia fresca cuyos archivos deben coincidir con ese manifiesto antes y después. Solo comprobaría que las condiciones y la instrumentación funcionan. No permite inferencia causal general, mínimo de contexto, ni conclusión de eficacia. Para una afirmación confirmatoria hacen falta más tareas, bóvedas y tamaño muestral calculado; quedan fuera de este piloto.

## Condiciones y controles

- **Preludio común:** leer `LEER_PRIMERO.md` en ambas condiciones. Su lectura y coste se cuentan en cada sesión y también se informan por separado.
- **Agrupada:** después del preludio común, solicitar en una respuesta los ocho archivos medidos: `Reglas.md`, `INDICE.md`, `Energía/00 - Índice - Energía.md`, `Energía/brisa-plan.md`, `Energía/brisa-acta.md`, `Energía/brisa-presupuesto.md`, `Energía/brisa-propuesta.md` y `Archivo/brisa-2030.md`.
- **Progresiva:** después del preludio común, solicitar en una respuesta `Reglas.md`, `INDICE.md` e `Energía/00 - Índice - Energía.md`; en una segunda respuesta, solicitar las mismas cinco notas centrales restantes.
- En ambas condiciones leer los mismos nueve archivos totales (preludio común más ocho archivos medidos) y usar el mismo prompt, tarea, rutas, herramienta y permisos. Usar copias frescas del corpus organizado N02, verificar el mismo manifiesto antes y después; cada intento recibe una copia idéntica. El manifiesto fijo controla descubrimiento de rutas: este piloto no lo evalúa.
- Crear una copia idéntica e inmutable por sesión; guardar hash antes/después. Cada sesión inicia sin historial previo. Registrar modelo exacto, cliente, configuración, caché y campos no controlables.
- No usar Grep en la tarea principal. Si resulta indispensable, pausar el piloto y preregistrar una variante que aplique idéntico filtro positivo verificado en ambos brazos; no sustituir fallos P01 por reintentos silenciosos.
- Usar Sonnet 5.5 alto solo si el evento de inicio confirma el modelo; registrar la versión real de Claude Code el día de cada sesión. Cambio de modelo o cliente exige enmienda antes de ejecutar.

## Medidas y análisis

Primaria de recursos: entrada acumulada por sesión desde el evento final `result.usage` (`input_tokens + cache_creation_input_tokens + cache_read_input_tokens`). Usar `request_id` únicos para contar solicitudes; no sumarles otra vez el uso final de sesión ni `modelUsage`. Registrar la salida una sola vez y por separado. Si falta el resultado final o el uso no se reconcilia con los eventos disponibles, declarar N/D. Secundarias: invocaciones, archivos y caracteres leídos, tiempo de pared y duración API por separado. No inferir tokens documentales de caracteres ni combinar estas medidas en un índice único.

Calidad es una condición de aceptación, no un descuento intercambiable por tokens: aplicar P08 a hechos, roles, vigencia, rutas, evidencia y abstención. Reportar éxito estricto y criterios individuales. Con dos pares, mostrar observaciones pareadas crudas; no calcular significación ni proclamar mejora. Coste ausente es N/D.

## Muestra, presupuesto y revisión

Diseño de factibilidad propuesto: dos pares, uno agrupada→progresiva y uno progresiva→agrupada; registrar el calendario exacto antes de iniciar. Presupuesto de llamadas: máximo cuatro sesiones nuevas; gasto monetario máximo y límites por intento quedan por fijar con Albert. **No ejecutar** hasta recibir nueva autorización de presupuesto. Identificar un revisor independiente que puntúe salidas anonimizadas sin ver consumo; aún no está asignado. Un segundo revisor aplica la misma ficha a ciegas; los desacuerdos se envían a una persona adjudicadora designada antes de congelar.

Congelar antes de correr: hash de corpus y manifiesto, prompt y clave P08, los textos exactos de las órdenes de agrupación/progresión, citas válidas por condición, modelo/cliente/permisos, orden, límites, presupuesto y responsables de revisión/adjudicación. El prompt base y el manifiesto indicados arriba no reemplazan los hashes de esas órdenes, que todavía se deben calcular. Registrar hashes en el expediente privado y publicar solo resúmenes sin metadatos de cuenta.

## Exclusiones y parada

No excluir una respuesta por ser incorrecta, costosa o contraria a la hipótesis. Si falla acceso/modelo antes de leer archivos, conservar el intento y detener el par; no reemplazarlo sin enmienda. Si cambia el corpus o falta uso tokenizado, reportarlo y no afirmar ahorro. Cualquier edición de la bóveda de prueba invalida esa copia; preservar manifiestos y declarar el desvío. No borrar intentos ni trazas.
