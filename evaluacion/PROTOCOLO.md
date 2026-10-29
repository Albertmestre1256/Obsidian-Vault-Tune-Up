> [!info]- Índice de esta nota (líneas)
> - Líneas 1–17: Este índice
> - Líneas 19–24: Medir la eficiencia de Obsidian Vault Tune-up
> - Líneas 25–32: Pregunta y alcance
> - Líneas 33–50: Comparaciones que permiten atribuir efectos
> - Líneas 51–60: Unidad experimental y entornos
> - Líneas 61–70: Tareas y respuestas esperadas
> - Líneas 71–86: Rúbrica de calidad
> - Líneas 87–107: Métricas de recursos
> - Líneas 108–119: Coste de preparación y mantenimiento
> - Líneas 120–129: Ejecución reproducible
> - Líneas 130–139: Análisis e incertidumbre
> - Líneas 140–152: Regla de decisión y resultados incompletos
> - Líneas 153–158: Evidencia mínima para auditar
> - Líneas 159–172: Instrumentación sin interfaz visual
> - Líneas 173–184: Fundamento y fuentes
> - Líneas 185–189: Estado de las afirmaciones actuales

# Medir la eficiencia de Obsidian Vault Tune-up

Versión metodológica 1.0, 24/10/2026. Propuesta de evaluación, no resultado experimental. La IA prepara y ejecuta los archivos; la persona no necesita programar. Las pruebas usan archivos y registros, sin controlar visualmente Obsidian.

Este protocolo evalúa una versión del kit como investigación independiente. No exige repetir el piloto completo en cada entrega a una persona. La entrega individual conserva sus comprobaciones habituales y declara lo que efectivamente pudo medir.

## Pregunta y alcance

¿La bóveda preparada con el kit permite resolver las mismas tareas con menos recursos, manteniendo respuestas correctas, evidencia comprobable y contenido conservado? Medir también cuánto cuesta organizarla y mantenerla. Una reducción de conexiones o de caracteres por sí sola no responde esta pregunta.

Separar tres resultados: conservación de la entrega; calidad de lectura y escritura; recursos consumidos. No combinarlos en una puntuación opaca. Un fallo de conservación invalida la entrega aunque sus consultas sean baratas.

Para la definición de eficiencia acordada el 29/10/2026 —comprender contexto y conformación de un nodo con la menor entrada suficiente— ver [Eficiencia de nodos](EFICIENCIA-NODOS.md). Distingue consumo observado, pico de contexto, búsqueda del mínimo entre presupuestos, tiempo y coherencia, e incluye el primer ensayo exploratorio.

## Comparaciones que permiten atribuir efectos

| Estudio | Condiciones | Qué permite concluir |
|---|---|---|
| Principal | A: instantánea anterior; B: copia producida por una versión fija del kit | Efecto del conjunto de cambios, en las tareas y entorno probados |
| Referencias | R0: sin referencias cruzadas; R1: rutas textuales; R2: los mismos destinos como wikilinks | R1−R0: aporte de referencias; R2−R1: aporte de sintaxis activa |
| Índices, opcional | B con índice de líneas; B equivalente sin ese bloque | Aporte y coste de mantener los índices |

En referencias conservar hechos, títulos, rutas de archivos, descripciones y orden. Solo cambia la presencia de la referencia o su sintaxis. R0 conserva la descripción, eliminando únicamente la referencia. R2−R1 incluye la diferencia de longitud de la sintaxis; no es una prueba de estética. Si se prueban enlaces Markdown, añadir una condición propia, no mezclarlos con wikilinks.

El estudio principal admite instrucciones, organización y redundancia diferentes: son parte del tratamiento. Dar a A sus mecanismos de navegación existentes y permitir búsqueda selectiva. No obligarla a leer todo ni perjudicarla retirando sus índices. Usar instrucciones comunes neutrales; las instrucciones propias del kit se contabilizan como parte de B.

