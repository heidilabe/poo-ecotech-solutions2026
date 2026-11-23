from itertools import count


class Departamento:
    _secuencia = count(1)

    def __init__(self, nombre: str, gerente=None):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del departamento es obligatorio")
        self.__id = next(Departamento._secuencia)
        self.__nombre = nombre.strip()
        self.__gerente = gerente
        self.__empleados = []

    def get_id(self) -> int:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_gerente(self):
        return self.__gerente

    def get_empleados(self) -> list:
        return list(self.__empleados)

    def editar(self, nombre=None, gerente=None):
        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre no puede quedar vacío")
            self.__nombre = nombre.strip()
        if gerente is not None:
            self.__gerente = gerente

    def buscar_por_nombre(self, texto: str) -> bool:
        return texto.strip().lower() in self.__nombre.lower()

    def asignar_empleado(self, empleado):
        if empleado in self.__empleados:
            raise ValueError("El empleado ya pertenece a este departamento")
        self.__empleados.append(empleado)

    def quitar_empleado(self, empleado):
        if empleado not in self.__empleados:
            raise ValueError("El empleado no pertenece a este departamento")
        self.__empleados.remove(empleado)

    def reasignar_empleado(self, empleado, nuevo_departamento):
        self.quitar_empleado(empleado)
        nuevo_departamento.asignar_empleado(empleado)

    def __str__(self):
        return f"Departamento {self.__id}: {self.__nombre}"