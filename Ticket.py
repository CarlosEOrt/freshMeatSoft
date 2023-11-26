#librerias para imprimir
#librerias de PDF
import aspose.pdf as ap
from ironpdf import PdfDocument

class Ticket():
    def __init__(self, productos, precioTotal, fecha):
        # Crear un objeto PDF
        self.rutaPDF = "Documentos\\Tickets\\ticket.pdf"
        document = ap.Document()
        longitudPantalla=45

        # Add page
        page = document.pages.add()
        page.set_page_size(227, 340);
        # Initialize textfragment object
        text = ap.facades.FormattedText("Fresh Meat Soft: " + str(fecha))
        text.add_new_line_text("")
        text.add_new_line_text("")
        text.add_new_line_text("______________________________________________")
        text.add_new_line_text("")
        text.add_new_line_text("")
        
        text.add_new_line_text("     Producto    -    Cantidad    -    Precio")
        for fila in range(len(productos)):
            text.add_new_line_text("")
            longitud = len(str(productos[fila][1])+f" {float(productos[fila][2]):.2f}"+f" ${float(productos[fila][3]):.2f}")
            espacioEntreCosas=(longitudPantalla+longitud)/3
            stringEspacio=""
            for i in range(int(espacioEntreCosas)):
                stringEspacio+=" "
            text.add_new_line_text(str(productos[fila][1])+stringEspacio+f" {float(productos[fila][2]):.2f}"+stringEspacio+f" ${float(productos[fila][3]):.2f}")
        text.add_new_line_text("")
        text.add_new_line_text("______________________________________________")
        text.add_new_line_text("")
        text.add_new_line_text("")
        text.add_new_line_text("     Precio total de la venta: "+ f"{float(precioTotal):.2f}")
        text.add_new_line_text("")
        text.add_new_line_text("     ¡Que tenga un excelente dia! ;D")
        stamp = ap.TextStamp(text)
        # Specify the Horizontal Alignment of text stamp as Center aligned
        stamp.horizontal_alignment = ap.HorizontalAlignment.LEFT
        stamp.horizontal_alignment = ap.HorizontalAlignment.LEFT
        # Specify the Vertical Alignment of text stamp as Center aligned
        stamp.vertical_alignment = ap.VerticalAlignment.CENTER
        # Specify the Text Horizontal Alignment of TextStamp as Center aligned
        stamp.text_alignment = ap.HorizontalAlignment.LEFT
        # Set top margin for stamp object
        stamp.top_margin = 10
        stamp.left_margin = 1
        document.pages[1].add_stamp(stamp)
        action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
        document.open_action = action
        # Save updated PDF
        document.save(self.rutaPDF)
        

    def imprimirTicket(self, rutaArchivo):
        pdf = PdfDocument.FromFile(rutaArchivo)
        pdf.Print()

    def obtenerRuta(self):
        return self.rutaPDF

