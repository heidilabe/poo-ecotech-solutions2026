from cryptography.fernet import Fernet


class ServicioCifrado:
    def __init__(self, clave: bytes = None):
        self.__clave = clave or Fernet.generate_key()
        self.__fernet = Fernet(self.__clave)

    def get_clave(self) -> bytes:
        return self.__clave

    def cifrar(self, texto: str) -> str:
        if not isinstance(texto, str) or not texto:
            raise ValueError("El texto a cifrar no puede estar vacío")
        return self.__fernet.encrypt(texto.encode("utf-8")).decode("utf-8")

    def descifrar(self, token: str) -> str:
        return self.__fernet.decrypt(token.encode("utf-8")).decode("utf-8")