  # Importamos las librerías que necesitamos:
  # os sirve para leer las variables guardadas en el archivo .env
  # psycopg2 es la librería que conecta Python con PostgreSQL (la base de datos de Supabase)
  # dotenv sirve para cargar el archivo .env dentro de Python
import os
import psycopg2
from dotenv import load_dotenv

 # Carga los datos del archivo .env (host, puerto, usuario, contraseña).
 # Así la contraseña no queda escrita en el código ni se sube a GitHub.
load_dotenv()

 # Esta función abre la conexión con la base de datos de Supabase.
 # Devuelve la conexión si todo sale bien, o None si algo falla.
def conectar_db():
    try:
 # Estos son los parámetros de conexión, y cada uno se lee desde el .env
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),   # dirección del servidor de Supabase
            port=os.getenv("DB_PORT"),   # puerto por donde se entra (5432)
            dbname=os.getenv("DB_NAME"), # nombre de la base de datos
            user=os.getenv("DB_USER"),   # usuario de la base de datos
            password=os.getenv("DB_PASSWORD") # contraseña de la base de datos
        )
        return conn
    except Exception as e:
 # Si falla (sin internet, clave incorrecta, etc.), mostramos el error
 # y devolvemos None para que el programa no se caiga.
        print(f"[ERROR] No se pudo conectar a la bd | {e}")
        return None