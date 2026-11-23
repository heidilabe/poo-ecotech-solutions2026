# Documentación de uso de IA – Eimy (rama-eimy)

Herramienta usada: Claude (Anthropic), mediante chat.

## 1. Qué código se apoyó con IA

| Archivo | Apoyo de IA | Qué hice yo |
| --- | --- | --- |
| `model/departamento.py` | Borrador de la clase a partir del informe técnico | Revisé atributos y métodos contra el informe, ajusté y probé |
| `model/proyecto.py` | Borrador de la clase | Revisé, ajusté y probé |
| `model/asignacion_proyecto.py` | Borrador de la clase | Revisé, ajusté y probé |
| `model/registro_tiempo.py` | Borrador y una corrección posterior | Detecté que la validación no funcionaba y se corrigió |
| `model/informe.py`, `informe_pdf.py`, `informe_excel.py` | Borrador con clase abstracta y dos subclases | Probé la exportación a Excel |
| `model/servicio_cifrado.py` | Borrador con Fernet | Revisé |
| `model/servicio_api.py` | Borrador de las APIs de clima y tipo de cambio | Probé con internet real y con datos incorrectos |
| `demo_eimy.py` | Borrador del menú con login | Probé todas las opciones |
| `README.md` | Borrador del texto | Lo ajusté con lo que indicó mi compañera |

## 2. Errores e inconsistencias encontrados en el código de la IA

1. **Validación de horas que no validaba.** El `ValidadorEntrada` de mi compañera devuelve `True` o `False`, pero el código inicial de `RegistroTiempo` lo llamaba sin revisar el resultado, como si lanzara una excepción. Con eso habría aceptado 30 horas o una tarea vacía. Se corrigió con `if not validador.validar_horas(...)` y `raise ValueError`. Comprobé que ahora rechaza 30 horas.
2. **Uso de `@staticmethod`.** El código inicial tenía métodos estáticos (`crear()`, `buscar_por_nombre()` y llamadas directas a `ValidadorEntrada`). El equipo decidió no usarlos. Se eliminaron los `crear()` (el constructor ya crea el objeto), `buscar_por_nombre` pasó a ser método normal y `RegistroTiempo` crea una instancia del validador.
3. **Nombres de métodos supuestos.** La IA supuso que el validador tenía `validar_horas` y `validar_texto`. Comprobé que existen en el código de mi compañera antes de dar por buena la integración.
4. **Contraseñas.** La demo no escribe ninguna contraseña en el código y usa `getpass` para que no se vea al escribirla.
5. **Redundancia.** Mi compañera y yo hicimos cada una una versión de la API (`services/` y `model/servicio_api.py`). Es una duplicación que hay que resolver dejando una sola.
6. **Límites de `servicio_cifrado.py`.** La clave se genera en memoria y no se guarda. Si el programa se reinicia, no se podría descifrar lo cifrado antes. Además, todavía no está integrado en el flujo de la demo.

## 3. Vulnerabilidades y riesgos revisados

- Las entradas del usuario (ciudad, moneda, monto, horas) se validan antes de usarse. La ciudad solo admite letras y espacios, lo que evita mandar texto raro a la API.
- Toda solicitud HTTP tiene límite de 8 segundos para que el programa no quede esperando.
- Los mensajes de error no muestran URLs ni datos internos del servicio.
- Las librerías de PDF y Excel se importan dentro de `exportar()`, así que si faltan, el programa avisa en vez de caerse.

## 4. Decisiones: qué adopté, modifiqué o descarté

- **Adopté:** la herencia `ServicioAPI` → `ServicioClima` y `ServicioTipoCambio`, para escribir el manejo de errores una sola vez; y la clase abstracta `Informe` con `exportar()`.
- **Modifiqué:** la validación de horas, los métodos estáticos y los comentarios del código, que se quitaron por decisión del equipo.
- **Descarté:** guardar contraseñas dentro del código de la demo.

## 5. Pruebas realizadas

- Clima de Puerto Montt y conversión de 1.900.000 pesos a dólares, con internet real.
- Ciudad `123`: rechazada por la validación.
- Ciudad inexistente: mensaje de error del servicio sin cerrar el programa.
- 30 horas: rechazadas.
- Login con contraseña y exportación del informe a Excel.

## 6. Mi conclusión

La IA me ahorró tiempo con el borrador, pero tuve que revisar y probar cada parte, porque cometió errores reales como el de la validación de horas. Entiendo qué hace cada archivo y puedo explicarlo.