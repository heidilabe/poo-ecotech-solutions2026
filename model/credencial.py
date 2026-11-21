import hashlib
import os


class CredencialAcceso:
    def __init__(self, usuario: str, password: str):
        self._usuario = usuario
        self._salt = os.urandom(16).hex()
        self._password_hash = self._generar_hash(password)
        self._intentos_fallidos = 0
        self._bloqueado = False

    def _generar_hash(self, password: str) -> str:
        return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            bytes.fromhex(self._salt),
            100000,
        ).hex()

    def get_usuario(self) -> str:
        return self._usuario

    def get_password_hash(self) -> str:
        return self._password_hash

    def get_salt(self) -> str:
        return self._salt

    def get_intentos_fallidos(self) -> int:
        return self._intentos_fallidos

    def esta_bloqueado(self) -> bool:
        return self._bloqueado

    def autenticar(self, password: str) -> bool:
        if self._bloqueado:
            print("Error: La cuenta esta bloqueada.")
            return False

        if self._generar_hash(password) == self._password_hash:
            self._intentos_fallidos = 0
            return True

        self._intentos_fallidos += 1

        if self._intentos_fallidos >= 3:
            self.bloquear()

        return False

    def cambiar_password(self, actual: str, nueva: str) -> bool:
        if self._generar_hash(actual) == self._password_hash:
            self._salt = os.urandom(16).hex()
            self._password_hash = self._generar_hash(nueva)
            return True

        print("Error: La contraseña actual no es correcta.")
        return False

    def bloquear(self) -> None:
        self._bloqueado = True