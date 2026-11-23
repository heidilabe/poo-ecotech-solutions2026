from model.informe import Informe


class InformeExcel(Informe):
    def exportar(self, ruta: str) -> str:
        from openpyxl import Workbook

        libro = Workbook()
        hoja = libro.active
        hoja.title = "Informe"
        hoja.append([self.get_titulo()])
        hoja.append(["Generado", self.get_fecha_generacion().strftime("%d/%m/%Y %H:%M")])
        hoja.append([])
        hoja.append(self.get_encabezados())
        for fila in self.get_filas():
            hoja.append(fila)
        libro.save(ruta)
        return ruta