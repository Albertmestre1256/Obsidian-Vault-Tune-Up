# Paso 10: validar y entregar

1. **Conservación y funcionamiento.** Comparar cada archivo original con su ubicación final o versión recuperable dentro de la entrega. Verificar movimientos, adjuntos, flujos NTFS, enlaces, reglas, agrupaciones, Sin clasificar e índices de notas e informes. Revisar cada consolidación contra sus fuentes: listar archivos esperados no demuestra conservación semántica. Con pérdida o cambios ajenos al plan, detenerse.
2. **Contexto y sesión nueva.** Medir el mismo recorrido antes/después: reglas → entrada → tabla de nodos por rangos → nodo → sección. Registrar caracteres y estimación de tokens; informar también si no hubo ahorro. Probar lectura y una edición acotada con recálculo del índice. Una sesión nueva debe orientarse. Para acreditar eficiencia usar el [protocolo de evaluación](../evaluacion/PROTOCOLO.md): mismas tareas, calidad con evidencia, consumo real cuando se exponga, intentos fallidos y costes de preparación y mantenimiento. Declarar si la misma IA organiza y evalúa, si falta uso instrumentado y los demás límites. La revisión visual es opcional para presentación; no es una medida de eficiencia.
3. **Entrega independiente.** IA instalada: indicar carpeta organizada y respaldo, sin reemplazar el original. IA web: producir ZIP descargable, extraerlo en otra carpeta nueva y comparar contenido, adjuntos y versiones preservadas contra la salida preparada. Entregar enlace y cambios, pendientes y reversión. El reemplazo queda a decisión de la persona.

## Auxiliar opcional para la IA

`python -B herramientas/verificar.py <copia> <respaldo> <trabajo> <esperados.txt> --movimientos <movimientos.json> [--excluir '<patrón acordado>']`

El trabajo contiene `manifiesto-original.csv` del respaldo de la copia y `diagnostico-datos.json`. `esperados.txt` enumera rutas que cambia/crea el plan; **no autoriza pérdidas**. `movimientos.json` relaciona rutas anteriores y finales; si no hubo movimientos, omitir la opción. El verificador detecta ausencias no trazadas, cambios fuera de rutas esperadas, movimientos con contenido diferente, destinos ocupados sin conservación trazada, flujos perdidos e índices pendientes. Al comparar notas movidas acepta reparaciones de wikilinks y enlaces Markdown sencillos si siguen apuntando al mismo archivo según el mapa de movimientos; conserva etiquetas, fragmentos y código literal. Otros formatos de enlace requieren revisión aparte. Si el texto está conservado pero un enlace dejó de resolver por el movimiento, informa navegación pendiente y mantiene el resultado parcial; no lo presenta como contenido perdido. No prueba que una síntesis conserve cada hecho ni que una relación temática sea correcta. Reglas con nombres adaptados y enlaces necesitan revisión adicional.

No ejecutar scripts propios de la bóveda sin autorización. No excluir problemas solo para conseguir un resultado correcto. Registrar excepciones y motivos.

## Informe de entrega

Guardar primero un informe en la copia según sus reglas: estado, alcance aprobado, agrupaciones, cambios, originales conservados, inventario de Sin clasificar, verificaciones, contexto antes/después, límites y pendientes. Registrar su creación y recalcular todos los índices tocados **antes** de la verificación final y el ZIP. No empaquetar el trabajo externo con datos privados o evidencia innecesaria.

## Qué significa éxito

- Conservación comprobada y agrupaciones/reglas respetadas.
- Reglas, mapa y Leer primero permiten encontrar y mantener información.
- Notas editables con rangos exactos y descripciones de hasta diez palabras; excepciones explícitas.
- Menos redundancia activa y contexto cuando hay una oportunidad real, con medición comparable y originales recuperables.
- Carpeta independiente o ZIP comprobado; el original sigue intacto.

Distinguir entrega verificada de optimización lograda. Sin ahorro, no afirmar optimización exitosa. Si faltan conservación, índices o capacidad de entregar archivos, el resultado es **parcial**, con motivo y próximo paso. No afirmar pruebas con personas ni compatibilidad con todas las IA web sin evidencia.
