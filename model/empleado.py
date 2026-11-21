from abc import ABC, abstractmethod
from datetime import date
from decimal import Decimal
from itertools import count

from model.validador_entrada import ValidadorEntrada


class Empleado(ABC):
    _secuencia = count(1)

    def __init__(
        self,
        nombre: str,
        direccion: str,
        telefono: str,
        correo: str,
        contrato: date,
        salario: float,
        credencial,
    ):
        self.__id = next(Empleado._secuencia)
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__contrato = contrato
        self.__salario = Decimal(str(salario))
        self.__credencial = credencial

    def id(self) -> int:
        return self.__id

    def nombre(self) -> str:
        return self.__nombre

    def registrar_horas(
        self,
        fecha: date,
        horas: float,
        tarea: str,
        proyecto,
    ):
        ValidadorEntrada.validar_horas(horas)

        from model.registro_tiempo import RegistroTiempo

        return RegistroTiempo(fecha, horas, tarea, self, proyecto)

    @abstractmethod
    def obtener_rol(self) -> str:
        pass

    @abstractmethod
    def tiene_permiso(self, modulo: str) -> bool:
        pass