El principal estima el efecto de la copia B concreta. Para estudiar la fiabilidad del proceso del kit, repetir además la organización desde la misma A en carpetas y sesiones nuevas, con entrevista y reglas guionadas; registrar variaciones de agrupación, conservación, coste y calidad. Tres organizaciones independientes pueden servir como piloto exploratorio, sin acreditar una tasa poblacional de éxito. Las consultas sobre una misma salida comparten esa salida y no son réplicas independientes del proceso de organización.

Si la pregunta es si conviene usar el kit frente a pedirle lo mismo a una IA sin kit, añadir un comparador propio: misma bóveda inicial, requisitos, acceso, entrevista y presupuesto, sin las instrucciones de Tune-up. Comparar sus entregas y costes de principio a fin. A contra B por sí solo no responde esa comparación.

No atribuir al enlace el resultado de A contra B. Un ensayo de referencias tampoco acredita el kit completo. Empezar por el principal; añadir una sola comparación de componentes si hace falta explicar el mecanismo.

## Unidad experimental y entornos

Una unidad pareada es la misma tarea, en la misma instantánea y configuración de modelo/herramientas, probada en las dos condiciones. Cada intento comienza en una sesión nueva; las repeticiones de una tarea no cuentan como tareas independientes.

Registrar proveedor, identificador exacto del modelo y versión si se expone; cliente y versión; instrucciones; herramientas; permisos; parámetros disponibles; límites de tiempo y salida; memoria, hooks, plugins y configuración relevante. Registrar también lo que el producto no permite fijar. Congelar el commit del kit, instantáneas, preguntas y criterios antes de generar respuestas.

GPT y Claude nombran familias de modelos; Codex, Claude Code y OpenCode son entornos. En OpenCode hay que especificar también proveedor/modelo. Estimar el efecto A−B dentro de cada entorno. No presentar una diferencia entre clientes como efecto causal del kit ni comparar directamente sus cantidades de tokens como unidades equivalentes.

Separar archivos locales, RAG y carga completa en el contexto. En RAG mantener configuración de fragmentación, recuperación y presupuesto constantes, reconstruyendo un índice independiente por condición y esperando su disponibilidad. Si un chat web oculta recuperación, versión o uso, declarar esa limitación: sirve para calidad observable, no para acreditar un porcentaje de tokens ahorrados.

## Tareas y respuestas esperadas

Preparar las preguntas antes de organizar la copia. Deben representar usos reales, incluyendo temas difíciles, notas largas, versiones contradictorias, ambigüedad y ausencia de información. Un piloto propuesto contiene 16 consultas: cuatro de dato puntual, cuatro que combinan notas, cuatro de vigencia y cuatro de abstención; añadir cuatro ediciones como estudio separado. Es una elección inicial, no un tamaño con potencia estadística demostrada.

Cada tarea lleva: pregunta idéntica entre condiciones; hechos obligatorios; hechos prohibidos o desactualizados; conjuntos alternativos de evidencia válidos; caso de abstención; comprobaciones de estado para ediciones. La referencia a un archivo no prueba que fue leído. Contrastar afirmación, pasaje y traza de acceso cuando esté disponible.

Las respuestas esperadas se guardan fuera del alcance de la IA evaluada. La IA no recibe claves, resultados previos, otra condición ni registro de optimización que revele respuestas. Todas las notas necesarias, incluidas versiones archivadas conservadas, siguen disponibles. No esconder casos difíciles ni archivos después de observar fallos.

Una bóveda ficticia pública permite repetir el procedimiento. Una copia privada de Proyecto 2 permite estudiar utilidad personal; sus datos no se publican. Para generalizar a otras personas hacen falta bóvedas independientes y casos reservados que no se hayan usado para ajustar el kit. El piloto y los ejemplos publicados sirven para desarrollo; no se reutilizan como confirmación independiente.

## Rúbrica de calidad

Evaluar primero sin mostrar al evaluador condición ni consumo, usando códigos aleatorios y neutralizando en la presentación las rutas que revelen la condición. Conservar aparte las respuestas y rutas originales para auditar. Cuando el cegamiento sea incompleto, declararlo.

