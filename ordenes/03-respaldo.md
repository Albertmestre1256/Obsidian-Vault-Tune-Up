# Fase 3: respaldo verificado

**Objetivo:** tener una copia completa y verificada de la bóveda antes del primer cambio.

**Regla:** no se escribe en la bóveda. Solo se escribe en la carpeta de respaldo (fuera de la bóveda) y en la de trabajo.

## Con Python

```text
python -B herramientas/respaldo.py <bóveda> <respaldo-nuevo> <trabajo>
```

Copia todo, genera `<trabajo>/manifiesto-original.csv` (ruta, bytes y SHA-256 de cada archivo) y compara la copia con el original. En Windows incluye los flujos alternativos de NTFS. No sobrescribe un respaldo existente. Termina con código 0 solo si la copia coincide.

## Sin Python

1. **Carpeta de respaldo:** la que indicó la persona en la fase 2. Si no la indicó, no se sigue. Nombre sugerido: `<bóveda>-respaldo-AAAA-MM-DD-HHMM`.
2. **Copiar todo**, incluidas las carpetas ocultas. Si la copia falla a mitad de camino, se borra la copia parcial (nunca el original) y se empieza de nuevo.
3. **Manifiesto:** ruta relativa, tamaño y SHA-256 de cada archivo del original y de la copia (`Get-FileHash -Algorithm SHA256` en PowerShell; `shasum -a 256` en macOS o Linux).
4. **En Windows, los flujos alternativos:** `Get-Item -LiteralPath <archivo> -Stream *`. El hash de un archivo no los cubre. En una prueba real, dos reportes con todo su texto en flujos ocultos pasaron la comparación de hashes sin aparecer.
5. **Verificar:** mismo número de archivos y mismo SHA-256 en cada archivo y flujo. Si hay diferencias, parar.

## Informe

En la carpeta de trabajo:

```markdown
# Respaldo verificado — AAAA-MM-DD HH:MM
- Respaldo: <ruta> · Archivos: <n> = <n> · Flujos alternativos: <n> · Diferencias: ninguna
- Manifiesto: manifiesto-original.csv · IA: <nombre> (<herramienta>, <modelo>)
```

## Tené en cuenta

- El respaldo es una foto. Si la bóveda cambia después (otra sesión, Obsidian abierto), la verificación final lo marca como cambio fuera del plan.
- **Revertir:** se copia el respaldo sobre la bóveda, con la persona presente y confirmándolo. Con `.git/` también sirve `git restore`.
- El respaldo no se borra sin aprobación de la persona, ni siquiera al terminar.

## Criterio de salida

Respaldo verificado, con el informe y el manifiesto guardados. Recién entonces se pasa a la fase 4.
