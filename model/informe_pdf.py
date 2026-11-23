from model.informe import Informe


class InformePDF(Informe):
    def exportar(self, ruta: str) -> str:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet

        estilos = getSampleStyleSheet()
        doc = SimpleDocTemplate(ruta, pagesize=A4)
        tabla = Table([self.get_encabezados()] + self.get_filas())
        doc.build([
            Paragraph(self.get_titulo(), estilos["Title"]),
            Paragraph(self.get_fecha_generacion().strftime("%d/%m/%Y %H:%M"), estilos["Normal"]),
            Spacer(1, 12),
            tabla,
        ])
        return ruta