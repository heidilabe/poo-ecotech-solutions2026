import re

import requests


class ErrorServicioExterno(Exception):
    pass


class ServicioAPI:
    TIMEOUT = 8

    def __init__(self):
        self.__sesion = requests.Session()

    def _solicitar(self, url: str, parametros: dict = None) -> dict:
        try:
            respuesta = self.__sesion.get(url, params=parametros, timeout=self.TIMEOUT)
        except requests.exceptions.Timeout:
            raise ErrorServicioExterno("El servicio externo tardó demasiado en responder")
        except requests.exceptions.ConnectionError:
            raise ErrorServicioExterno("No hay conexión con el servicio externo")
        except requests.exceptions.RequestException:
            raise ErrorServicioExterno("No se pudo completar la solicitud")

        if respuesta.status_code == 404:
            raise ErrorServicioExterno("El recurso solicitado no existe")
        if respuesta.status_code >= 500:
            raise ErrorServicioExterno("El servicio externo no está disponible por ahora")
        if respuesta.status_code != 200:
            raise ErrorServicioExterno(f"Respuesta inesperada del servicio ({respuesta.status_code})")

        try:
            return respuesta.json()
        except ValueError:
            raise ErrorServicioExterno("El servicio entregó una respuesta que no se pudo leer")


class ServicioClima(ServicioAPI):
    URL_GEOCODIFICACION = "https://geocoding-api.open-meteo.com/v1/search"
    URL_PRONOSTICO = "https://api.open-meteo.com/v1/forecast"
    DESCRIPCIONES = {
        0: "Despejado",
        1: "Mayormente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna",
        55: "Llovizna intensa",
        61: "Lluvia ligera",
        63: "Lluvia",
        65: "Lluvia intensa",
        71: "Nieve ligera",
        73: "Nieve",
        75: "Nieve intensa",
        80: "Chubascos",
        95: "Tormenta",
    }

    def validar_ciudad(self, ciudad: str) -> str:
        if not isinstance(ciudad, str) or not ciudad.strip():
            raise ValueError("Debes ingresar una ciudad")
        ciudad = ciudad.strip()
        if len(ciudad) > 60 or not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü .'-]+", ciudad):
            raise ValueError("La ciudad solo puede tener letras y espacios")
        return ciudad

    def obtener_clima(self, ciudad: str) -> dict:
        ciudad = self.validar_ciudad(ciudad)
        datos = self._solicitar(
            self.URL_GEOCODIFICACION,
            {"name": ciudad, "count": 1, "language": "es"},
        )
        resultados = datos.get("results")
        if not resultados:
            raise ErrorServicioExterno("No se encontró la ciudad indicada")
        lugar = resultados[0]

        pronostico = self._solicitar(
            self.URL_PRONOSTICO,
            {
                "latitude": lugar["latitude"],
                "longitude": lugar["longitude"],
                "current": "temperature_2m,relative_humidity_2m,weather_code",
            },
        )
        actual = pronostico.get("current")
        if not actual:
            raise ErrorServicioExterno("El servicio no entregó datos del clima")

        codigo = actual.get("weather_code")
        return {
            "ciudad": lugar.get("name", ciudad),
            "pais": lugar.get("country", ""),
            "temperatura": actual.get("temperature_2m"),
            "humedad": actual.get("relative_humidity_2m"),
            "estado": self.DESCRIPCIONES.get(codigo, "Sin descripción"),
        }


class ServicioTipoCambio(ServicioAPI):
    URL_INDICADORES = "https://mindicador.cl/api"
    MONEDAS = ("dolar", "euro")

    def validar_moneda(self, moneda: str) -> str:
        if not isinstance(moneda, str) or not moneda.strip():
            raise ValueError("Debes ingresar una moneda")
        moneda = moneda.strip().lower()
        if moneda not in self.MONEDAS:
            raise ValueError("Moneda no permitida. Opciones: " + ", ".join(self.MONEDAS))
        return moneda

    def obtener_valor(self, moneda: str) -> float:
        moneda = self.validar_moneda(moneda)
        datos = self._solicitar(f"{self.URL_INDICADORES}/{moneda}")
        serie = datos.get("serie")
        if not serie:
            raise ErrorServicioExterno("El servicio no entregó el valor de la moneda")
        valor = serie[0].get("valor")
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ErrorServicioExterno("El valor recibido no es válido")
        return float(valor)

    def convertir_pago(self, monto_clp: float, moneda: str) -> float:
        if not isinstance(monto_clp, (int, float)) or monto_clp <= 0:
            raise ValueError("El monto debe ser un número mayor que cero")
        return round(monto_clp / self.obtener_valor(moneda), 2)
