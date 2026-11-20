# Esta es la clase base de todos los trabajadores de la empresa guarda sus datos personales y de contrato como el nombre, correo y salario igual define las acciones comunes que luego heredan Administrador y Colaborador.
class Empleado:
    def __init__(self, id_empleado: int, nombre: str, direccion: str, telefono: str,correo: str,fecha_inicio_contrato: str, salario: float):

        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario

    def get_id_empleado(self) -> int:
        return self.id_empleado
    
    def actualizar_datos(self, direccion: str, telefono: str,correo: str)-> bool:
        if isinstance(direccion, str) and isinstance(telefono, str) and isinstance(correo, str):
            self.direccion = direccion
            self.telefono = telefono
            self.correo = correo
            return True 
        else:
            print("Error: Los datos proporcionados no son válidos.")
        return False
    def registrar_horas(self, fecha: str, horas: float, tarea: str, proyecto: str) -> str:
        return (
            f"Registro de {self.nombre} en {proyecto}| {fecha}:{horas} hrs-{tarea}"
        )
    def obtener_rol(self) -> str:
        return "Empleado"

    def tiene_permiso(self, modulo: str) -> bool:
        return False

    def mostrar_datos(self) -> str:
        return (
            f"Empleado\n ID: {self.id_empleado} | Nombre: {self.nombre} |"
            f"correo: {self.correo} | Rol:{self.obtener_rol()}"
        )
    

            
    
      

        

        
        