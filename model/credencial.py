# bcrypt es la libreia que protege las contraseñas.
#Convierte una clave como 1234 en un codigo largo e ilegible, por ejemplo $2b$12$...
# Ese codigo se llama hash, y de el no se puede volver a la clave original
import bcrypt
class CredencialAcceso:
    def __init__(self, usuario: str, password: str):
        self._usuario = usuario
        self._password_hash = self._generar_hash(password)
        self._intentos_fallidos = 0
        self._bloqueado = False

    def _generar_hash(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hash_bytes = bcrypt.hashpw(password.encode("utf-8"),salt)
        return hash_bytes.decode("utf-8") 

    def get_usuario(self) -> str:
        return self._usuario

    def get_password_hash(self) -> str:
        return self._password_hash

    def get_intentos_fallidos(self) -> int:
        return self._intentos_fallidos

    def esta_bloqueado(self) -> bool:
        return self._bloqueado

    def autenticar(self, password: str) -> bool:
        if self._bloqueado:
            print("Error: La cuenta esta bloqueada.")
            return False
        if bcrypt.checkpw(password.encode("utf-8"), self._password_hash.encode("utf-8")):
            self._intentos_fallidos = 0
            return True
        else:
            self._intentos_fallidos += 1
            if self._intentos_fallidos >= 3:
                self.bloquear()
            return False

    def cambiar_password(self,actual: str, nueva: str)-> bool:
            if bcrypt.checkpw(actual.encode("utf-8"), self._password_hash.encode("utf-8")):
                self._password_hash = self._generar_hash(nueva)
                return True
            else:
                print("Error: La contraseña actual no es correcta,")
                return False
            
    def bloquear(self):
        self._bloqueado = True




