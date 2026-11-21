from model.empleado import Empleado
# esta clase representa a un colaborador de la empresa. Hereda todos los datos de Empleado y agrega su cargo . Sobre el rol y los permisos para que sean distintos a los del Administrador.
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