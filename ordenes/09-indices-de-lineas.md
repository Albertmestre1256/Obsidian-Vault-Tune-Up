# Paso 9: índices exactos y lectura por rangos

1. **Inventariar alcance.** Cada nota Markdown editable, incluidas Sin clasificar, reglas, mapas e informes nuevos, lleva índice al principio, después de propiedades si existen. Respetar atribuciones y excepciones acordadas; listar notas protegidas, de terceros o incompatibles como pendientes/excepciones. No convertir codificaciones sin permiso. Una excepción no equivale a una nota indexada.
2. **Calcular y revisar.** Cada entrada indica comienzo y fin exactos dentro del archivo completo, incluido el índice. Su descripción tiene **máximo diez palabras**, identifica el contenido y no reproduce datos privados. Conservar títulos y cuerpo; ante un título largo, resumir la descripción sin cambiarlo. Actualizar también registro e informes de cierre.
3. **Comprobar lectura.** Cada rango comienza donde corresponde y termina antes de la sección siguiente, sin dejar contenido sin cubrir. Recalcular tras cada edición; aplicar dos veces no debe volver a modificar la nota. Comparar consulta por rangos y lectura completa, registrando verificaciones.

## Auxiliar opcional para la IA

- `python -B herramientas/indice_lineas.py check --boveda <copia> --excluir '<patrón acordado>'`
- `python -B herramientas/indice_lineas.py apply <nota1> <nota2> ...`
- Repetir `check`. El script conserva el cuerpo y limita descripciones a diez palabras; la IA revisa su sentido. No cambiar el texto para ajustar el índice.

Sin Python, usar números de línea de las herramientas, escribir el índice y volver a leer el archivo numerado para comprobar rangos. No estimar posiciones ni afirmar exactitud sin revisión. Recalcular los ejemplos de las plantillas después de completar sus datos.