| Componente | Criterio verificable |
|---|---|
| Exactitud | Todos los hechos exigidos correctos; ninguno inventado o contradicho por evidencia vigente |
| Cobertura | Hechos obligatorios presentes / hechos obligatorios de la tarea |
| Evidencia | Cada afirmación exigida respaldada por un pasaje válido, realmente accesible |
| Abstención | Reconoce que el dato no está; no rellena con conocimiento externo ni suposiciones |
| Escritura | Estado final pedido, índices existentes actualizados, enlaces necesarios válidos y ningún cambio ajeno |

Éxito estricto de consulta = exactitud, cobertura completa y evidencia correctas; en tareas negativas, abstención correcta. Una respuesta plausible o una cita con destino válido no bastan. Éxito de escritura se decide sobre el estado final y diff, además de la respuesta del agente. Guardar también las puntuaciones desagregadas para diagnosticar fallos.

Usar comparación exacta para campos cerrados y revisión de hechos/pasajes para síntesis. Revisar manualmente los casos ambiguos y una muestra aleatoria predefinida de aciertos. Si se usa un juez IA, fijar su configuración, repetir con orden invertido, contrastarlo con revisión humana y contabilizar su coste como evaluación. No dejar que una IA certifique por sí sola su propia mejora. En un estudio publicable, usar dos revisores y registrar desacuerdos y su resolución.

## Métricas de recursos

Métricas principales conjuntas: tasa de éxito estricto y tokens de entrada acumulados por intento. Mostrar salida, coste monetario y tiempo por separado. Registrar todos los intentos, incluidos errores, abandonos, agotamiento del presupuesto y reintentos de la política fijada.

| Medida | Definición |
|---|---|
| Entrada total | Suma de entrada de cada llamada del intento, incluidas instrucciones, historial, índices y resultados de herramientas |
| Salida total | Suma de salida de cada llamada; conservar cómo se informa el razonamiento |
| Tokens totales | Entrada total + salida total, solo tras normalizar campos sin solapamientos |
| Coste por éxito | Coste de todos los intentos / número de éxitos estrictos; indefinido si no hay éxitos |
| Lectura observada | Llamadas, archivos únicos, rangos y caracteres devueltos, incluidos resultados de búsqueda e índices |
| Recuperación | Hechos requeridos recuperados / requeridos; caracteres de evidencia relevante / caracteres documentales devueltos |
| Tiempo | Duración del intento, mediana y percentil 95; registrar arranque, esperas, reintentos y límites |
| Trabajo humano | Tiempo activo, decisiones requeridas y correcciones, separado de esperas de red/modelo |

Una lectura repetida cuenta otra vez como coste; además se informa la fracción de texto repetido. Las métricas de recuperación necesitan pasajes relevantes anotados; son diagnósticas, pues leer una regla puede ser necesario sin contener la respuesta. Si no se exponen los pasajes recuperados, usar N/D en lugar de inferirlos de la respuesta.

Preservar uso bruto del proveedor y documentar su normalización. Caché leída/escrita y razonamiento pueden ser subconjuntos de otros campos: no sumarlos dos veces. No sumar a la vez acumulados de sesión y consumos por llamada. Identificar llamadas y reintentos para evitar duplicados. Medir por intento, no con un contador global mezclado con otros proyectos.

Sesión nueva no garantiza caché vacía. Registrar caché y orden; usar bloques balanceados. Separar ensayos de arranque y de uso repetido. Si el proveedor no permite eliminar caché o no informa consumo, declarar la incertidumbre. Una estimación con tokenizador local se etiqueta como tal, con nombre y versión; caracteres y caracteres/4 nunca sustituyen tokens reales ni facturación. Una suscripción no convierte una estimación de dólares en un cargo marginal observado.

## Coste de preparación y mantenimiento

La conservación incluye originales recuperables de todas las transformaciones y una revisión semántica de las consolidaciones contra sus fuentes. Inventariar antes hechos, matices, atribuciones y versiones críticos; comprobarlos después. Un inventario finito o una muestra no certifican automáticamente todos los matices: declarar cobertura y excepciones.

Guardar por separado el coste del diagnóstico, entrevista, organización, generación de índices y validación. Distinguir coste operativo del kit de coste extraordinario de investigarlo/evaluarlo.

