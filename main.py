from model.administrador import Administrador
from model.colaborador import Colaborador
from database.empleado_dao import buscar_empleado_por_usuario
from database.empleado_dao import actualizar_empleado


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
    # ==========================================
# ACTUALIZAR EMPLEADO
# ==========================================
print("\n--- ACTUALIZAR EMPLEADO ---")

resultado = actualizar_empleado(
    1,
    "Calle 10",
    "999777666",
    "luis@mail.com"
)

print("Resultado de actualizacion:", resultado)