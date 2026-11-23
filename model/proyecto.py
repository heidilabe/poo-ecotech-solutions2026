from datetime import date
from itertools import count

from model.asignacion_proyecto import AsignacionProyecto


class Proyecto:
    _secuencia = count(1)

    def __init__(self, nombre: str, descripcion: str, fecha_inicio: date = None):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del proyecto es obligatorio")
        self.__id = next(Proyecto._secuencia)
        self.__nombre = nombre.strip()
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio or date.today()
        self.__asignaciones = []

    def get_id(self) -> int:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_descripcion(self) -> str:
        return self.__descripcion

    def get_fecha_inicio(self) -> date:
        return self.__fecha_inicio

    def get_asignaciones(self) -> list:
        return list(self.__asignaciones)

    def editar(self, nombre=None, descripcion=None):
        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre no puede quedar vacío")
            self.__nombre = nombre.strip()
        if descripcion is not None:
            self.__descripcion = descripcion

    def asignar_empleado(self, empleado, fecha: date = None) -> AsignacionProyecto:
        for a in self.__asignaciones:
            if a.get_empleado() is empleado and a.esta_vigente():
                raise ValueError("El empleado ya está asignado a este proyecto")
        asignacion = AsignacionProyecto(empleado, self, fecha)
        self.__asignaciones.append(asignacion)
        return asignacion

    def desasignar_empleado(self, empleado):
        for a in self.__asignaciones:
            if a.get_empleado() is empleado and a.esta_vigente():
                a.finalizar()
                return
        raise ValueError("El empleado no tiene una asignación vigente en este proyecto")

    def equipo_vigente(self) -> list:
        return [a.get_empleado() for a in self.__asignaciones if a.esta_vigente()]

    def __str__(self):
        return f"Proyecto {self.__id}: {self.__nombre}"