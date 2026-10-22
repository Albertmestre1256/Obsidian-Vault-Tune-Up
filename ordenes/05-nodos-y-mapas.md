# Fase 5: nodos, fichas y mapa

**Objetivo:** que cada proyecto o colección tenga índice, ficha (si es un proyecto) y entrada en el mapa, usando solo lo que la bóveda ya dice.

**Requisito:** fase 4 verificada.

## Regla central

**Solo se usa lo que está escrito en la bóveda.** Si un dato no aparece en las notas, queda «pendiente de confirmar» y se le pregunta a la persona. Nunca se inventan estado, fechas, plazos, responsables ni propósitos.

## Por cada nodo

### 1. Índice del nodo
- Si no existe, se crea desde `plantillas/indice-nodo.md`, con propósito, estado con fecha, notas del nodo y próximos pasos, todo con su fuente.
- Si existe, no se reemplaza: se agregan al final solo las secciones que falten.

### 2. Ficha (solo proyectos)
- Va en `00_CORE/cells/<id>.md`, desde `plantillas/ficha.md`. El `id` va sin tildes y con guiones.
- Campos sin dato: vacíos o «pendiente de confirmar».
- Una colección independiente (por ejemplo, apuntes de un tema) no necesita ficha.

### 3. Mapa
- Una fila por nodo en la tabla del mapa: nodo, de qué trata, índice y ficha.
- El resumen describe el propósito, no el estado. El estado vive en el índice y la ficha.
- Las filas existentes no se reescriben; solo se agregan las que faltan.

### 4. Enlaces
- Padre ↔ hijo: cada subnodo enlaza a su nodo y viceversa.
- Nodo ↔ nota: cada nota del nodo es alcanzable desde su índice.
- Cada índice enlaza la entrada y el mapa.
- Enlaces entre temas solo si el contenido lo justifica, anotando el motivo.

## No hacer
- Crear un proyecto que la persona no acordó.
- Inferir un propósito a partir del nombre de una carpeta.
- Copiar el estado al mapa: queda en un solo lugar.

## Verificación de la fase
- Cada nodo del plan tiene índice, ficha (o «sin ficha») y fila en el mapa.
- Cada índice enlaza la entrada y el mapa.
- No hay datos inventados: cada campo tiene fuente o figura como pendiente.
