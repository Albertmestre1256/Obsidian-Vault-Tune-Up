# Fase 4: estructura mínima y movimientos

**Objetivo:** dejar la bóveda con la estructura del kit sin reescribir contenido.

**Requisito:** fases 1 a 3 completas, plan aprobado, respaldo verificado y una sola sesión escribiendo (regla 15).

## Estructura de destino

Es la misma que usa [Obsidian Genesis](https://github.com/Albertmestre1256/obsidian-genesis), así una bóveda adaptada y una nueva se manejan igual. Si la bóveda ya tiene una pieza equivalente con otro nombre, **se conserva la suya** y se anota la equivalencia en el mapa.

| Pieza | Nombre por defecto | Plantilla |
|---|---|---|
| Entrada (lo primero que se lee) | `LEER_PRIMERO.md` | `plantillas/LEER_PRIMERO.md` |
| Mapa general | `INDICE.md` | `plantillas/INDICE.md` |
| Reglas | `00_CORE/atoms/00_vault-rules.md` | `plantillas/00_vault-rules.md` |
| Fichas de proyecto | `00_CORE/cells/<id>.md` | `plantillas/ficha.md` |
| Registro de cambios | `00_CORE/logs/registro-cambios.md` | `plantillas/registro-cambios.md` |
| Índice de cada nodo | `<nodo>/00 - Índice - <nodo>.md` | `plantillas/indice-nodo.md` |
| Material de un proyecto (opcional) | `01_FUENTES/` (originales), `02_SINTESIS/` (trabajo), `03_ENTREGABLES/` (finales) | — |
| Lo que sobra | `_archivo/` | — |

## Pasos

Cada paso es un bloque del plan. Después de cada bloque: verificar, registrar y seguir.

### 1. Carpetas faltantes
Se crean solo las que hacen falta. Nunca carpetas de nodo vacías.

### 2. Reglas
- Si faltan: se copia la plantilla y se completan sus datos.
- Si existen: no se reemplazan. Las reglas del kit que falten se agregan, y solo con aprobación.

### 3. Entrada y mapa
- Si faltan: se crean desde las plantillas y se completan con los nodos reales, enlazando cada índice.
- Si existen: no se reemplazan. Se agregan al final solo las secciones o filas que falten.

### 4. Registro
Si no hay, se crea desde la plantilla. Desde este bloque, cada cambio deja su fila (fase 0).

### 5. Movimientos (uno por vez)
1. Confirmar que el origen existe y el destino no.
2. Mover el archivo, con Obsidian o con la herramienta de archivos.
3. **Corregir los enlaces.** Mover con herramientas de archivos (o con un conector) **no actualiza los `[[...]]`**, como sí lo hace Obsidian. Hay que buscar los enlaces que apuntaban a la nota movida y corregirlos dentro del mismo bloque.
4. Registrar `origen → destino`, fecha e ID del plan.

Si un movimiento falla o el destino existe, se para el bloque y se pide una decisión.

### 6. Sin eliminaciones
El kit no elimina nada. Lo que sobra va a `_archivo/<AAAA-MM-DD>-tuneup/`.

## Verificación de la fase
- Cada origen del plan está en su destino o en `_archivo/`, con su fila en el registro.
- La fase no dejó enlaces rotos nuevos (se compara con el diagnóstico).
- Las reglas existentes no cambiaron, salvo lo aprobado.
