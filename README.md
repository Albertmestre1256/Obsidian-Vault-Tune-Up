> **Crédito principal a [davidkimai](https://github.com/davidkimai):** basado en su trabajo [Context Engineering](https://github.com/davidkimai/Context-Engineering), a través de [Obsidian Genesis](https://github.com/Albertmestre1256/obsidian-genesis).

# Obsidian Vault Tune-up

**Conversá con una IA y recibí una copia de tu bóveda de Obsidian organizada, conectada y más fácil de consultar.**

Vos elegís qué temas deben ir juntos y aprobás las reglas. La IA organiza una copia, conserva el contenido, mejora los enlaces y prepara índices para leer solo lo necesario. Tu bóveda original permanece intacta y vos decidís si reemplazarla.

El kit son instrucciones y plantillas Markdown. No necesitás programar ni ejecutar comandos. Las herramientas de archivos de la IA hacen el trabajo; hay cuatro scripts opcionales para cálculos y comprobaciones exactas. [Genesis](https://github.com/Albertmestre1256/obsidian-genesis) crea bóvedas nuevas; Tune-up adapta bóvedas existentes respetando sus nombres y preferencias.

## Empezar con una IA instalada

Descargá este repositorio fuera de tu bóveda, abrilo con una IA que tenga acceso a archivos y escribile:

> Leé AGENTS.md. Quiero organizar mi bóveda en `<ruta original>` y recibir una copia independiente en `<carpeta nueva>`. Primero preguntame qué temas o notas quiero mantener juntos y proponeme las reglas. No cambies el original.

Recibís una carpeta nueva que podés abrir como otra bóveda en Obsidian. El kit no reemplaza el original.

## Empezar con una IA web

Usá una IA que pueda recibir archivos, modificarlos y devolver ZIP descargables. Adjuntá un ZIP de tu bóveda y los archivos de este kit, y escribile:

> Leé AGENTS.md. Quiero que organices una copia de la bóveda adjunta y me devuelvas un ZIP con el resultado. Primero preguntame qué temas o notas quiero mantener juntos y proponeme las reglas. Conservá todo el contenido.

La IA comprueba primero que puede procesar y entregar los archivos. Si no tiene esas capacidades, no puede completar Tune-up desde ese chat. No necesitás publicar ni sincronizar tu bóveda. Conservá una copia local al preparar el ZIP de entrada: contenido especial de NTFS puede no viajar en un ZIP convencional; la IA debe comprobarlo, no asumirlo.

## Los diez pasos

La IA lee las [reglas de trabajo](ordenes/00-reglas-de-trabajo.md) y solo el paso que está usando.

| Paso | Qué hace la IA |
|---|---|
| 1. [Alcance](ordenes/01-alcance.md) | Confirma el entorno, el idioma y la entrega |
| 2. [Diagnóstico](ordenes/02-diagnostico.md) | Revisa la bóveda sin modificarla y mide el contexto |
| 3. [Preferencias y plan](ordenes/03-preferencias-y-plan.md) | Pregunta qué debe ir junto y acuerda la organización |
| 4. [Reglas](ordenes/04-reglas.md) | Propone reglas y espera su aprobación |
| 5. [Copia independiente](ordenes/05-copia-de-trabajo.md) | Crea y verifica la copia de trabajo |
| 6. [Organización](ordenes/06-organizacion.md) | Agrupa por temática; lo dudoso va a Sin clasificar |
| 7. [Navegación](ordenes/07-navegacion.md) | Incorpora reglas, mapa, entrada e índices de nodos |
| 8. [Compactación](ordenes/08-compactacion.md) | Reduce repeticiones con aprobación y conservación |
| 9. [Índices de líneas](ordenes/09-indices-de-lineas.md) | Añade rangos exactos y descripciones de hasta diez palabras |
| 10. [Validación y entrega](ordenes/10-validacion-y-entrega.md) | Verifica conservación, mide el resultado y entrega carpeta o ZIP |

No necesitás aprender los números ni aprobar cada movimiento por separado: la IA explica un plan concreto, registra tu aprobación y continúa con ese alcance. Las fusiones, modificaciones de reglas existentes y cualquier propuesta de eliminación se consultan explícitamente. Nada se elimina por defecto.

## Qué se conserva

- Todas las notas, adjuntos y versiones. Las preferencias del usuario mandan sobre una clasificación automática.
- Reglas y nombres existentes, salvo cambios propuestos y aprobados.
- Contenido que no se pueda clasificar: va a **Sin clasificar**, en tu idioma, con navegación desde el mapa.
- Originales de las consolidaciones, recuperables dentro de la entrega y fuera del recorrido habitual de la IA. No se confunde compactar con borrar.
- Configuraciones, archivos de terceros y bloques generados: se conservan; no se ejecutan ni alteran por iniciativa del kit.

La IA registra las rutas anteriores y nuevas, las decisiones y las comprobaciones. No copia valores privados a los informes. La programación sirve para verificar el trabajo, no para obligarte a operar una aplicación adicional.

## Cómo se evalúa el resultado

La copia debe conservar la información, respetar las agrupaciones y reglas aprobadas y permitir navegar desde Leer primero → reglas → mapa → nodo → rango de nota. Los rangos incluyen las líneas del propio índice; cada descripción ocupa como máximo diez palabras.

La IA compara antes y después: contexto necesario para una misma consulta, repeticiones retiradas del recorrido activo, enlaces y conservación. Informa si no hubo ahorro. Caracteres / 4 es solo una estimación de tokens; no demuestra ahorro real en todas las tareas. La lectura y escritura deben poder hacerse sin cargar la bóveda completa; después de editar se actualiza el índice correspondiente.

## Herramientas auxiliares

La IA puede usar herramientas equivalentes de su entorno. Estos scripts usan solo Python estándar 3.8+, sin dependencias; los ejecuta la IA, no la persona.

| Herramienta | Uso |
|---|---|
| `herramientas/diagnostico.py` | Inventario y hallazgos sin valores privados |
| `herramientas/respaldo.py` | Copia y manifiesto SHA-256, incluidos flujos NTFS en Windows |
| `herramientas/indice_lineas.py` | Rangos exactos y descripciones breves, sin modificar el cuerpo |
| `herramientas/verificar.py` | Cambios esperados, movimientos declarados, flujos e índices; no sustituye la revisión del contenido consolidado |

Ver [pruebas y límites](PRUEBAS.md). Para desarrollar: `python -B -m unittest discover -s tests -v`.

## Estado

**v0.3 en desarrollo.** El flujo adapta los objetivos acordados: copia independiente, entrevista temática, reglas aprobadas, Sin clasificar, conservación y contexto reducido. Las capacidades de la IA web dependen de su entorno. Las pruebas automáticas y locales no sustituyen una prueba completa con personas, una sesión de contexto limpio ni la revisión visual en Obsidian.

## Licencia

[MIT](LICENSE). Se mantienen los créditos de Context Engineering y Obsidian Genesis.
