from model.empleado import Empleado

class Administrador(Empleado):
    def __init__(self, id_empleado: int, nombre: str, direccion: str, telefono: str, correo: str, fecha_inicio_contrato: str, salario: float,nivel_acceso: int):
        super().__init__(id_empleado, nombre, direccion, telefono, correo, fecha_inicio_contrato, salario )
        self.nivel_acceso = nivel_acceso
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

    def solicitar_informe(self, tipo :str):
        return f"Solicitud de informe:{tipo}"
    
      
        
        

    
