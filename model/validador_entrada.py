# Esta clase se encarga de revisar que lo que escribe el usuario como correo, o texto o las horas trabajadas este bien escrito y no venga vacio o con errores antes de guardarlo.

class ValidadorEntrada:
    def validar_email(self, correo: str)-> bool:
        if "@" in correo and "." in correo:
            return True
        else:
            return False

    def validar_texto(self, texto: str)-> bool: 
        texto_limpio = texto.strip()
        if len(texto_limpio) > 0:
            return True
        else:
            return False

    def validar_horas(self, horas: float)->bool:
        if horas > 0 and horas <= 24:
            return True
        else:
            return False