Para N consultas de una mezcla de tareas fijada: coste con kit = preparación + N × coste medio posterior + mantenimiento previsto. Sin kit = preparación propia de la línea base + N × coste medio anterior + mantenimiento propio. El punto de equilibrio usa la diferencia de costes fijos dividida por el ahorro medio por consulta, si este es positivo. Usar la misma unidad y tarifas/fecha; publicar supuestos e incertidumbre. No sumar tiempo humano y dinero sin una valoración explícita.

Tras cada edición de prueba, comprobar exactitud de rangos, descripciones de hasta diez palabras, significado de las descripciones y conservación de texto no autorizado. Restaurar una copia nueva por intento; la edición anterior no debe facilitar la siguiente. Un índice correcto antes de editar no demuestra que sea barato mantenerlo.

Para comprobar que la experiencia es amigable, hacer un estudio separado con personas sin conocimientos técnicos: completar la tarea conversando con la IA, sin comandos o código exigidos; registrar finalización, ayuda requerida, tiempo activo, correcciones y comprensión de las decisiones. Comparar orden balanceado con tareas/bóvedas equivalentes para reducir aprendizaje. Contar menos aprobaciones no es una mejora si se omitió consentimiento necesario. Sin este estudio, solo puede afirmarse que el flujo fue diseñado para ser conversacional.

## Ejecución reproducible

1. Crear una carpeta nueva de experimento, fuera del original y de la copia entregable. Guardar protocolo, preregistro y SHA-256 de entradas. Incluir adjuntos y flujos NTFS cuando existan. La ejecución con modelos espera a tener definidos entorno y presupuesto.
2. Preparar una copia B con el kit fijado, reglas y agrupaciones predefinidas del escenario. Conservar A, respaldo, mapa de movimientos y originales recuperables. Verificar que la organización no haya adelantado las respuestas esperadas en nuevos resúmenes de evaluación.
3. Separar el estudio de consultas del de escritura. Para el piloto: 16 tareas × 2 condiciones × 3 repeticiones = 96 sesiones de consulta por entorno; cuatro ediciones equivalentes agregan 24 sesiones. Una sesión puede consumir varias llamadas. Hacer primero dos tareas de calibración excluidas del conjunto medido.
4. Balancear AB/BA por tarea y repetición, con semilla y calendario guardados antes de ejecutar. Alternar tareas para reducir efectos de horario. En tres condiciones usar las seis permutaciones balanceadas; no ejecutar siempre la misma condición primero.
5. Ejecutar sesiones aisladas, herramientas equivalentes y límites iguales. Memoria, instrucciones heredadas y conexiones ajenas se aíslan; las instrucciones pertinentes a cada condición se cargan y cuentan. No ejecutar scripts o plugins de la bóveda. No abrir Obsidian ni enviar material privado a servicios como parte del protocolo público.
6. Guardar respuesta, traza disponible, uso bruto, duración, errores, configuración y estado final. Aplicar la rúbrica con el consumo oculto. Conservar todos los fallos; un fallo técnico de infraestructura se etiqueta y cualquier repetición queda vinculada, sin borrar el primer intento.
7. Contrastar conservación y cambios autorizados; calcular resultados pareados. Congelar un paquete con manifiesto final, instrucciones de repetición, versión del análisis y limitaciones. Nunca sobrescribir un ensayo anterior.

## Análisis e incertidumbre

Para cada tarea, promediar repeticiones y calcular B−A de calidad, entrada, salida y tiempo. Mostrar resultados por categoría y entorno, además del agregado con pesos fijados previamente. Mostrar también dispersión entre repeticiones y tabla de fallos; no seleccionar únicamente intentos correctos.

Ahorro de entrada = 1 − suma(entrada B) / suma(entrada A), usando los mismos intentos planeados y cobertura de medición completa. Informar coste/tokens por éxito como medida complementaria: nunca ocultar una caída de calidad detrás de esa razón. Si falta consumo de un intento, no calcular un ahorro global con los restantes como si representaran a todos.

