> [!info]- Índice de esta nota (líneas)
> - Líneas 1–8: Este índice
> - Líneas 10–13: Coordinación del diagnóstico de eficiencia
> - Líneas 14–21: Retomar con poco contexto
> - Líneas 22–29: Fuente vigente del seguimiento
> - Líneas 30–35: Orden recomendado
> - Líneas 36–45: Evidencia para avanzar y cerrar
> - Líneas 46–48: Dónde está la evidencia privada

# Coordinación del diagnóstico de eficiencia

Estado al 30/10/2026: diez problemas registrados; P01 mitigado localmente, con adopción por agente pendiente. P02 tiene análisis offline y diseño controlado preparados; no se iniciaron nuevas sesiones de Claude Code. P08/P09 y un presupuesto nuevo preceden a las comparaciones de comprensión y ahorro. Este directorio coordina el desarrollo y la investigación del kit; no añade requisitos a quien quiere organizar su bóveda.

## Retomar con poco contexto

1. Leer [observaciones](OBSERVACIONES-2026-10-29.md) para conocer los resultados y sus límites.
2. Consultar la tabla de [problemas](PROBLEMAS.md) y leer solo la ficha que corresponda, usando su índice de líneas.
3. Leer las entradas recientes de [registro](REGISTRO.md) relacionadas con ese ID. Verificar también cambios locales y commits nuevos; no sobrescribir trabajo ajeno.
4. Anotar responsable, fecha y alcance antes de editar. Si otra IA ya tomó el problema, coordinar el relevo o trabajar en una parte separada y registrarlo.
5. Dejar evidencia, resultado y siguiente acción al terminar. Mantener el problema abierto mientras falte una verificación obligatoria.

## Fuente vigente del seguimiento

La nota compartida de Obsidian es la entrada acordada con Albert para responsables y relevos. PROBLEMAS.md refleja el estado técnico, responsable y próxima acción; al retomar, contrastar ambos y registrar diferencias antes de editar. REGISTRO.md conserva los intentos y relevos en orden; se añaden entradas, sin borrar las anteriores. OBSERVACIONES-2026-10-29.md es una instantánea histórica: las correcciones posteriores se documentan en el registro, sin reescribir resultados para mejorar su apariencia.

La planilla del 29/10 es otra instantánea del diagnóstico. No se sincroniza automáticamente con estos archivos. Actualizarla cuando se solicite o se entregue una nueva versión, indicando su fecha; ante diferencias de estado posteriores, consultar estos Markdown y el historial de Git.

Un responsable declarado no equivale a un bloqueo técnico. Releer la ficha y el estado de Git inmediatamente antes de guardar. Si hay ediciones concurrentes, preservar ambos trabajos y resolver el conflicto; no dar por libre una tarea por el mero paso del tiempo. Este procedimiento no inicia agentes, no envía mensajes y no ejecuta modelos automáticamente.

## Orden recomendado

P01 tiene una mitigación local validada; su adopción por agente queda pendiente. P02 ya separó descriptivamente la lectura progresiva del reintento P01; su comparación controlada espera P08 (rúbrica) y P09 (prerregistro y presupuesto). P04 puede prepararse por separado; cualquier trabajo simultáneo debe respetar responsables y archivos separados. Mantener P03, P05, P06 y P10 visibles.

El diagnóstico disponible permite preparar estas tareas, no afirmar que las soluciones ya funcionan. No interpretar este registro como autorización para consumir nuevas cuotas o cambiar la bóveda original. Usar las autorizaciones vigentes; definir el alcance de una nueva campaña antes de iniciarla y no repetir aprobaciones que ya cubran el mismo trabajo.

## Evidencia para avanzar y cerrar

- Separar hecho observado, hipótesis causal y solución propuesta. Conservar alternativas y resultados negativos.
- Guardar una reproducción con entradas, versión, parámetros, salida y localizador verificable. Las referencias F01–F08 de las observaciones se resuelven en el anexo local externo.
- Para comparar soluciones, congelar tarea, rúbrica y configuración antes de ejecutar. Cambiar un componente por condición y registrar todos los intentos y consumos.
- Enlazar diff y commit de la implementación, prueba de comprensión y comprobaciones de conservación. Actualizar instrucciones y documentación afectadas en el mismo alcance.
- Cerrar solo cuando se cumpla el criterio de aceptación de la ficha. Si una hipótesis se descarta, registrar por qué; eso no implica que el problema general esté resuelto.

La entrada acumulada, el pico por solicitud, el tiempo y la comprensión se informan por separado. No convertir caracteres en tokens reales ni prometer el ahorro de llamadas eliminadas sin medir el nuevo historial. Los índices, enlaces y fuentes se conservan según las reglas aprobadas; las pruebas usan carpetas nuevas bajo I:/Obsidian Tune Up.

## Dónde está la evidencia privada

El anexo local está en I:/Obsidian Tune Up/coordinacion-ia-2026-10-29-01/FUENTES-LOCALES.md. Contiene rutas y hashes de los expedientes, incluida la planilla. No subirlo junto con trazas o copias a GitHub. Una IA sin acceso a ese anexo puede revisar el método y preparar una prueba, pero debe declarar que no contrastó los eventos originales.
