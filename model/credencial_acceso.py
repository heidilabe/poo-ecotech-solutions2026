class CredencialAcceso:
    def __init__(self, usuario: str, contrasena: str):
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__intentos_fallidos = 0
        self.__bloqueada = False

    def autenticar(self, usuario: str, contrasena: str) -> bool:
        if self.__bloqueada:
            return False

        if usuario == self.__usuario and contrasena == self.__contrasena:
            self.__intentos_fallidos = 0
            return True

        self.__intentos_fallidos += 1

        if self.__intentos_fallidos >= 3:
            self.bloquear()

        return False

    def cambiar_password(self, contrasena_actual: str, nueva_contrasena: str) -> bool:
        if self.__bloqueada:
            return False

        if contrasena_actual != self.__contrasena:
            return False

        self.__contrasena = nueva_contrasena
        self.__intentos_fallidos = 0
        return True

    def bloquear(self) -> None:
        self.__bloqueada = True

    def esta_bloqueada(self) -> bool:
        return self.__bloqueada