En el piloto se pueden informar intervalos bootstrap pareados del 95 %, remuestreando tareas con todas sus repeticiones, y semilla guardada. Si hay varias bóvedas, remuestrear bóvedas y luego tareas, respetando sus dependencias. Con pocas tareas/bóvedas o resultados constantes, los intervalos pueden ser engañosos; declararlos exploratorios. Tres repeticiones de 16 tareas no son 48 tareas independientes. Ninguna semilla garantiza idénticas respuestas de un servicio cambiante.

Para una afirmación confirmatoria, reservar datos nuevos y preregistrar la diferencia mínima útil, margen aceptable de calidad, tamaño muestral calculado con el piloto, regla de decisión, métrica principal y corrección por comparaciones múltiples. La elección requiere justificar la tolerancia de errores; no adoptar un porcentaje universal ni elegir el margen después de ver resultados. Informar intervalos y magnitud, no solo significación estadística.

## Regla de decisión y resultados incompletos

| Resultado | Conclusión admisible |
|---|---|
| Pérdida o cambio no autorizado | Entrega rechazada; no hay éxito del kit |
| Menos recursos y peor calidad | Intercambio entre coste y calidad; no mejora acreditada |
| Misma calidad observada y menos recursos en piloto | Señal favorable en esas tareas; falta confirmación independiente |
| Evidencia confirmatoria supera criterios predefinidos | Mejora acreditada dentro del alcance medido |
| Menos caracteres o enlaces sin uso medido | Cambio estructural; ahorro de tokens no demostrado |
| Uso parcial u oculto | Calidad y recursos observables; ahorro global de tokens N/D |

La aceptación incluye conservación, agrupaciones aprobadas, ausencia de modificaciones ajenas, navegación funcional y excepciones declaradas. Un porcentaje de ahorro requiere además calidad suficiente según el criterio fijado y cobertura de medición explícita. Distinguir calidad de la salida organizada de calidad de las consultas posteriores.

## Evidencia mínima para auditar

Conservar: protocolo y preregistro fechados; commit del kit; instantáneas/manifiestos; reglas y aprobación del escenario; mapa de transformaciones; preguntas y claves separadas; calendario; configuración por entorno; trazas originales disponibles; uso bruto y adaptador de normalización; calificaciones justificadas; análisis reproducible; informe de exclusiones, fallos y datos faltantes. Calcular SHA-256 no prueba validez de contenido: permite identificar qué archivos se evaluaron.

El informe distingue tres niveles: reproducción de cálculos sobre las mismas trazas; repetición del procedimiento con nuevas sesiones; replicación en modelos, tareas o bóvedas independientes. El primer nivel puede ser exacto; los otros pueden variar por el servicio. No confundir reproducibilidad documental con resultados de modelo deterministas.

## Instrumentación sin interfaz visual

