> [!info]- Índice de esta nota (líneas)
> - Líneas 1–8: Este índice
> - Líneas 10–13: Eficiencia para comprender un nodo
> - Líneas 14–26: Qué debe entender la IA
> - Líneas 27–41: Medidas que se mantienen separadas
> - Líneas 42–54: Cómo buscar el menor contexto suficiente
> - Líneas 55–60: Cómo evaluar coherencia
> - Líneas 61–78: Ensayo exploratorio del 29 de octubre

# Eficiencia para comprender un nodo

Definición acordada con Albert el 29/10/2026: preparar a una IA para trabajar en un nodo con la menor entrada suficiente, conservando comprensión del contexto y de su conformación. Evaluar también tiempo y coherencia. Complementa [PROTOCOLO.md](PROTOCOLO.md); no agrega una herramienta que deba ejecutar la persona usuaria.

## Qué debe entender la IA

Antes de medir recursos, fijar una tarea de orientación y su respuesta esperada fuera de la bóveda evaluada. No alcanza con recuperar un dato aislado. La respuesta debe identificar:

- Objetivo y alcance del nodo, distinguiendo hechos de inferencias.
- Notas centrales, rutas reales y función de cada una.
- Datos necesarios para la tarea y evidencia efectivamente consultada.
- Fuentes vigentes, historia y propuestas pendientes; autoridad ante conflictos.
- Nota donde correspondería trabajar y restricciones relevantes, sin editarla.
- Datos ausentes e incertidumbres, sin inventarlos.

Usar los mismos requisitos semánticos en A y B; permitir los mecanismos de búsqueda que cada una ya tenga. No pedirle a A que lea toda la bóveda ni darle a B las claves. Registrar aparte fallos de formato y de significado: si se permite texto o números, «8400 créditos» no debe rechazarse por no ser el número JSON 8400. Resolver ambigüedades sin ver el consumo y conservar la salida automática original.

## Medidas que se mantienen separadas

| Medida | Qué responde | Límite |
|---|---|---|
| Contexto documental suministrado | Cuánto material del vault se inyectó | Requiere contador adecuado y paquete o resultados observables; N/D si no se expone |
| Entrada por solicitud y su pico | Cuánto contexto recibió el modelo en cada llamada | Incluye instrucciones, herramientas e historial; no equivale a documentos únicos |
| Entrada acumulada del intento | Cuánto procesamiento de entrada requirió llegar a la respuesta | El historial leído de nuevo cuenta otra vez, incluso en caché |
| Tiempo hasta última lectura | Cuándo terminó la recuperación observable | No incluye el razonamiento posterior ni prueba velocidad pura del disco |
| Tiempo hasta respuesta válida | Cuánto espera la persona | Incluye arranque, red, servicio y generación; separar reintentos |
| Comprensión y coherencia | Si el resultado permite trabajar correctamente | Requiere contrastar evidencia y vigencia; enlaces resolubles no bastan |

Para Claude, sumar las categorías separadas input_tokens, cache_creation_input_tokens y cache_read_input_tokens. No sumar también el desglose de duración de caché ni modelUsage. Si se usa message.usage, agrupar por identificador de mensaje/solicitud para no contar dos veces eventos del mismo mensaje; contrastar la suma con el resultado final. No aplicar esta normalización automáticamente a otros proveedores. [Categorías oficiales de caché](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).

El pico mide la mayor entrada observada en una trayectoria. No demuestra que todo ese contexto fuera necesario. Los caracteres recuperados, líneas y archivos permiten diagnosticar el recorrido; no se convierten en tokens reales mediante caracteres/4. Tampoco restar arbitrariamente un supuesto prompt fijo al total para atribuir el resto a la bóveda.

## Cómo buscar el menor contexto suficiente

Una ejecución libre A/B mide el consumo observado del agente. Para buscar un mínimo hace falta además una curva de comprensión frente a presupuesto:

1. Fijar nodos, tareas, hechos, roles, límites, calidad exigida y repeticiones antes de ejecutar; reservar nodos nuevos para confirmar. No seleccionar la mejor respuesta de muchos intentos.
2. Construir paquetes de contexto con un recuperador y orden fijados, iguales para A/B. Conservar ruta, versión y líneas de cada fragmento. El recuperador puede navegar y buscar; no consultar claves ni elegir pasajes conociendo las respuestas. Contar su trabajo aparte.
3. Probar niveles de entrada decrecientes, fijados previamente. Mantener completos los fragmentos y la identificación de sus fuentes; no cortar justo antes de un estado o advertencia. Cambiar el método de selección constituye otra condición.
4. Con sesión nueva por nivel, entregar únicamente el paquete a una IA sin acceso adicional. Fijar tarea, modelo, esfuerzo y salida, y medir su comprensión con la misma rúbrica. Mantener también la evaluación libre para saber si el agente encuentra ese contexto por sí mismo.
5. Contar tokens con la interfaz apropiada del modelo y guardar el uso real. Si solo se dispone del CLI y no de conteo documental verificable, identificar niveles por fragmentos/bytes y reportar la entrada real posterior; no llamarlos presupuestos exactos de tokens documentales. El endpoint de conteo de mensajes existe en la API de Claude, pero no se presupone disponible mediante una suscripción o un CLI. [Conteo oficial](https://platform.claude.com/docs/en/build-with-claude/token-counting).
6. Informar el nivel más pequeño que cumple la rúbrica en las repeticiones previstas, junto con todos los fallos inferiores y el consumo de recuperación. Llamarlo «menor contexto suficiente observado entre los niveles probados». Con respuestas estocásticas no es un mínimo universal ni una garantía de acierto futuro.

No se fijan aquí cantidades universales: la tarea y el modelo determinan los niveles útiles. No extrapolar de una consulta puntual a comprender cualquier nodo. La calibración no habilita automáticamente una campaña extensa de llamadas.

## Cómo evaluar coherencia

Conservar tres comprobaciones: estructural (rutas y enlaces necesarios resolubles, índices exactos, versiones recuperables); documental (fuente activa, autoridad explícita y contradicciones identificadas); y de respuesta (el agente usa la versión correcta y encuentra dónde actuar). Una contradicción histórica bien marcada no equivale a dos reglas activas incompatibles. Medir incidencias por tarea, con evidencia y gravedad, evitando un promedio que oculte pérdida de contenido.

No puntuar belleza del grafo, cantidad de enlaces o carpeta temática como comprensión. La comparación incluye conservación y mantenimiento de índices. Separar el coste de organizar del coste de consultar; una consulta más barata puede no amortizar la preparación.

## Ensayo exploratorio del 29 de octubre

Cuatro sesiones nuevas de Claude Code 2.1.304, Sonnet 5.5 solicitado en alto y reportado como claude-sonnet-5-5. Dos nodos ficticios, una repetición por condición; orden Brisa A/B y Nexo B/A. A/B son las instantáneas preparadas el 25/10, con los mismos hechos conservados; no se volvió a organizar la bóveda ni se midió la fiabilidad del proceso de organización. El commit vigente al ejecutar fue ba6d0d8bf51f0df9638f56fb2a2adefd90e9c75a; no es el commit histórico de producción de B.

| Nodo | Entrada acumulada A → B | Pico por solicitud A → B | Tiempo total A → B |
|---|---|---|---|
| Brisa | 28.959 → 50.542 | 9.243 → 11.427 | 17,809 → 24,875 s |
| Nexo | 53.914 → 56.366 | 17.742 → 19.015 | 21,836 → 20,291 s |

Las cuatro respuestas resolvieron los cinco campos exigidos de su nodo, las notas centrales y sus roles, la vigencia y el destino de trabajo, con citas contrastadas. La comparación automática de tipos rechazó tres campos textuales correctos de Brisa; se conservaron esos fallos y se adjudicaron semánticamente antes de inspeccionar tokens. La revisión fue de la misma IA que preparó el ensayo, sin revisión humana independiente: no constituye validación externa de calidad.

La entrada acumulada total fue 82.873 en A y 106.908 en B: 29,00 % más en estas dos tareas. Los tiempos fueron mixtos. B añadió navegación y en Nexo el agente leyó el manual completo en ambas condiciones, pese a disponer de índices en B. Esto identifica una hipótesis de mejora para la selección de rangos; no aísla causalmente el coste de cada componente. El pico por solicitud se añadió como análisis descriptivo tras la ejecución; no se presenta como métrica principal preregistrada.

Las dos condiciones tenían cero destinos wiki inexistentes según el diagnóstico, cuyo comprobador no certifica por sí solo desambiguación semántica. B tenía 34 notas con índices consistentes y ocho excepciones de conservación. No se observó una mejora de comprensión en estas respuestas ni se demostró ahorro o mínimo suficiente. Todas las copias conservaron sus hashes; las fuentes ficticias no tenían flujos NTFS alternativos.

Plan, prompts, claves, invocaciones, trazas y análisis reproducible permanecen en el expediente local privado del ensayo. No se publican copias ni eventos que puedan contener metadatos de cuenta. El registro permite repetir cálculos; las sesiones de un servicio cambiante no son deterministas. La metodología de contrastar respuestas, trazas y estado se apoya en [evaluación de agentes de Anthropic](https://www.anthropic.com/research/demystifying-evals-for-ai-agents); las decisiones y resultados concretos de este documento pertenecen a Tune-up.

Para continuar el diagnóstico entre distintas IA, usar [Coordinación del diagnóstico](seguimiento/LEER-PRIMERO.md): observaciones fechadas, fichas P01–P10 y registro de intentos. Documentar una causa no equivale a tener implementada y validada su solución.
