from model.administrador import Administrador
from model.colaborador import Colaborador

admin = Administrador(1, "Luis", "Calle 1", "999111222", "luis@mail.com", "2026-01-15", 1800000, "luis", "1234", 3)
colab = Colaborador(2, "Ana", "Calle 2", "999333444", "ana@mail.com", "2026-02-01", 1200000, "ana", "1234", "Analista")

print(admin.mostrar_datos())
print(colab.mostrar_datos())
print(colab.tiene_permiso("registros"))
print(admin.get_credencial().autenticar("1234"))
print(colab.actualizar_datos("Calle 5", "999555666", "ana.nueva@mail.com"))