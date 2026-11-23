from datetime import date


class AsignacionProyecto:
    def __init__(self, empleado, proyecto, fecha_incorporacion: date = None):
        if empleado is None or proyecto is None:
            raise ValueError("La asignación requiere empleado y proyecto")
        self.__empleado = empleado
        self.__proyecto = proyecto
        self.__fecha_incorporacion = fecha_incorporacion or date.today()
        self.__vigente = True

    def get_empleado(self):
        return self.__empleado

    def get_proyecto(self):
        return self.__proyecto

    def get_fecha_incorporacion(self) -> date:
        return self.__fecha_incorporacion

    def esta_vigente(self) -> bool:
        return self.__vigente

    def finalizar(self):
        self.__vigente = False

    def __str__(self):
        estado = "vigente" if self.__vigente else "finalizada"
        return f"{self.__empleado.get_nombre()} -> {self.__proyecto.get_nombre()} ({estado})"