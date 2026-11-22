from datetime import date
from getpass import getpass

from model.departamento import Departamento
from model.empleado import Empleado
from model.informe_excel import InformeExcel
from model.informe_pdf import InformePDF
from model.proyecto import Proyecto
from model.registro_tiempo import RegistroTiempo
from model.servicio_api import ErrorServicioExterno, ServicioClima, ServicioTipoCambio


class Aplicacion:
    MAX_INTENTOS = 3

    def __init__(self):
        self.__clima = ServicioClima()
        self.__cambio = ServicioTipoCambio()
        self.__empleado = None
        self.__departamentos = []
        self.__proyectos = []
        self.__registros = []

    def preparar_usuario(self):
        print("=== EcoTech Solutions ===")
        usuario = input("Crea un usuario de prueba: ").strip()
        password = getpass("Crea una contraseña: ")
        if not usuario or len(password) < 6:
            raise ValueError("Usuario obligatorio y contraseña de al menos 6 caracteres")
        self.__empleado = Empleado(
            1, "Eimy", "Puerto Montt", "999999999", "eimy@ecotech.cl",
            str(date.today()), 1900000, usuario, password,
        )

    def iniciar_sesion(self) -> bool:
        credencial = self.__empleado.get_credencial()
        for _ in range(self.MAX_INTENTOS):
            usuario = input("Usuario: ").strip()
            password = getpass("Contraseña: ")
            if usuario == credencial.get_usuario() and credencial.autenticar(password):
                print("Sesión iniciada")
                return True
            if credencial.esta_bloqueado():
                print("Cuenta bloqueada por demasiados intentos")
                return False
            print("Credenciales incorrectas")
        return False

    def consultar_clima(self):
        ciudad = input("Ciudad: ")
        datos = self.__clima.obtener_clima(ciudad)
        print(f"{datos['ciudad']}, {datos['pais']}: {datos['temperatura']} °C, "
              f"humedad {datos['humedad']}%, {datos['estado']}")

    def convertir_pago(self):
        moneda = input("Moneda (dolar/euro): ")
        try:
            monto = float(input("Monto en pesos chilenos: "))
        except ValueError:
            raise ValueError("El monto debe ser un número")
        resultado = self.__cambio.convertir_pago(monto, moneda)
        print(f"{monto:,.0f} CLP equivalen a {resultado:,.2f} {moneda.strip().lower()}")

    def crear_departamento_y_proyecto(self):
        nombre_depto = input("Nombre del departamento: ")
        departamento = Departamento(nombre_depto, self.__empleado)
        departamento.asignar_empleado(self.__empleado)
        self.__departamentos.append(departamento)

        nombre_proyecto = input("Nombre del proyecto: ")
        descripcion = input("Descripción: ")
        proyecto = Proyecto(nombre_proyecto, descripcion)
        proyecto.asignar_empleado(self.__empleado)
        self.__proyectos.append(proyecto)
        print(f"Creados: {departamento} y {proyecto}")

    def registrar_horas(self):
        if not self.__proyectos:
            raise ValueError("Primero crea un proyecto")
        proyecto = self.__proyectos[-1]
        try:
            horas = float(input("Horas trabajadas: "))
        except ValueError:
            raise ValueError("Las horas deben ser un número")
        tarea = input("Tarea realizada: ")
        registro = RegistroTiempo(date.today(), horas, tarea, self.__empleado, proyecto)
        self.__registros.append(registro)
        print(f"Registro guardado: {registro}")

    def exportar_informe(self):
        if not self.__registros:
            raise ValueError("No hay registros para exportar")
        encabezados = ["Fecha", "Empleado", "Proyecto", "Horas", "Tarea"]
        filas = [
            [str(r.get_fecha()), r.get_empleado().get_nombre(),
             r.get_proyecto().get_nombre(), r.get_horas(), r.get_tarea()]
            for r in self.__registros
        ]
        opcion = input("Formato (1 Excel, 2 PDF): ").strip()
        if opcion == "1":
            ruta = InformeExcel("Horas trabajadas", encabezados, filas).exportar("informe_horas.xlsx")
        elif opcion == "2":
            ruta = InformePDF("Horas trabajadas", encabezados, filas).exportar("informe_horas.pdf")
        else:
            raise ValueError("Opción de formato no válida")
        print(f"Informe generado: {ruta}")

    def ejecutar_opcion(self, opcion: str) -> bool:
        acciones = {
            "1": self.consultar_clima,
            "2": self.convertir_pago,
            "3": self.crear_departamento_y_proyecto,
            "4": self.registrar_horas,
            "5": self.exportar_informe,
        }
        if opcion == "0":
            return False
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción no válida")
            return True
        try:
            accion()
        except ValueError as error:
            print(f"Dato no válido: {error}")
        except ErrorServicioExterno as error:
            print(f"Servicio externo: {error}")
        except ImportError:
            print("Falta instalar una librería para esta función")
        except Exception:
            print("Ocurrió un error inesperado. Intenta nuevamente")
        return True

    def menu(self):
        continuar = True
        while continuar:
            print("\n1. Consultar clima")
            print("2. Convertir pago a otra moneda")
            print("3. Crear departamento y proyecto")
            print("4. Registrar horas")
            print("5. Exportar informe")
            print("0. Salir")
            continuar = self.ejecutar_opcion(input("Opción: ").strip())

    def ejecutar(self):
        try:
            self.preparar_usuario()
        except ValueError as error:
            print(f"Dato no válido: {error}")
            return
        if self.iniciar_sesion():
            self.menu()
        else:
            print("Acceso denegado")


if __name__ == "__main__":
    Aplicacion().ejecutar()
