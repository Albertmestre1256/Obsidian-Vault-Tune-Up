> [!info]- Índice de esta nota (líneas)
> - Líneas 1–8: Este índice
> - Líneas 10–13: P01: espacios dentro del filtro de Grep
> - Líneas 14–21: Hallazgo y mecanismo respaldado
> - Líneas 22–39: Pruebas y controles
> - Líneas 40–45: Implementación acotada en el kit
> - Líneas 46–55: Reproducción y conservación de evidencia
> - Líneas 56–58: Próximo paso y criterio de cierre

# P01: espacios dentro del filtro de Grep

29/10/2026. IA:Codex (Codex desktop). Estado: causa operativa aislada y mitigación local validada; pendiente validar la instrucción en el flujo con modelo. El comportamiento original del cliente sigue reproduciéndose. No se acredita ahorro de tokens.

## Hallazgo y mecanismo respaldado

Grep nativo de Claude Code 2.1.304, expuesto mediante claude mcp serve, reproduce la anomalía de N02: con glob !Versiones conservadas/** devuelve cero; sin ese filtro, 25 líneas. El mismo corpus consultado por rg con esa exclusión tiene 20 líneas.

Se redujo a dos archivos: actual.md y Versiones conservadas/anterior.md, ambos con una línea Brisa. Sin glob devuelve dos. Con la exclusión literal que contiene un espacio devuelve cero, aunque debería conservar actual.md. Con !Versiones*/** o !Versiones?conservadas/** devuelve una. Las negaciones sin espacios, incluso de un directorio inexistente, funcionan en un control de un archivo.

La hipótesis respaldada es que el cliente separa el valor de glob por espacios. Dos observaciones adicionales la distinguen de un fallo general de exclusiones: `Energía/** Archivo/** Reglas.md` se comporta como varios patrones y devuelve 20 líneas; al intentar escapar el espacio con una barra inversa, el error de ripgrep identifica solo el prefijo !Versiones seguido de esa barra, con diagnóstico dangling backslash. Las comillas dentro del valor no lo corrigen. Es evidencia del comportamiento de la interfaz; no se inspeccionó ni modificó el código interno del cliente.

## Pruebas y controles

| Caso | Esperado | Grep nativo observado |
|---|---:|---:|
| B, sin filtro | 25 | 25 |
| B, exclusión literal con espacio | 20 | 0 |
| B, exclusión sin espacio literal | 20 | 20 |
| B, filtro positivo {Energía/**,Archivo/**,Reglas.md} | 20 | 20 |
| B, path exacto a Versiones conservadas | 5 | 5 |
| B, dato inexistente con filtro positivo validado | 0 | 0 |
| Dos archivos, exclusión literal con espacio | 1 | 0 |
| Dos archivos, exclusión entre comillas | 1 | 0 |
| Dos archivos, espacio escapado con barra inversa | 1 | Error explícito |

El filtro positivo se probó dos veces en copias nuevas. En ambas, sus 20 resultados coinciden exactamente con las rutas, líneas y textos obtenidos por rg usando la exclusión original. Las pruebas incluyen un positivo y un negativo reales; no se acepta una herramienta que siempre devuelva cero. Los manifiestos antes/después coinciden.

Los comodines de la prueba son controles diagnósticos, no una sustitución general de nombres: pueden abarcar otras carpetas. La mitigación recomendada es acotar por path exacto y usar patrones simples comprobados; un filtro positivo compuesto solo se usa si su alcance corresponde a la tarea y fue verificado. Una búsqueda parcial no acredita ausencia en toda la bóveda.

## Implementación acotada en el kit

El paso 2 ahora indica verificar un resultado vacío contradictorio con evidencia conocida y usar path exacto ante este caso de Grep. No añade un auxiliar de producción ni impone comandos al usuario. La regla no exige repetir cada búsqueda vacía: se aplica a filtros no comprobados y resultados contradictorios.

No se cambia la instalación de Claude ni se elimina la búsqueda de respaldo. El fallo del cliente permanece reproducible. Se validaron las operaciones de lectura que sustentan la instrucción; falta comprobar que una IA sigue esa instrucción dentro del ensayo completo y mantiene comprensión, coste y tiempo. Eso depende también de P08 y P09.

## Reproducción y conservación de evidencia

Expediente local privado: I:/Obsidian Tune Up/p01-grep-2026-10-29-01/. Contiene probar_grep.py, casos_p01.py, versión y hash del ejecutable, manifiestos, esquemas nativos, solicitudes/respuestas RPC y resultados por intento. Cada intento usa una carpeta nueva y conserva su fuente de prueba; no se sobrescriben fallos.

El caso original se reproduce con casos_p01.py --id NUEVO_ID --modo original y falla deliberadamente al exigir las 20 coincidencias. El modo espacios contiene el caso de dos archivos y conserva también el error de escape. El modo mitigacion valida cinco controles y debe pasar. Elegir un ID sin usar; la persona usuaria no necesita ejecutar estas pruebas.

Intentos relevantes: original-rojo, minimo-rojo (control que no reprodujo), minimo-con-slash (también no reprodujo), dos-archivos-espacios (interrumpido al último caso con error explícito), espacios-completos (todos los resultados conservados), matriz-original y mitigacion-verde-01/02. El primer arranque del servidor no respondió; se conservaron sus trazas y se corrigió la invocación antes de las pruebas funcionales. Los errores de arranque no se cuentan como búsqueda vacía ni como ahorro.

Solo se llamó al protocolo MCP de descubrimiento y a Grep, sin solicitudes a un modelo ni uso de herramientas de escritura en las copias. El servidor ofrece otras herramientas, por lo que no constituye un sandbox: el cliente diagnóstico restringió las llamadas realizadas. La referencia pública describe [Claude Code como servidor MCP](https://code.claude.com/docs/en/mcp#use-claude-code-as-an-mcp-server) y [Grep](https://code.claude.com/docs/en/tools-reference#grep-tool-behavior); la causa específica se sostiene con estas pruebas locales, no con una promesa de la documentación.

## Próximo paso y criterio de cierre

P01 queda mitigado localmente, sin cerrar el fallo original ni afirmar mejora de eficiencia. Tras fijar la rúbrica de P08 y el diseño de P09, probar la instrucción en una nueva sesión acotada y medir si evita el falso cero y conserva los hechos, roles y vigencia. Registrar también el coste de verificar el filtro. Repetir los controles si cambia la versión del cliente; no extrapolar este comportamiento a GPT, OpenCode u otros proveedores.
