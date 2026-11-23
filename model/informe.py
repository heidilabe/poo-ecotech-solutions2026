from abc import ABC, abstractmethod
from datetime import datetime


class Informe(ABC):
    def __init__(self, titulo: str, encabezados: list, filas: list):
        if not titulo or not titulo.strip():
            raise ValueError("El informe necesita un título")
        self.__titulo = titulo.strip()
        self.__encabezados = list(encabezados)
        self.__filas = [list(f) for f in filas]
        self.__fecha_generacion = datetime.now()

    def get_titulo(self) -> str:
        return self.__titulo

    def get_encabezados(self) -> list:
        return list(self.__encabezados)

    def get_filas(self) -> list:
        return [list(f) for f in self.__filas]

    def get_fecha_generacion(self) -> datetime:
        return self.__fecha_generacion

    @abstractmethod
    def exportar(self, ruta: str) -> str:
        pass