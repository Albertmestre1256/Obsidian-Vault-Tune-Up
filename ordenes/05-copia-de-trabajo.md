# Paso 5: copia independiente y respaldo

1. **Preparar destinos nuevos.** IA instalada: `<nombre>-organizado/` fuera del original. IA web: extraer una copia de trabajo aislada para luego empaquetarla. Mantener original recibido, respaldo íntegro y trabajo externo separados de la salida. Rechazar rutas coincidentes, destinos ocupados y escritura a través de enlaces hacia el origen.
2. **Copiar y verificar antes de transformar.** Inventariar origen, copiar, comparar cantidad, tamaño y SHA-256 de archivos y contenido especial (NTFS cuando aplique), y verificar que el origen no cambió durante la captura. Si falta algo o no coincide, conservar evidencia y detener la copia. No alterar el origen para que coincida.
3. **Preparar el respaldo de la copia**, guardar manifiestos y registrar rutas reales. Desde acá, toda operación apunta a la copia organizada. No activar configuraciones o sincronizadores copiados. La persona decide al final si reemplaza el original.

## Auxiliar opcional para la IA

`python -B herramientas/respaldo.py <origen> <salida-nueva> <trabajo>` crea y verifica una copia sin escribir en el origen. Volver a usarlo con la salida como origen y un respaldo nuevo como destino; usar una subcarpeta de trabajo distinta para cada manifiesto.

En Windows verificar los flujos alternativos: una copia puede parecer completa y ocultar texto no visible en Obsidian. Un ZIP común no conserva esos flujos. Si existen, conservar también cada flujo como archivo de preservación, con hash y correspondencia documentada, dentro de la entrega antes de empaquetar. No dar por verificado contenido que nunca se recibió.

Sin Python, usar copia y comprobaciones equivalentes del entorno. No pedir programación a la persona. Si no se puede verificar integridad, informar resultado parcial y no iniciar transformaciones.
