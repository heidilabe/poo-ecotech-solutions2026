from model.empleado import Empleado
#colaborador.py es una plantilla que usamos para definir como sera un colaborador dentro 
#del sistema establece que datos tendra, cual sera su cargo y que permisos podra tener.
#Asi cada vez que necesitemos crear un colaborador, utilizamos esa plantilla sin tener que definir todo desde cero.
class Colaborador(Empleado):
    def __init__(self, id_empleado: int, nombre: str, direccion: str,telefono: str, correo: str, fecha_inicio_contrato: str, salario: float,usuario: str, password: str, cargo: str):
        super().__init__(id_empleado, nombre, direccion, telefono, correo, fecha_inicio_contrato, salario, usuario, password)
        self.cargo = cargo

    def obtener_rol(self) -> str:
        return "Colaborador"

    def get_cargo(self) -> str:
        return self.cargo

    def tiene_permiso(self, modulo: str) -> bool:
        return modulo == "registros"

    def consultar_mis_registros(self):
        return f"Registros de{self.get_nombre()}"
