# Fase 6: índices de líneas

**Objetivo:** que cada nota propia empiece con un bloque que diga en qué líneas está cada parte, para que una IA lea solo el rango que necesita.

**Requisito:** fase 5 verificada.

## Formato

Después de las propiedades (si las hay):

```markdown
> [!info]- Índice de esta nota (líneas)
> - Líneas 1–5: Propiedades
> - Líneas 6–10: Este índice
> - Líneas 12–30: <primera sección>
> - Líneas 31–60: <segunda sección>
```

- Los números son líneas del archivo completo, incluido el propio índice.
- Cada sección empieza en un título (`#`, `##`; si la bóveda ya los usa, también `###`).
- Si la nota cambia, el índice se recalcula. Un índice desactualizado es peor que ninguno.
- `[!info]-` se muestra plegado en Obsidian. Si la bóveda ya usa `[!info]` (abierto), se conserva.

## Alcance

**Sí:** las notas `.md` propias de la bóveda.

**No:**
- plantillas;
- `_archivo/`;
- archivos de terceros;
- notas que no son UTF-8;
- excepciones declaradas por la bóveda;
- datos (`.csv`, `.json`, `.yaml`).

## Con Python

1. `python -B herramientas/indice_lineas.py check --boveda <bóveda> [--excluir '<patrón>']` lista cada nota con el índice faltante, desactualizado u omitido. No escribe nada.
2. `python -B herramientas/indice_lineas.py apply <nota1> <nota2> …` trabaja solo con las notas aprobadas en el plan. Conserva las descripciones escritas a mano y la forma del índice existente (títulos hasta `##` o `###`, atribución previa). Respeta la codificación, el BOM y los saltos de línea de cada nota.
3. Volver a correr `check`. Tiene que quedar limpio, salvo las excepciones.
4. Si en el mismo bloque se escribió en el registro, recalcular también su índice.

## Sin Python

Para cada nota:

1. Leerla con números de línea.
2. Ubicar los títulos.
3. Escribir el bloque.
4. Comprobar que cada rango empiece en el título que nombra y termine justo antes del siguiente.

En el registro se anota que el índice se hizo a mano.

## Verificación de la fase
- Cada nota del alcance tiene su bloque y `check` está limpio, o la revisión manual coincide.
- El registro dice cuántas notas se indexaron y con qué método.
