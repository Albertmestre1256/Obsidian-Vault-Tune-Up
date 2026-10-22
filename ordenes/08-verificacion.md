# Fase 8: verificación y cierre

**Objetivo:** comprobar que la bóveda cumple las reglas y que no se perdió nada. Esta fase no escribe en la bóveda, salvo el informe final.

## Con Python

```text
python -B herramientas/verificar.py <bóveda> <respaldo> <trabajo> <trabajo>/esperados.txt [--excluir '<patrón>']
```

`esperados.txt` lleva una ruta por línea: todo lo que el plan aprobado cambia, crea o mueve. El script revisa los puntos 1, 6, 9 y 10 y los flujos alternativos, y mide el arranque. Los archivos que cambian solos en cada sesión (`.obsidian/workspace*.json`, `__pycache__`, el diario de `.obsidian-mcp`) se informan aparte.

## Checklist

Cada punto se marca «ok», «falla» o «no aplica». Con un «falla» no hay cierre.

| # | Comprobación | Cómo |
|---|---|---|
| 1 | Nada perdido ni cambiado fuera del plan | Cada archivo y flujo del manifiesto original sigue igual, o cambió según el plan, o figura en el registro con su ruta nueva. Un cambio fuera del plan puede ser de otra sesión: parar y averiguar |
| 2 | Movimientos registrados | Cada movimiento tiene su fila `origen → destino` |
| 3 | Sin enlaces rotos nuevos | Comparar con el diagnóstico |
| 4 | Piezas básicas | Hay reglas, entrada y mapa (con los nombres del kit o sus equivalentes anotados) |
| 5 | Reglas | Las existentes no cambiaron, salvo lo aprobado |
| 6 | Índices de líneas | `check` limpio, salvo las excepciones anotadas |
| 7 | Nodos completos | Cada nodo tiene índice, ficha (o «sin ficha») y fila en el mapa |
| 8 | Sin datos inventados | Cada campo nuevo tiene fuente o figura como pendiente |
| 9 | Datos privados intactos | Las líneas con datos que marcó el diagnóstico siguen idénticas (pueden cambiar de número). No sirve comparar el hash del archivo: cambia apenas se recalcula el índice |
| 10 | Herramientas intactas | Carpetas ocultas, scripts, plugins, `_archivo/` y bloques generados sin cambios fuera del plan |
| 11 | Registro completo | Cada bloque ejecutado tiene su fila, con autor, aprobación y verificación |
| 12 | Prueba de arranque | Ver abajo |

## Prueba de arranque

Lo ideal es que la haga una sesión nueva, que no armó el plan. Si la hace la misma IA, se anota como límite. La sesión lee solo esto:

1. Las reglas.
2. La entrada.
3. El mapa, solo el rango de su tabla de nodos.
4. El índice y la ficha de un nodo activo.

Con eso tiene que responder, sin leer nada más: ¿qué proyectos hay y cuál está activo?, ¿qué sigue en el proyecto elegido?, ¿dónde se registra un cambio?

Si necesita leer más, la bóveda no quedó bien indexada: se anota qué faltó. También se anota cuántos caracteres leyó, para compararlo con la fase 7.

## Resultado

- **CIERRE VERIFICADO:** todos los puntos «ok» y la prueba de arranque superada.
- **PARCIAL:** algún punto en «falla» o pendiente. Se listan con su motivo y el próximo paso.

## Informe final

Se guarda en la bóveda (donde guarde sus reportes; si no tiene un lugar, en `00_CORE/logs/tuneup-AAAA-MM-DD.md`) y se registra.

```markdown
# Tune-up de <bóveda> — AAAA-MM-DD
**Estado:** CIERRE VERIFICADO / PARCIAL · **IA:** <nombre> (<herramienta>, <modelo>)
**Plan aprobado:** P-001 a P-0xx · **Respaldo:** <ruta>
## Hecho · ## Pendiente · ## Verificación (checklist) · ## Prueba de arranque
```

## Cierre con la persona

1. El estado y lo que quedó pendiente.
2. Dónde está el respaldo y cómo restaurarlo.
3. Que abrir la bóveda en Obsidian y mirarla es una prueba visual aparte, que la IA no puede hacer.
