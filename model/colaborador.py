from datetime import date

from model.empleado import Empleado


class Colaborador(Empleado):
    def __init__(
        self,
        nombre: str,
        direccion: str,
        telefono: str,
        correo: str,
        contrato: date,
        salario: float,
        credencial,
        cargo: str,
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
        self.__cargo = cargo
        self.__registros = []

    def obtener_rol(self) -> str:
        return "Colaborador"

    def tiene_permiso(self, modulo: str) -> bool:
        return modulo == "mis_registros"

    def registrar_horas(
        self,
        fecha: date,
        horas: float,
        tarea: str,
        proyecto,
    ):
        registro = super().registrar_horas(fecha, horas, tarea, proyecto)
        self.__registros.append(registro)
        return registro

    def consultar_mis_registros(self) -> list:
        return self.__registros