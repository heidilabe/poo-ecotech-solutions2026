# Importamos la funcion que abre la conexion con Supabase 
from database.conexion import conectar_db
# esta funcion crea la tabla " empleados" si todavia no existe.
def validar_tabla_empleados():  # crea la tabla empleado.


    consulta_sql = """
        create table if not exists empleados (
            id_empleado integer primary key,
            nombre varchar(100) not null,
            direccion varchar(150),
            telefono varchar(30),
            correo varchar(100) not null unique,
            fecha_inicio_contrato varchar(20) not null,
            salario numeric not null,
            rol varchar(30) not null,
            nivel_acceso integer,
            cargo varchar(100),
            usuario varchar(50) not null unique,
            password_hash varchar(100) not null,
            intentos_fallidos integer default 0,
            bloqueado boolean default false
        )
    """
    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_sql)
            conn.commit()  # En PostgreSQL hay que confirmar para que la tabla se guarde
            print("[INFO] Tabla empleados creada correctamente")
    except Exception as e:
        if conn:
            conn.rollback()  # Si algo falla, nada cambia en la base de datos

        print(f"[ERROR] Creación de tabla empleados | {e}")
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()
 # esta funcion guarda un empleado en la tabla empleados.
 # La contraseña no se guarda tal cual: se guarda su hash, que ya calculo CredencialAcceso con bcrypt.
def insertar_empleado(empleado): 
    consulta_insert = "insert into empleados (id_empleado, nombre, direccion, telefono, correo, fecha_inicio_contrato, salario, rol, usuario, password_hash) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta_insert, (
                empleado.get_id_empleado(),
                empleado.get_nombre(),
                empleado.get_direccion(),
                empleado.get_telefono(),
                empleado.get_correo(),
                empleado.get_fecha_inicio_contrato(),
                empleado.get_salario(),
                empleado.obtener_rol(),
                empleado.get_credencial().get_usuario(),
                empleado.get_credencial().get_password_hash()
            ))
            conn.commit()
            print("[INFO] Empleado insertado correctamente")
    except Exception as e:
        if conn:
            conn.rollback()  # Si algo falla, nada cambia en la base de datos

        print(f"[ERROR] Empleado no registrado | {e}")
    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


    #  Esta funcion busca en la tabla un empleado por su usuario.
   #   Devuelve sus datos o None si no existe.

def buscar_empleado_por_usuario(usuario):  # busca empleado por usuario.
    consulta = """
        SELECT id_empleado, nombre, rol, password_hash
        FROM empleados
        WHERE usuario = %s
    """

    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta, (usuario,))
            return cursor.fetchone()

    except Exception as e:
        print(f"[ERROR] No se pudo buscar el empleado | {e}")
        return None

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


# Esta funcion permite actualizar los datos de un empleado.

def actualizar_empleado(id_empleado, direccion, telefono, correo):
    consulta = """
        UPDATE empleados
        SET direccion = %s,
            telefono = %s,
            correo = %s
        WHERE id_empleado = %s
    """

    conn = None
    cursor = None

    try:
        conn = conectar_db()

        if conn:
            cursor = conn.cursor()
            cursor.execute(consulta, (
                direccion,
                telefono,
                correo,
                id_empleado
            ))

            conn.commit()

            if cursor.rowcount > 0:
                print("[INFO] Empleado actualizado correctamente")
                return True
            else:
                print("[INFO] No se encontro el empleado")
                return False

    except Exception as e:
        if conn:
            conn.rollback()

        print(f"[ERROR] No se pudo actualizar el empleado | {e}")
        return False

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

 

                


           


