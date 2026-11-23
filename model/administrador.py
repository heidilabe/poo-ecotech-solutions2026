from model.empleado import Empleado

# Esta clase representa a un administrador de la empresa. Hereda todos los datos de Empleado y agrega su nivel de acceso. Sobrescribe el rol y los permisos, y tiene las acciones de gestión del sistema.
class Administrador(Empleado):
    def __init__(self, id_empleado: int, nombre: str, direccion: str, telefono: str, correo: str, fecha_inicio_contrato: str, salario: float, usuario: str, password: str, nivel_acceso: int):
        super().__init__(id_empleado, nombre, direccion, telefono, correo, fecha_inicio_contrato, salario, usuario, password)
        self._nivel_acceso = nivel_acceso

    def get_nivel_acceso(self) -> int:
        return self._nivel_acceso

    def obtener_rol(self) -> str:
        return "Administrador"

    def tiene_permiso(self, modulo: str) -> bool:
        return True

    def registrar_empleado(self):
        return "Empleado registrado correctamente"

    def gestionar_departamento(self):
        return "Gestion de departamento."

    def gestionar_proyecto(self):
        return "Gestion de proyecto."

    def solicitar_informe(self, tipo: str):
        return f"Solicitud de informe: {tipo}"