- OpenAI: recoger uso por llamada/sesión según la interfaz concreta; verificar campos y evitar sumar sus subconjuntos. Si se usa Codex, registrar su versión y eventos realmente expuestos; el uso de la API no demuestra que una exportación de Codex contenga lo mismo.
- Claude Code: admite ejecución programática y JSON/eventos. Conservar versión, salida y uso de cada intento nuevo. Sus estimaciones de coste no equivalen necesariamente a factura; no sumar acumulados de conversaciones reanudadas.
- OpenCode: fijar versión mayor y proveedor/modelo; comprobar ayuda de la versión instalada. Guardar eventos y exportación de la sesión. La documentación de distintas versiones difiere; no dar por expuestos campos de tokens que no estén en la exportación real.
- ChatGPT/Claude web: usar corpus ficticio, proyectos separados y configuración registrada, sin automatizar la computadora. Si no existe una exportación suficiente, dejar el estudio de tokens para una interfaz instrumentable y registrar solo calidad observable en web.
- Lectura sin shell: si el cliente bloquea comandos de lectura, no se habilitan por fuera de la política. La vía es `evaluacion/servidor_lectura_boveda.py`: un servidor MCP de solo lectura confinado a la copia del intento, sin herramientas de escritura. Registrar en el intento qué herramienta se usó (llamadas MCP o shell) y comprobar que las llamadas de lectura aparecen en la traza; una sesión sin lectura queda como fallo de acceso, no como medición de calidad.
- Fijar también versión/hash del lector y sus límites, formato y parámetros. El lector ofrece rangos para notas grandes y continuación con `offset` en búsqueda/listado. Un resultado truncado, un error de UTF-8 o de acceso no acreditan ausencia del dato. Mantener estable la copia durante el intento y comprobar su manifiesto al terminar; el servidor no sustituye un sandbox del proceso ni protege frente a modificaciones concurrentes de enlaces del sistema de archivos.
- Verificar el contrato del buscador con controles positivos y negativos. [P01](P01-GREP.md) reproduce un cero falso en Grep de Claude Code 2.1.304 con un espacio dentro de glob; se validaron filtros alternativos sin invocar modelos. El resultado local no demuestra ahorro ni que un agente siga todavía la nueva instrucción del paso 2.
- Verificar la política de herramientas antes del piloto: una llamada MCP intentada o una salida de proceso cero no prueban acceso. Exigir una llamada completada sin error y comprobar su contenido. El lector 1.2 declara `readOnlyHint`; una configuración acotada puede listar solo sus tres herramientas y usar `default_tools_approval_mode = "writes"`, manteniendo denegada la ejecución o escritura no aprobadas. Las anotaciones no sustituyen los controles de rutas. [Política MCP de Codex](https://learn.chatgpt.com/docs/extend/mcp).
- Modelo y servicio: la sesión se acepta solo si el evento de inicio reporta el identificador de modelo solicitado. Si reporta un alias, un nombre distinto o ninguno, la sesión se marca inválida y no se etiqueta con el nombre pedido. Un destino local que no escucha (conexión rechazada) se registra como fallo técnico de infraestructura, con su error, antes de cualquier reintento.

Estas capacidades documentadas no implican que se hayan ejecutado modelos en esta investigación. El protocolo no instala clientes, no incorpora dependencias y no requiere contratar una plataforma de evaluación.

## Fundamento y fuentes

Consultadas el 24/10/2026. Las decisiones concretas de diseño, tamaños del piloto y regla de aceptación anteriores son propuestas para Tune-up; no estándares impuestos por estas fuentes.

- [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): respalda definir objetivo, datos, métricas y comparación, y contrastar la evaluación automática con juicio humano.
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents): distingue tareas, intentos, trazas y estado final; sustenta revisar resultados observables y repetir intentos.
- [Ragas, Es y otros](https://arxiv.org/abs/2309.15217): distingue recuperación de contexto y uso fiel de este en la respuesta. Adoptamos esa separación; no dependemos de sus jueces automáticos ni de su biblioteca.
- [Dror y otros, ACL 2018](https://aclanthology.org/P18-1128/): fundamenta elegir las pruebas estadísticas según diseño, tarea y medida. El bootstrap del piloto aquí es una propuesta exploratoria, no una garantía de validez con pocas muestras.
- [OpenAI: Observability and usage](https://developers.openai.com/api/docs/guides/agents-api/observability): documenta categorías de uso solapadas, ausencia de datos y distinción entre uso observado y factura.
- [Claude Code: ejecución programática](https://code.claude.com/docs/en/headless) y [costes](https://code.claude.com/docs/en/costs): documentan JSON/eventos y estimaciones de consumo/coste.
- [OpenCode: CLI](https://opencode.ai/docs/cli/): documenta ejecución por comandos y exportación de sesiones. Adaptar comandos a la versión instalada.

## Estado de las afirmaciones actuales

Las pruebas anteriores de Tune-up aportan conservación y medidas estructurales. El 17 % menos de caracteres en un recorrido y el 7,68 % menos de conexiones del subgrafo no prueban ahorro de tokens ni mejor respuesta. En las 30 notas de navegación del ensayo de enlaces, el texto aumentó un 0,9 %. La revisión nativa posterior comprobó recorridos, pero quedó incompleta y no es un ensayo de eficiencia.

La próxima evidencia necesaria es el estudio principal con sesiones nuevas, respuestas esperadas fijadas y uso instrumentado. Este documento habilita diseñarlo y auditarlo; no adelanta su resultado.
