from model.empleado import Empleado


class Administrador(Empleado):
    def __init__(
        self,
        nombre: str,
        direccion: str,
        telefono: str,
        correo: str,
        contrato,
        salario: float,
        credencial,
        nivel_acceso: int,
    ):
        super().__init__(
            nombre,
            direccion,
            telefono,
            correo,
            contrato,
            salario,
            credencial,
        )
        self.__nivel_acceso = nivel_acceso
        self.__empleados_registrados = []

    def obtener_rol(self) -> str:
        return "Administrador"

    def tiene_permiso(self, modulo: str) -> bool:
        return True

    def registrar_empleado(self, empleado: Empleado) -> bool:
        if not isinstance(empleado, Empleado):
            return False

        self.__empleados_registrados.append(empleado)
        return True

    def gestionar_departamento(self, departamento, nuevo_nombre: str) -> None:
        departamento.editar(nuevo_nombre)

    def solicitar_informe(self, informe, datos):
        return informe.exportar(datos)