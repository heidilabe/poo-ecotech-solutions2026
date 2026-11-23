"""from model.administrador import Administrador
from model.colaborador import Colaborador
from database.empleado_dao import buscar_empleado_por_usuario
from database.empleado_dao import actualizar_empleado
from database.empleado_dao import eliminar_empleado
from database.empleado_dao import insertar_empleado

  

admin = Administrador(1, "Luis", "Calle 1", "999111222", "luis@mail.com", "2026-01-15", 1800000, "luis", "1234", 3)
colab = Colaborador(2, "Ana", "Calle 2", "999333444", "ana@mail.com", "2026-02-01", 1200000, "ana", "1234", "Analista")

print(admin.mostrar_datos())
print(colab.mostrar_datos())
print(colab.tiene_permiso("registros"))
print(admin.get_credencial().autenticar("1234"))
print(colab.actualizar_datos("Calle 5", "999555666", "ana.nueva@mail.com"))
# Prueba de busqueda de empleado en Supabase
print("\n--- BUSQUEDA DE EMPLEADO ---")

empleado = buscar_empleado_por_usuario("luis")

if empleado:
    print("Empleado encontrado:")
    print("ID:", empleado[0])
    print("Nombre:", empleado[1])
    print("Rol:", empleado[2])
    print("Hash de contraseña:", empleado[3])
else:
    print("No se encontro el empleado.")

# ACTUALIZAR EMPLEADO

print("\n--- ACTUALIZAR EMPLEADO ---")

resultado = actualizar_empleado(
    1,
    "Calle 10",
    "999777666",
    "luis@mail.com"
)

print("Resultado de actualizacion:", resultado)

# ==========================================
# REGISTRAR EMPLEADO DE PRUEBA
# ==========================================

pedro = Colaborador(
    3,
    "Pedro",
    "Calle 20",
    "999888777",
    "pedro@mail.com",
    "2026-03-01",
    1000000,
    "pedro",
    "1234",
    "Asistente"
)

insertar_empleado(pedro)"""
import bcrypt

from database.conexion import conectar_db
from database.empleado_dao import (
    actualizar_empleado,
    buscar_empleado_por_usuario,
    eliminar_empleado,
    insertar_empleado,
    validar_tabla_empleados,
)
from model.administrador import Administrador
from model.colaborador import Colaborador


def iniciar_sesion():
    print("\n--- INICIAR SESION ---")
    usuario = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    registro = buscar_empleado_por_usuario(usuario)
    if not registro:
        print("[ERROR] Usuario no encontrado.")
        return

    id_empleado, nombre, rol, password_hash = registro

    try:
        es_valida = bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8"),
        )
    except Exception:
        es_valida = False

    if es_valida:
        print(f"[INFO] Bienvenido/a {nombre} (ID: {id_empleado} | Rol: {rol})")
    else:
        print("[ERROR] Contraseña incorrecta.")


def registrar_empleado():
    print("\n--- REGISTRAR EMPLEADO ---")
    try:
        id_empleado = int(input("ID empleado (numero): ").strip())
        nombre = input("Nombre: ").strip()
        direccion = input("Direccion: ").strip()
        telefono = input("Telefono: ").strip()
        correo = input("Correo: ").strip()
        fecha_inicio = input("Fecha inicio contrato (YYYY-MM-DD): ").strip()
        salario = float(input("Salario: ").strip())
        usuario = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()
        tipo = input("Tipo (1 = Administrador, 2 = Colaborador): ").strip()

        if tipo == "1":
            nivel = int(input("Nivel de acceso (numero): ").strip())
            empleado = Administrador(
                id_empleado, nombre,direccion,telefono,correo,fecha_inicio,salario, usuario, password, nivel,
            )
        else:
            cargo = input("Cargo: ").strip()
            empleado = Colaborador(id_empleado,nombre,direccion,telefono,correo, fecha_inicio,salario,usuario,password,cargo,
            )
        insertar_empleado(empleado)
    except ValueError:
        print("[ERROR] Revisa que ID, salario o nivel sean numeros validos.")


def buscar_empleado():
    print("\n--- BUSCAR EMPLEADO ---")
    usuario = input("Usuario a buscar: ").strip()
    empleado = buscar_empleado_por_usuario(usuario)

    if empleado:
        print("Empleado encontrado:")
        print("ID:", empleado[0])
        print("Nombre:", empleado[1])
        print("Rol:", empleado[2])
    else:
        print("No se encontro el empleado.")


def actualizar_empleado_menu():
    print("\n--- ACTUALIZAR EMPLEADO ---")
    try:
        id_empleado = int(input("ID del empleado a actualizar: ").strip())
        direccion = input("Nueva direccion: ").strip()
        telefono = input("Nuevo telefono: ").strip()
        correo = input("Nuevo correo: ").strip()
        actualizar_empleado(id_empleado, direccion, telefono, correo)
    except ValueError:
        print("[ERROR] El ID debe ser un numero entero.")


def eliminar_empleado_menu():
    print("\n--- ELIMINAR EMPLEADO ---")
    try:
        id_empleado = int(input("ID del empleado a eliminar: ").strip())
        eliminar_empleado(id_empleado)
    except ValueError:
        print("[ERROR] El ID debe ser un numero entero.")


def mostrar_menu():
    while True:
        print("\n===== ECOTECH SOLUTIONS =====")
        print("1. Iniciar sesión")
        print("2. Registrar empleado")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_empleado()
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            actualizar_empleado_menu()
        elif opcion == "5":
            eliminar_empleado_menu()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("[ERROR] Opcion no valida.")


if __name__ == "__main__":
    conexion_prueba = conectar_db()
    if conexion_prueba:
        conexion_prueba.close()
        print("[INFO] Conexion verificada con Supabase.")
        validar_tabla_empleados()
        mostrar_menu()
    else:
        print("[ERROR] No se pudo iniciar el sistema por falla en la conexion.")