class ValidadorEntrada:
    @staticmethod
    def validar_email(v: str) -> bool:
        # Debe ser texto y tener un @
        if not isinstance(v, str) or "@" not in v:
            return False
        # Despues del @ tiene que haber un punto (ej: mail.com)
        partes = v.split("@")
        if "." in partes[1]:
            return True
        else:
            return False

    @staticmethod
    def validar_texto(v: str) -> bool:
        # Debe ser texto y no estar vacio
        if isinstance(v, str) and v.strip() != "":
            return True
        else:
            return False

    @staticmethod
    def validar_horas(h: float) -> bool:
        # Debe ser un numero mayor que  0 y hasta 24
        if isinstance(h, (int, float)) and h > 0 and h <= 24:
            return True
        else:
            return False

