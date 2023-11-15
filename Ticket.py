#librerias para imprimir
#from ironpdf import *
import os
#librerias de PDF
import pdfkit
import jinja2

class Ticket():
    def __init__(self, productos, precioTotal):
        # Crear un objeto PDF
        self.rutaPDF = "ticket.pdf"
        
        width = 227
        height = 340
        

    #def imprimirTicket(self, rutaArchivo):
        #pdf = self.PdfDocument.FromFile(rutaArchivo)
        #pdf.Print()

    def obtenerRuta(self):
        return self.rutaPDF
    
ticket = Ticket(1, 2)

