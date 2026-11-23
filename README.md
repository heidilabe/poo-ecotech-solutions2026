# EcoTech Solutions – Sistema de gestión de empleados

Proyecto de Programación Orientada a Objeto Seguro (TI3V21), Evaluación 2.

Programa en Python para gestionar empleados, departamentos, proyectos y horas trabajadas. Pide inicio de sesión, guarda empleados en una base de datos y consulta el clima y el tipo de cambio para planificar proyectos y pagos en otras monedas.

## Equipo

- **Heidi** (`rama-heidi`): base de datos, empleados, roles y login.
- **Eimy** (`rama-eimy`): departamentos, proyectos, registro de horas, informes, cifrado y consumo de APIs.

## Carpetas

- `database/`: conexión y operaciones sobre la base de datos.
- `model/`: las clases del diagrama UML (empleado, administrador, colaborador, credencial, departamento, proyecto, asignación, registro de tiempo, informes, cifrado y servicio de APIs).
- `demo_eimy.py`: menú con login para probar clima, tipo de cambio, horas e informes.
- `main.py`: programa principal.

## Cómo ejecutarlo

```
pip install requests openpyxl reportlab cryptography psycopg2-binary python-dotenv bcrypt
python main.py
```

## Conexión a la base de datos

El proyecto usa PostgreSQL mediante Supabase.

- La conexión está en `database/conexion.py`.
- Las operaciones de acceso a datos están en `database/empleado_dao.py`.

La conexión lee sus datos desde un archivo `.env` en la raíz del proyecto, que no se sube a GitHub. Quien clone el proyecto debe crearlo con estas variables:

```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

## Seguridad de credenciales

Las contraseñas se guardan con hash bcrypt, que ya incluye el salt, para no almacenar credenciales en texto plano. La cuenta se bloquea al tercer intento fallido. Además se validan ciudad, moneda, monto y horas antes de usarlos.

## Menú de usuario

**Administrador**
- Registrar empleados
- Buscar empleados
- Actualizar empleados
- Eliminar empleados
- Gestionar proyectos

**Colaborador**
- Consultar información personal
- Registrar horas de trabajo
- Consultar proyectos asignados

## APIs usadas

- Clima: Open-Meteo.
- Tipo de cambio (dólar y euro): mindicador.cl.

Ninguna necesita llave. Si una API falla (sin internet, tiempo agotado, error 404 o 500), el programa muestra un mensaje corto y sigue funcionando, sin mostrar URLs ni datos internos.

## Uso de IA

Usamos IA como apoyo y revisamos el código antes de dejarlo. Por ejemplo, corregimos la validación de horas, que ignoraba el resultado del validador, y quitamos las contraseñas escritas dentro del código. El detalle está en la carpeta aparte de documentación de IA.
