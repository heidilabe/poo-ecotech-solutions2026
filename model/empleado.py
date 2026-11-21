from model.credencial import CredencialAcceso
from model.validador_entrada import ValidadorEntrada


class Empleado:
    def __init__(
        self,
        id_empleado: int,
        nombre: str,
        direccion: str,
        telefono: str,
        correo: str,
        fecha_inicio_contrato: str,
        salario: float,
        usuario: str,
        password: str,
    ):
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._fecha_inicio_contrato = fecha_inicio_contrato
        self._salario = salario

        self._credencial = CredencialAcceso(usuario, password)
        self._registros = []
        self._asignaciones = []
        self._departamento = None

    def get_id_empleado(self) -> int:
        return self._id_empleado

    def get_nombre(self) -> str:
        return self._nombre

    def get_direccion(self) -> str:
        return self._direccion

    def get_telefono(self) -> str:
        return self._telefono

    def get_correo(self) -> str:
        return self._correo

    def get_fecha_inicio_contrato(self) -> str:
        return self._fecha_inicio_contrato

    def get_credencial(self) -> CredencialAcceso:
        return self._credencial

    def get_registros(self) -> list:
        return self._registros

    def get_asignaciones(self) -> list:
        return self._asignaciones

    def get_departamento(self):
        return self._departamento

    def get_salario(self) -> float:
        return self._salario

    def actualizar_datos(
        self,
        direccion: str,
        telefono: str,
        correo: str,
    ) -> bool:
        validador = ValidadorEntrada()

        if (
            validador.validar_texto(direccion)
            and validador.validar_texto(telefono)
            and validador.validar_email(correo)
        ):
            self._direccion = direccion
            self._telefono = telefono
            self._correo = correo
            return True

        print("Error: Los datos proporcionados no son válidos.")
        return False