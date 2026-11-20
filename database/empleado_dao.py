from database.conexion import obtener_conexion


class EmpleadoDAO:
    def listar_empleados(self):
        conn = obtener_conexion()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM empleados;")
                return cur.fetchall()
        finally:
            conn.close()