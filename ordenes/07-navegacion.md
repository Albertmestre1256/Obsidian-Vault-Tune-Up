# Paso 7: reglas, mapa y entrada

1. **Verificar las reglas aprobadas** incorporadas en el paso 6 y crear o adaptar índice general y Leer primero. Respetar equivalentes; si faltan, usar plantillas. Traducir nuevos nombres al idioma de la persona y actualizar enlaces y rutas de las plantillas. No duplicar las mismas reglas en tres notas.
2. **Conectar nodos reales.** Cada nodo tiene índice de notas y subnodos; cada nota enlaza su índice; padres e hijos se enlazan entre sí. Las fichas son opcionales, solo si aportan datos vivos sin duplicar estado. No inventar campos. Sin clasificar también tiene índice y entrada en el mapa.
3. **Revisar relaciones.** Añadir conexiones justificadas por contenido, explicadas cuando haga falta. Reparar enlaces afectados y proponer arreglos de enlaces previos con destino inequívoco. No inventar relaciones para evitar Sin clasificar ni editar bloques generados sin permiso.

## Piezas por defecto, si no hay equivalentes

| Pieza | Ruta | Plantilla |
|---|---|---|
| Reglas | `00_CORE/atoms/00_vault-rules.md` | `plantillas/00_vault-rules.md` |
| Mapa | `INDICE.md` | `plantillas/INDICE.md` |
| Entrada | `LEER_PRIMERO.md` | `plantillas/LEER_PRIMERO.md` |
| Índice temático | `<nodo>/00 - Índice - <nodo>.md` | `plantillas/indice-nodo.md` |
| Ficha opcional | `00_CORE/cells/<id>.md` | `plantillas/ficha.md` |
| Registro | `00_CORE/logs/registro-cambios.md` | `plantillas/registro-cambios.md` |

El mapa describe propósito y rutas; cada estado vive en una fuente activa. Leer primero explica: reglas → mapa por rangos → nodo → sección necesaria. Para escribir, consultar esa fuente, modificar lo aprobado, actualizar el índice y registrar. Rutas del original no autorizan a salir de la copia: adaptarlas en las piezas aprobadas y documentar referencias históricas sin ejecutarlas.
