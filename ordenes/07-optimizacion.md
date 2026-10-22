# Fase 7: optimización del contexto (opcional, cada acción aprobada)

**Objetivo:** que una IA que arranca en la bóveda cargue lo mínimo: reglas + entrada + mapa (por rangos) + índice y ficha del nodo de trabajo.

**Requisito:** fases 4 a 6 verificadas y cada acción aprobada por separado.

**Regla:** nada se borra. Lo que se poda va a `_archivo/`.

## Acciones permitidas

| Acción | Cuándo | Aprobación |
|---|---|---|
| Medir el arranque | Siempre | No (es lectura) |
| **Formato sin pérdida:** quitar espacios de alineación en tablas | Si el diagnóstico los encuentra. Se comprueba que cada celda conserve su texto y la nota sus líneas | Por nota |
| Leer por rangos: agregar al mapa el índice de líneas que señala su tabla de nodos | Si el mapa es largo | Por nota |
| Pasar el historial de una ficha o índice pesado a una nota de avance | Si una ficha supera unos 10 000 caracteres | Por nota (riesgo alto) |
| Dividir una nota enorme en subnotas | Si el diagnóstico lo recomienda | Por nota |
| Fusionar duplicados o notas solapadas | Con el contenido de ambas a la vista | Por caso |
| Mandar material obsoleto a `_archivo/` | Solo si la persona lo dice | Por archivo |

## Acciones prohibidas
- Borrar.
- Reescribir texto para acortarlo, aunque quede mejor.
- Tocar datos privados, archivos de terceros, binarios o código.

## Pasos

1. **Medir** el arranque, leyendo todo y leyendo por rangos. Se guarda `medicion-antes.md` en la carpeta de trabajo.
2. **Proponer** cada acción: archivo, qué cambia, cuánto ahorra (caracteres antes y después), qué se pierde y cómo se recupera.
3. **Ejecutar** solo lo aprobado, de a un cambio, con su fila en el registro. Después de cada cambio se verifican enlaces y rangos (fase 6).
4. **Medir de nuevo** igual que en el paso 1 y guardar `medicion-despues.md`.

Conviene empezar por lo que no pierde nada. En una bóveda real de prueba, quitar los espacios de alineación del mapa ahorró el 28 % del archivo sin cambiar una palabra, y el arranque leyendo por rangos bajó de unos 4 860 a unos 3 440 tokens.

## Informe

```markdown
# Optimización — AAAA-MM-DD
**IA:** <nombre> (<herramienta>, <modelo>) · **Plan:** P-0xx a P-0xx
- Arranque completo: <n> → <n> caracteres (≈ <n> → <n> tokens)
- Arranque por rangos: <n> → <n> caracteres
- Cambios: P-0xx <qué> (<ahorro>)
- Movido a `_archivo/`: <ruta> (antes en <ruta>)
- Límite: tokens estimados (caracteres / 4), no medidos con el modelo.
```
