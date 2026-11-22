from datetime import date
from itertools import count

from model.validador_entrada import ValidadorEntrada


class RegistroTiempo:
    _secuencia = count(1)

    def __init__(self, fecha: date, horas: float, tarea: str, empleado, proyecto):
        if empleado is None or proyecto is None:
            raise ValueError("El registro requiere empleado y proyecto")
        self.__id = next(RegistroTiempo._secuencia)
        self.__fecha = fecha
        self.__horas = horas
        self.__tarea = tarea
        self.__empleado = empleado
        self.__proyecto = proyecto
        self.validar()

    def validar(self):
        validador = ValidadorEntrada()
        if not validador.validar_horas(self.__horas):
            raise ValueError("Las horas deben ser mayores que 0 y hasta 24")
        if not validador.validar_texto(self.__tarea):
            raise ValueError("La tarea no puede estar vacía")

    def get_id(self) -> int:
        return self.__id

    def get_fecha(self) -> date:
        return self.__fecha

    def get_horas(self) -> float:
        return self.__horas

    def get_tarea(self) -> str:
        return self.__tarea

    def get_empleado(self):
        return self.__empleado

    def get_proyecto(self):
        return self.__proyecto

    def __str__(self):
        return (f"{self.__fecha} | {self.__horas} h | {self.__tarea} | "
                f"{self.__empleado.get_nombre()} | {self.__proyecto.get_nombre()}")