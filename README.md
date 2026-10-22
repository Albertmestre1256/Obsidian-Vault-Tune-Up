> **Crédito principal a [davidkimai](https://github.com/davidkimai):** este kit se basa en su trabajo [Context Engineering](https://github.com/davidkimai/Context-Engineering), a través de [Obsidian Genesis](https://github.com/Albertmestre1256/obsidian-genesis).

# Obsidian Vault Tune-up

**Ordená y aligerá una bóveda de Obsidian que ya existe, con ayuda de una IA, sin perder nada.**

Tune-up es una serie de órdenes en markdown, con unos scripts opcionales, para que una IA con acceso a tus archivos reacomode tu bóveda. Al terminar, la bóveda tiene reglas claras, un mapa, un índice por proyecto, un índice de líneas en cada nota y un registro de cambios. Así cualquier IA encuentra lo que necesita leyendo poco: menos tokens, menos confusión y menos errores.

Es el hermano de [Obsidian Genesis](https://github.com/Albertmestre1256/obsidian-genesis): **Genesis crea bóvedas nuevas; Tune-up adapta las que ya tenés** a la misma estructura.

## Cómo se usa

1. **Descargá este repositorio** en una carpeta **fuera** de tu bóveda.
2. **Abrí una IA que pueda leer y escribir archivos** (Claude Code, Codex, OpenCode u otra) en la carpeta del kit, y dale acceso también a tu bóveda.
3. **Escribile:**

   > Leé `AGENTS.md` y hacé el diagnóstico de mi bóveda en `<ruta de tu bóveda>`.

La IA trabaja por fases. Antes de cambiar cualquier cosa te muestra un plan con acciones numeradas, y vos aprobás las que quieras.

## Qué hace y qué no hace

| Hace | No hace |
|---|---|
| Diagnostica la bóveda sin escribir nada | Borrar (lo que sobra va a `_archivo/`) |
| Propone un plan con IDs que vos aprobás | Reescribir el texto de tus notas |
| Respalda y verifica antes del primer cambio | Inventar estados, fechas o propósitos |
| Mueve, indexa y enlaza según lo aprobado | Agregar ni quitar datos privados sin tu permiso |
| Reduce el contexto de arranque (con aprobación) | Tocar `.git`, `.obsidian`, plugins o scripts propios |
| Registra cada cambio y quién lo hizo | Publicar, sincronizar ni subir nada |

## Las fases

La IA lee [las reglas de trabajo](ordenes/00-reglas-de-trabajo.md) y **solo la fase en curso**, para no cargar todo el kit de una vez.

| Fase | Orden | Escribe en la bóveda | Necesita tu aprobación |
|---|---|---|---|
| 0 | [Reglas de trabajo](ordenes/00-reglas-de-trabajo.md) | No | — |
| 1 | [Diagnóstico](ordenes/01-diagnostico.md) | No | No |
| 2 | [Plan con IDs](ordenes/02-plan.md) | No | **Sí** |
| 3 | [Respaldo verificado](ordenes/03-respaldo.md) | No | Incluido en el plan |
| 4 | [Estructura y movimientos](ordenes/04-estructura.md) | Sí | Por ID |
| 5 | [Nodos, fichas y mapa](ordenes/05-nodos-y-mapas.md) | Sí | Por ID |
| 6 | [Índices de líneas](ordenes/06-indices-de-lineas.md) | Sí | Por ID |
| 7 | [Optimización](ordenes/07-optimizacion.md) (opcional) | Sí | **Por cada acción** |
| 8 | [Verificación y cierre](ordenes/08-verificacion.md) | Solo el informe | No |

## Seguridad

- **Nada se borra.** Lo que sobra se archiva con su ruta original anotada.
- **Respaldo primero.** No se escribe nada hasta que hay una copia completa y verificada (en Windows, incluso el contenido oculto en flujos alternativos de NTFS).
- **Aprobación por ID.** Un «sí» general no alcanza; las acciones de riesgo alto se aprueban de a una.
- **Una sola sesión escribiendo.** Si mientras tanto otra IA o persona cambia la bóveda, la verificación lo detecta y la IA para.
- **Tus datos privados no salen de la bóveda:** los informes dicen dónde están, nunca qué dicen.

## Herramientas (opcionales)

Están en `herramientas/` y usan solo Python estándar 3.8+. Ninguna escribe en la bóveda, salvo `indice_lineas.py apply` sobre las notas que le indiques. Se corren con `python -B` para que no dejen `__pycache__`.

| Script | Fase | Qué hace |
|---|---|---|
| `diagnostico.py` | 1 | Inventario, reglas y mapa, nodos, índices de líneas, registro, enlaces rotos, bloques generados, duplicados, peso de contexto y ubicación de datos privados (sin los valores) |
| `respaldo.py` | 3 | Copia, manifiesto SHA-256 (con flujos alternativos en Windows) y comparación |
| `indice_lineas.py` | 6 | Revisa o recalcula los índices de líneas. Conserva las descripciones, la forma del índice, la codificación y los saltos de línea de cada nota |
| `verificar.py` | 8 | Compara con el respaldo: cambios fuera del plan, herramientas, contenido oculto, datos privados e índices; mide el arranque |

Sin Python, cada fase describe cómo hacerlo con las herramientas de archivos de la IA.

Pruebas: `python -B -m unittest discover -s tests`.

## Estado del proyecto

**v0.2, en construcción.** Probado sobre la copia de una bóveda real de unas 300 notas (diagnóstico, plan, respaldo, dos acciones de riesgo bajo y verificación) y con una prueba automática sobre una bóveda desordenada ficticia. Falta:

- probarlo con personas y con bóvedas desordenadas reales;
- una prueba de arranque hecha por una sesión nueva;
- revisión visual en Obsidian;
- versiones del README en otros idiomas.

## Licencia y créditos

[MIT](LICENSE). Basado en [Context Engineering](https://github.com/davidkimai/Context-Engineering) de davidkimai y en [Obsidian Genesis](https://github.com/Albertmestre1256/obsidian-genesis).
