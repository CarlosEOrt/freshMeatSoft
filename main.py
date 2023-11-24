import sys
import serial
import time
import datetime
import tempfile
import jinja2
import pdfkit
import webbrowser
import os
import os.path
import re
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import messagebox
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from datetime import date, datetime
from os import remove
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from Producto import Producto
from Gasto import Gasto
from Venta import Venta
from Ticket import Ticket

from Comunicacion import Comunicacion


class MyWindow(QMainWindow):
    global arduino
    arduino = serial.Serial('COM3', 9600) # Puerto y baud-rate en los que funciona el Arduino
    global pathTemperatura
    pathTemperatura = "Documentos\\Temperatura\\"

    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('carniceria.ui', self)

        # Control al cargar interfaz
        self.control_btn_pestana()
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowTitle('FRESH MEAT SOFT')

        global nombreArchivo
        # Nombre del archivo donde se guardan las temperaturas
        nombreArchivo = "Reporte Temperatura " + self.obtenerFechaActual() + ".txt"

        # Setteo de datos de las tablas
        self.actualizarTablaInventario()
        self.actualizarTablaGastos()
        self.actualizarTablaTemperaturas()
        self.actualizarResultadosBusqueda()

        # Botones graficas
        self.btn_regresar_estadisticas.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_estadisticas))
        self.btn_regresar_estadisticas2.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_estadisticas))
        self.btn_regresar_estadisticas3.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_estadisticas))
        self.btn_grafica_ventas.clicked.connect(
            lambda: self.dirigirseAPestaniaVentas())
        self.btn_grafica_gastos.clicked.connect(
            lambda: self.dirigirseAPestaniaGastos())
        self.btn_grafica_productos.clicked.connect(
            lambda: self.dirigirseAPestaniaProducto())
        self.actualizarGraficaVentas()
        self.actualizarGraficaGastos()
        self.actualizarGraficaProductos()
        self.lineEdit_grafica_productos.textChanged.connect(
            lambda: self.actualizarGraficaProductos())

        self.timer = QTimer(self) # se crea una variable para constante actualizacion
        self.timer.timeout.connect(lambda:self.actualizarTemperatura())#actualiza el label
        self.timer.start(1)#tiempo que tarda en el contador

        # Redireccion de botones menu
        self.btn_inventario.clicked.connect(
            lambda: self.actualizarTablaInventario())
        self.btn_ventas.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_ventas))
        self.btn_cote_de_caja.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_corte_de_caja))
        self.btn_estadisticas.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_estadisticas))
        self.btn_temperaturas.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_temperaturas))

        # Botones de la barra superior
        self.btn_cerrar.clicked.connect(lambda: self.close())
        self.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.btn_pestana.clicked.connect(self.control_btn_pestana)
        self.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        self.btn_menu.clicked.connect(self.mover_menu)
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # Botones del CRUD botones de redireccion a metodos del CRUD
        self.btn_agregar_inventario.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_agregar_inventario))
        self.btn_eliminar_inventario.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_credenciales_eliminar))
        self.btn_editar_inventario.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_credenciales_editar))
        self.btn_anadir_gasto.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_agregar_gasto))

        # Boton Credenciales
        self.btn_validar_contrasena_editar.clicked.connect(
            lambda: self.validacion_de_credenciales_editar())
        self.btn_validar_contrasena_eliminar.clicked.connect(
            lambda: self.validacion_de_credenciales_eliminar())
        self.btn_validar_contrasena_eliminar_temperatura.clicked.connect(
            lambda: self.validacion_de_credenciales_eliminar_temperatura())
        self.btn_validar_contrasena_corte.clicked.connect(
            lambda: self.validacion_de_credenciales_corte())

        # Botones de Funcionalidades de CRUD Inventario
        self.btn_agregar_producto.clicked.connect(
            lambda: self.agregarProductoABaseDeDatos())
        self.btn_agregar_producto_7.clicked.connect(
            lambda: self.actualizarProducto())
        self.tabla_inventario.cellClicked.connect(self.celda_clicada)
        self.tabla_temperaturas.cellClicked.connect(
            self.celda_clicada_tabla_temperaturas)

        # Botones de Funcionalidades de CRUD Corte de Caja
        self.btn_agregar_gasto.clicked.connect(
            lambda: self.agregarGastoABaseDeDatos())
        self.btn_generar_corte.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_resultado_corte))
        self.btn_agregar_montos.clicked.connect(
            lambda: self.agregarMontosATemporal())
        self.btn_mostrar_corte.clicked.connect(
            lambda: self.abrirPDFCorte())

        # Botones de Funcionalidades de Ventas
        self.lineEdit_busqueda_ventas.textChanged.connect(
            lambda: self.actualizarResultadosBusqueda())
        self.lineEdit_busqueda_ticket.textChanged.connect(
            lambda: self.actualizarResultadosTicket())
        self.tabla_ventas.cellClicked.connect(self.agregarProductoACarrito)
        self.tabla_carrito.cellClicked.connect(
            self.seleccionarProductoDeCarrito)
        self.btn_realizar_venta.clicked.connect(
            lambda: self.realizarVentaDeCarrito())
        self.btn_buscar_ticket.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_busqueda_ticket))
        self.btn_regresar_ventas.clicked.connect(
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_ventas))
        # Funcion para actualizar el comboBox de agregar productos

        self.comboBox.currentIndexChanged.connect(
            lambda: self.actualizarComboBoxAgregarProducto())

        # Funcion para actualizar el comboBox de editar productos

        self.comboBox_13.currentIndexChanged.connect(
            lambda: self.actualizarComboBoxEditarProducto())

        # Botón de conversión de temperaturas

        self.btn_convertir_temperaturas.clicked.connect(
            lambda: self.convertirTablaTemperaturas()
        )

    # validacion de credenciales
    def validacion_de_credenciales_editar(self):
        contrasena = self.lbl_contrasena_editar.text()
        if contrasena == '123':
            self.lbl_contrasena_editar.setText("")
            self.stackedWidget_menu.setCurrentWidget(
                self.page_editar_inventario)
            self.lineEdit_26.setText(self.lbl_nombre.text())
            self.lineEdit_27.setText(self.lbl_descripcion.text())
            self.lineEdit_28.setText(self.lbl_precio.text())
            self.lineEdit_25.setText(self.lbl_cantidad.text().rstrip(" kg.").rstrip(" c/u"))
            self.comboBox_13.setCurrentText(self.lbl_categoria.text())
            self.comboBox_14.setCurrentText(self.lbl_subcategoria.text())
        else:
            self.lbl_contrasena_editar.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_inventario)

    def validacion_de_credenciales_eliminar(self):
        contrasena = self.lbl_contrasena_eliminar.text()
        if contrasena == '123':
            self.lbl_contrasena_eliminar.setText("")
            # en esta linea se realizara la eliminacion
            self.borrarProductoDeBaseDeDatos()
        else:
            self.lbl_contrasena_eliminar.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_inventario)

    def validacion_de_credenciales_eliminar_temperatura(self):
        contrasena = self.lbl_contrasena_eliminar_temperatura.text()
        if contrasena == '123':
            # en esta linea se realizara la eliminacion de la temperatura
            com = Comunicacion()
            com.eliminarTemperatura(self.tabla_temperaturas.item(
                self.tabla_temperaturas.currentRow(), 0).text())
            self.lbl_contrasena_eliminar_temperatura.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_temperaturas)
            self.actualizarTablaTemperaturas()
        else:
            self.lbl_contrasena_eliminar_temperatura.setText("")
            messagebox.showwarning(
                'ERROR DE CREDENCIALES', 'La contraseña no coincide con las de permiso para acceder a esta área.')
            self.stackedWidget_menu.setCurrentWidget(self.page_temperaturas)

    def validacion_de_credenciales_corte(self):
        contrasena = self.lbl_contrasena_corte.text()
        if contrasena == '123':
            self.stackedWidget_menu.setCurrentWidget(self.page_agregar_montos)
            self.lbl_contrasena_corte.setText("")

        else:
            self.lbl_contrasena_corte.setText("")
            messagebox.showwarning(
                'ERROR DE CREDENCIALES', 'La contraseña no coincide con las de permiso para acceder a esta área.')
            self.stackedWidget_menu.setCurrentWidget(self.page_corte_de_caja)

    def actualizarTemperatura(self):
        # Leer los datos que manda el Arduino
        datosCelsius = arduino.readline()
        datosFahrenheit = arduino.readline()
        datosHumedad = arduino.readline()

        strCelsius = str(datosCelsius.decode('utf-8'))
        strFahrenheit = str(datosFahrenheit.decode('utf-8'))
        strHumedad = str(datosHumedad.decode('utf-8'))

        if self.comboBox_temperaturas.currentIndex() == 0:  # Caso grados Celsius
            self.lbl_temperatura_actual.setText(
                "\n" + str(strCelsius))
        elif self.comboBox_temperaturas.currentIndex() == 1:  # Caso grados fahrenheit
            self.lbl_temperatura_actual.setText(
                "\n" + str(strFahrenheit))
        else:  # Caso humedad
            self.lbl_temperatura_actual.setText(
                "\n" + str(strHumedad))

        com = Comunicacion()
        fecha = self.obtenerFechaActual()

        if com.verificarFechaTemperaturas(fecha) is None:
            if (com.verificacionCorteEnBase(fecha)):
                if strCelsius.strip() != "Error en el sensor!" and strFahrenheit.strip() != "Error en el sensor!" and strHumedad.strip() != "Error en el sensor!":
                    if (os.path.isfile(pathTemperatura + nombreArchivo)):
                        # Abre el archivo si ya existe
                        archivo = open(pathTemperatura + nombreArchivo, "a")
                    else:
                        # Crea el archivo si no existe
                        archivo = open(pathTemperatura + nombreArchivo, "x")

                    # Escribe la temperatura en el archivo txt creado
                    archivo.write(str(datosCelsius.decode('utf-8')).strip() + "\n")
                    archivo.close()

    def convertirTablaTemperaturas(self):
        if self.tabla_temperaturas.rowCount() > 0:
            com = Comunicacion()

            lista = com.verificarUnidadesTemperatura()
            string = ','.join([str(i) for i in lista])
            string = string.replace('(', '').replace(')', '').replace(',', '')

            if float(string) == float(self.tabla_temperaturas.item(0, 1).text()):
                self.conversionTemperaturas(1)
                self.btn_convertir_temperaturas.setText("Cambiar unidad a °C")
            else:
                self.conversionTemperaturas(2)
                self.btn_convertir_temperaturas.setText("Cambiar unidad a °F")

    def conversionTemperaturas(self, boolean):
        for i in range(1, 4):
            for j in range(0, self.tabla_temperaturas.rowCount()):
                temperaturaAConvertir = float(
                    self.tabla_temperaturas.item(j, i).text())
                if boolean == 1:
                    temperaturaAConvertir = (temperaturaAConvertir * (9/5)) + 32
                else:
                    temperaturaAConvertir = (temperaturaAConvertir - 32)*(5/9)
                temperaturaAConvertir = round(temperaturaAConvertir, 1)
                item = QtWidgets.QTableWidgetItem(str(temperaturaAConvertir))
                self.tabla_temperaturas.setItem(j, i, item)

    # Funcionalidad botones barra superior
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width == 0:
                extender = 300
            else:
                extender = normal
            self.animacion = QPropertyAnimation(
                self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animacion.start()

    def control_btn_minimizar(self):
        self.showMinimized()

    def control_btn_pestana(self):
        self.showNormal()
        self.btn_pestana.hide()
        self.btn_maximizar.show()

    def control_btn_maximizar(self):
        self.showMaximized()
        self.btn_pestana.show()
        self.btn_maximizar.hide()

    def control_btn_Minimizar(self):
        self.showMinimized()

    # mover ventana

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == Qt.MouseButton.LeftButton:
                self.move(
                    self.pos() + event.globalPosition().toPoint() - self.clickPosition)
                self.clickPosition = event.globalPosition().toPoint()

        if event.globalPosition().toPoint().y() <= 20:
            self.control_btn_maximizar()
        else:
            self.control_btn_pestana()

    # funcionalides de CRUD de inventario

    def agregarProductoABaseDeDatos(self):
        if((self.comboBox.currentText()=="Carne") or (self.comboBox.currentText()=="Despensa" and (self.comboBox_2.currentText()=="Fruta" or self.comboBox_2.currentText()=="Verdura"))):
            productoEsFlotante=True
        else:
            productoEsFlotante=False
        validoNombre=self.validarNombre(self.lineEdit.text(),self.lbl_error_nombre_agregar)
        validoDescripcion=self.validarDescripcion(self.lineEdit_2.text(),self.lbl_error_descripcion_agregar) 
        if(productoEsFlotante):
            validoCantidad=self.validarCantidadFlotante(self.lineEdit_3.text(),self.lbl_error_cantidad_agregar)
        else:
            validoCantidad=self.validarCantidadEntero(self.lineEdit_3.text(),self.lbl_error_cantidad_agregar)
        validoPrecio=self.validarPrecio(self.lineEdit_4.text(), self.lbl_error_precio_agregar)
        if(validoNombre and validoDescripcion and validoCantidad and validoPrecio):
            producto = Producto(self.lineEdit.text(), self.lineEdit_2.text(),
                                self.comboBox.currentText(), self.comboBox_2.currentText(),
                                self.lineEdit_4.text(), self.lineEdit_3.text())
            com = Comunicacion()
            com.insertarProducto(producto)
            self.borrarCamposInventarioAgregar()
            self.actualizarTablaInventario()
            self.limpiarErroresAgregar()

    def actualizarTablaInventario(self):
        com = Comunicacion()
        resultados = com.traerProductos()
        self.tabla_inventario.setRowCount(0)
        self.tabla_inventario.setRowCount(len(resultados))

        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                if columna == 6: # Verificar si estamos en la columna que contiene la información que nos interesa
                    if resultados[fila][3] == 'Carne' or (resultados[fila][3] == 'Despensa' and (resultados[fila][4]=="Fruta" or resultados[fila][4]=="Verdura")):
                        # Si el valor es 'carne', establecer el texto como número flotante con la leyenda 'kg'
                        item = QtWidgets.QTableWidgetItem(f"{float(valor):.2f} kg.")
                    elif resultados[fila][3] == 'Despensa':
                        # Si el valor es 'despensa', establecer el texto como 'c/u'
                        item = QtWidgets.QTableWidgetItem(f"{float(valor):.0f} c/u")
                    else:
                        # Manejar otros casos si es necesario
                        item = QtWidgets.QTableWidgetItem(str(valor))
                elif columna ==5:
                    item = QtWidgets.QTableWidgetItem(f"{float(valor):.2f}")
                else:
                    # Para otras columnas, simplemente establecer el valor como texto
                    item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_inventario.setItem(fila, columna, item)

        self.stackedWidget_menu.setCurrentWidget(self.page_inventario)

    def actualizarProducto(self):
        if(self.comboBox_13.currentText()=="Carne" or (self.comboBox_13.currentText()=="Despensa" and (self.comboBox_14.currentText()=="Fruta" or self.comboBox_14.currentText()=="Verdura"))):
            productoEsFlotante=True
        else:
            productoEsFlotante=False
        validoNombre=self.validarNombre(self.lineEdit_26.text(),self.lbl_error_nombre_agregar)
        validoDescripcion=self.validarDescripcion(self.lineEdit_27.text(),self.lbl_error_descripcion_editar) 
        if(productoEsFlotante):
            validoCantidad=self.validarCantidadFlotante(self.lineEdit_25.text(),self.lbl_error_cantidad_editar)
        else:
            validoCantidad=self.validarCantidadEntero(self.lineEdit_25.text(),self.lbl_error_cantidad_editar)
        validoPrecio=self.validarPrecio(self.lineEdit_28.text(), self.lbl_error_precio_editar)
        if(validoNombre and validoDescripcion and validoCantidad and validoPrecio):
            producto = Producto(self.lineEdit_26.text(), self.lineEdit_27.text(),
                                self.comboBox_13.currentText(), self.comboBox_14.currentText(),
                                self.lineEdit_28.text(), self.lineEdit_25.text())
            com = Comunicacion()
            com.editarProducto(producto, self.lbl_id.text())
            self.actualizarTablaInventario()
            self.limpiarErroresEditar()

    def borrarProductoDeBaseDeDatos(self):
        com = Comunicacion()
        com.eliminarProducto(self.lbl_id.text())
        self.actualizarTablaInventario()

    def celda_clicada(self, fila, columna):
        # Acción específica cuando una celda se hace clic
        if columna == 0:  # si es la columna de id nos lleva a mostrar el producto
            self.stackedWidget_menu.setCurrentWidget(
                self.page_mostrar_seleccion)
            self.lbl_id.setText(
                self.tabla_inventario.item(fila, columna+0).text())
            self.lbl_nombre.setText(
                self.tabla_inventario.item(fila, columna+1).text())
            self.lbl_descripcion.setText(
                self.tabla_inventario.item(fila, columna+2).text())
            self.lbl_categoria.setText(
                self.tabla_inventario.item(fila, columna+3).text())
            self.lbl_subcategoria.setText(
                self.tabla_inventario.item(fila, columna+4).text())
            self.lbl_precio.setText(
                self.tabla_inventario.item(fila, columna+5).text())
            self.lbl_cantidad.setText(
                self.tabla_inventario.item(fila, columna+6).text())

    # Funciones Corte de Caja
    def agregarGastoABaseDeDatos(self):
        fecha_actual_str = self.obtenerFechaActual()
        gasto = Gasto(self.lineEdit_concepto_gasto.text(),
                      self.lineEdit_monto_gasto.text(), fecha_actual_str)
        com = Comunicacion()
        com.insertarGasto(gasto)
        self.borrarCamposGastosAgregar()
        self.stackedWidget_menu.setCurrentWidget(self.page_corte_de_caja)
        self.actualizarTablaGastos()

    def obtenerFechaActual(self):
        fecha_actual = date.today()
        fecha_actual_str = fecha_actual.strftime('%Y-%m-%d')
        return fecha_actual_str

    def actualizarTablaGastos(self):
        com = Comunicacion()
        resultados = com.traerGastos()
        self.tabla_gastos.setRowCount(0)
        self.tabla_gastos.setRowCount(len(resultados))

        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_gastos.setItem(fila, columna, item)

    def guardarTemporalMontos(self, monto50c, monto1, monto2, monto5, monto10, monto20, monto50, monto100, monto200, monto500):
        # Crear un archivo temporal
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            # Escribir los valores en el archivo
            temp_file.write(
                f"{monto50c}\n{monto1}\n{monto2}\n{monto5}\n{monto10}\n{monto20}\n{monto50}\n{monto100}\n{monto200}\n{monto500}")

        # Obtener la ruta del archivo temporal
            temp_file_path = temp_file.name
        return temp_file_path

    def leerTemporalMontos(self, archivo_temporal):
        # Leer los valores desde el archivo temporal
        with open(archivo_temporal, 'r') as temp_file:
            lineas = temp_file.readlines()
        # Obtener los montos desde el archivo
            monto50c = float(lineas[0].strip())
            monto1 = float(lineas[1].strip())
            monto2 = float(lineas[2].strip())
            monto5 = float(lineas[3].strip())
            monto10 = float(lineas[4].strip())
            monto20 = float(lineas[5].strip())
            monto50 = float(lineas[6].strip())
            monto100 = float(lineas[7].strip())
            monto200 = float(lineas[8].strip())
            monto500 = float(lineas[9].strip())
        # Sumatoria total de los montos en caja
        efectivoTotalCaja = monto50c+monto1+monto2+monto5 + \
            monto10+monto20+monto50+monto100+monto200+monto500

        return efectivoTotalCaja

    def agregarMontosATemporal(self):

        monto500 = self.spinBox_monto_500.value()
        monto200 = self.spinBox_monto_200.value()
        monto100 = self.spinBox_monto_100.value()
        monto50 = self.spinBox_monto_50.value()
        monto20 = self.spinBox_monto_20.value()
        monto10 = self.spinBox_monto_10.value()
        monto5 = self.spinBox_monto_5.value()
        monto2 = self.spinBox_monto_2.value()
        monto1 = self.spinBox_monto_1.value()
        monto50c = self.spinBox_monto_50c.value()

        efectivoTotalCaja = self.leerTemporalMontos(self.guardarTemporalMontos(
            monto50c, monto1, monto2, monto5, monto10, monto20, monto50, monto100, monto200, monto500))
        self.borrarCamposMontosAgregar()
        self.generarReporteTemperaturas()
        self.generar_pdf_corte(efectivoTotalCaja)

    def verificarExistenciaCorte(self):
        validacion = False
        ruta_archivo = 'Documentos\Reportes Corte de caja\cortedecaja_' + \
            self.obtenerFechaActual() + '.pdf'
        if os.path.exists(ruta_archivo):
            validacion = True
        else:
            validacion = False
        return validacion

    def agregarCorteABaseDeDatos(self, efectivoTotalCaja):
        com = Comunicacion()
        sumaGastos = com.sumaGastos(self.obtenerFechaActual())
        ventaBase = com.sumaVentas(self.obtenerFechaActual())
        fecha = self.obtenerFechaActual()
        gananciaDia = ventaBase - sumaGastos
        com.insertarCorte(gananciaDia, fecha, efectivoTotalCaja)

    def generar_pdf_corte(self, efectivoTotalCaja):
        com = Comunicacion()
        fecha = self.obtenerFechaActual()
        validacion = 0
        # validacion = com.verificacionCorteEnBase(fecha)
        # print("Verificacion",com.verificacionCorteEnBase(fecha))
        # com.verificacionCorteEnBase(fecha)
        if not self.verificarExistenciaCorte():
            if (com.verificacionCorteEnBase(fecha)):
                cam = Comunicacion()
                self.agregarCorteABaseDeDatos(efectivoTotalCaja)
                gastos = cam.sumaGastos(fecha)
                venta = cam.sumaVentas(fecha)
                gananciaDia = venta - gastos
                tempMin = cam.traerTemperaturaMin(fecha)
                tempMax = cam.traerTemperaturaMax(fecha)
                tempProm = cam.traerTemperaturaProm(fecha)
                idcorte = cam.traerIDCorte(fecha)
                template_loader = jinja2.FileSystemLoader('./')
                template_env = jinja2.Environment(loader=template_loader)

                html_template = 'corte_caja_plantilla.html'
                template = template_env.get_template(html_template)
                # Insertar datos de Corte de caja
                output_text = template.render({"today_date": fecha, "num_corte": idcorte, "subtotal_gastos": gastos, "subtotal_montos": efectivoTotalCaja,
                                               "totalVentas": venta, "subtotal_venta": venta, "totalGanancias": gananciaDia,
                                               "minTemp": tempMin, "maxTemp": tempMax, "promTemp": tempProm})
                option = {'page-size': 'Legal',
                          'margin-top': '0.05in',
                          'margin-left': '0.05in',
                          'margin-right': '0.05in',
                          'margin-bottom': '0.05in',
                          'encoding': 'UTF-8'}

                config = pdfkit.configuration(
                    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
                fechaReportePDF = 'cortedecaja_' + self.obtenerFechaActual() + '.pdf'
                ruta_salida = 'Documentos/Reportes Corte de caja/'+fechaReportePDF
                pdfkit.from_string(
                    output_text, ruta_salida, css='estilos.css', options=option, configuration=config)
                self.stackedWidget_menu.setCurrentWidget(
                    self.page_corte_de_caja)
            else:
                self.desbloquearPrograma(False)
                messagebox.showwarning('CORTE DE CAJA EXISTENTE EN BASE DE DATOS',
                                       'Se ha generado un corte de caja con la fecha del día actual, verifique el documento')
                self.desbloquearPrograma(True)
                self.stackedWidget_menu.setCurrentWidget(
                    self.page_corte_de_caja)
        else:
            self.desbloquearPrograma(False)
            messagebox.showwarning(
                'CORTE DE CAJA EXISTENTE', 'Se ha generado un corte de caja con la fecha del día actual, verifique el documento')
            self.desbloquearPrograma(True)
            self.stackedWidget_menu.setCurrentWidget(self.page_corte_de_caja)

    def abrirPDFCorte(self):
        if self.verificarExistenciaCorte():
            ruta_archivo = 'Documentos\Reportes Corte de caja\cortedecaja_' + \
                self.obtenerFechaActual() + '.pdf'
            ruta_absoluta = os.path.abspath(ruta_archivo)
            webbrowser.open('file://' + ruta_absoluta)
        else:
            self.desbloquearPrograma(False)
            messagebox.showwarning(
                'CORTE DE CAJA INEXISTENTE', 'No se ha generado aun un corte el día actual, intente generar uno previamente')
            self.desbloquearPrograma(True)

    # Funcionalidades Temperaturas
    def generarReporteTemperaturas(self):
        com = Comunicacion()
        if com.verificacionCorteEnBase(self.obtenerFechaActual()):
            archivo = open(pathTemperatura + nombreArchivo, "r")
            lista = archivo.readlines()

            for i in range(0, len(lista)):
                lista[i] = float(lista[i].strip())

            lista.sort()

            temperaturaMin = lista[0]
            temperaturaMax = lista[len(lista)-1]
            temperaturaPromedio = sum(lista)/len(lista)

            archivo.close()

            com = Comunicacion()
            com.insertarTemperatura(self.obtenerFechaActual(), round(
                temperaturaPromedio, 1), temperaturaMax, temperaturaMin)

            os.remove(pathTemperatura + nombreArchivo)

            self.actualizarTablaTemperaturas()

    def celda_clicada_tabla_temperaturas(self, fila, columna):
        # Acción específica cuando una celda se hace clic
        if columna == 5:  # si es la columna de borrado nos lleva a la insercion de contraseña
            self.stackedWidget_menu.setCurrentWidget(
                self.page_credenciales_eliminar_temperatura)

    def actualizarTablaTemperaturas(self):
        com = Comunicacion()
        resultados = com.traerTemperaturas()
        self.tabla_temperaturas.setRowCount(0)
        self.tabla_temperaturas.setRowCount(len(resultados))

        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                itemEliminar = QtWidgets.QTableWidgetItem("Eliminar")
                self.tabla_temperaturas.setItem(fila, columna, item)
                self.tabla_temperaturas.setItem(fila, 5, itemEliminar)

    # funcionalidades de borrado de campos

    def borrarCamposInventarioAgregar(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(1)

    def borrarCamposGastosAgregar(self):
        self.lineEdit_concepto_gasto.setText("")
        self.lineEdit_monto_gasto.setText("")

    def borrarCamposMontosAgregar(self):
        self.spinBox_monto_500.setValue(0)
        self.spinBox_monto_200.setValue(0)
        self.spinBox_monto_100.setValue(0)
        self.spinBox_monto_50.setValue(0)
        self.spinBox_monto_20.setValue(0)
        self.spinBox_monto_10.setValue(0)
        self.spinBox_monto_5.setValue(0)
        self.spinBox_monto_2.setValue(0)
        self.spinBox_monto_1.setValue(0)
        self.spinBox_monto_50c.setValue(0)

    # Funcionalidades Temperaturas

    # funcionalidades para actualizar ComboBox

    def actualizarComboBoxAgregarProducto(self):
        # Limpia el segundo ComboBox
        self.comboBox_2.clear()

        # Obtiene la selección del primer ComboBox
        seleccion = self.comboBox.currentText()

        # Llena el segundo ComboBox basado en la selección del primero
        if seleccion == "Carne":
            self.comboBox_2.addItem("Pollo")
            self.comboBox_2.addItem("Res")
            self.comboBox_2.addItem("Cerdo")
            self.comboBox_2.addItem("Pescado")
        else:
            self.comboBox_2.addItem("Fruta")
            self.comboBox_2.addItem("Verdura")
            self.comboBox_2.addItem("Abarrote")
            self.comboBox_2.addItem("Limpieza")
            self.comboBox_2.addItem("Cremería")

    def actualizarComboBoxEditarProducto(self):
        # Limpia el segundo ComboBox
        self.comboBox_14.clear()

        # Obtiene la selección del primer ComboBox
        seleccion = self.comboBox_13.currentText()

        # Llena el segundo ComboBox basado en la selección del primero
        if seleccion == "Carne":
            self.comboBox_14.addItem("Pollo")
            self.comboBox_14.addItem("Res")
            self.comboBox_14.addItem("Cerdo")
            self.comboBox_14.addItem("Pescado")
        else:
            self.comboBox_14.addItem("Fruta")
            self.comboBox_14.addItem("Verdura")
            self.comboBox_14.addItem("Abarrote")
            self.comboBox_14.addItem("Limpieza")
            self.comboBox_14.addItem("Cremería")

    # Funciones del apartado Ventas
    def actualizarResultadosBusqueda(self):
        com = Comunicacion()
        resultados = com.traerProductosVentas(
            self.lineEdit_busqueda_ventas.text())
        self.tabla_ventas.setRowCount(0)
        self.tabla_ventas.setRowCount(len(resultados))

        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                if columna == 2: # Verificar si estamos en la columna que contiene la información que nos interesa
                    if resultados[fila][4] == 'Carne' or (resultados[fila][4] == 'Despensa' and (resultados[fila][5]=="Fruta" or resultados[fila][5]=="Verdura")):
                        # Si el valor es 'carne', establecer el texto como número flotante con la leyenda 'kg'
                        item = QtWidgets.QTableWidgetItem(f"{float(valor):.2f} kg.")
                    elif resultados[fila][4] == 'Despensa':
                        # Si el valor es 'despensa', establecer el texto como 'c/u'
                        item = QtWidgets.QTableWidgetItem(f"{float(valor):.0f} c/u")
                    else:
                        # Manejar otros casos si es necesario
                        item = QtWidgets.QTableWidgetItem(str(valor))
                elif columna ==3:
                    item = QtWidgets.QTableWidgetItem(f"{float(valor):.2f}")
                else:
                    # Para otras columnas, simplemente establecer el valor como texto
                    item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_ventas.setItem(fila, columna, item)

    

    def actualizarResultadosTicket(self):
        com = Comunicacion()
        resultados = com.traerVentasDeTicket(
            self.lineEdit_busqueda_ticket.text())
        self.tabla_busqueda_ticket.setRowCount(0)
        self.tabla_busqueda_ticket.setRowCount(len(resultados))
        totalDeVenta=0
        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                if columna == 2: # Verificar si estamos en la columna que contiene la información que nos interesa
                    if resultados[fila][5] == 'Carne' or (resultados[fila][5] == 'Despensa' and (resultados[fila][6]=="Fruta" or resultados[fila][6]=="Verdura")):
                        # Si el valor es 'carne', establecer el texto como número flotante con la leyenda 'kg'
                        item = QtWidgets.QTableWidgetItem(f"{float(valor):.2f} kg.")
                    elif resultados[fila][5] == 'Despensa':
                        # Si el valor es 'despensa', establecer el texto como 'c/u'
                        item = QtWidgets.QTableWidgetItem(f"{float(valor):.0f} c/u")
                    else:
                        # Manejar otros casos si es necesario
                        item = QtWidgets.QTableWidgetItem(str(valor))
                elif columna == 3:
                    item = QtWidgets.QTableWidgetItem(f"{float(valor):.2f}")
                else:
                    # Para otras columnas, simplemente establecer el valor como texto
                    item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_busqueda_ticket.setItem(fila, columna, item)
        
        for fila in range(self.tabla_busqueda_ticket.rowCount()):
            totalDeVenta += float(self.tabla_busqueda_ticket.item(fila, 3).text())
        if(totalDeVenta!=0):
            self.label_21.setText(f"Total de Venta: {float(totalDeVenta):.2f}")
        else:
            self.label_21.setText("")
        
    def actualizarGraficaVentas(self):
        self.grafica1 = Canvas_grafica_ventas()
        while self.grafica_ventas.count():
            widget = self.grafica_ventas.takeAt(0)
            if widget.widget():
                widget.widget().deleteLater()

        self.grafica_ventas.addWidget(self.grafica1)

    def actualizarGraficaGastos(self):
        self.grafica2 = Canvas_grafica_gastos()
        while self.grafica_gastos.count():
            widget = self.grafica_gastos.takeAt(0)
            if widget.widget():
                widget.widget().deleteLater()

        self.grafica_gastos.addWidget(self.grafica2)

    def actualizarGraficaProductos(self):
        self.grafica3 = Canvas_grafica_productos(
            self.lineEdit_grafica_productos.text())
        while self.grafica_productos.count():
            widget = self.grafica_productos.takeAt(0)
            if widget.widget():
                widget.widget().deleteLater()

        self.grafica_productos.addWidget(self.grafica3)
    
    def dirigirseAPestaniaVentas(self):
        self.stackedWidget_menu.setCurrentWidget(self.page_grafica_ventas)
        self.actualizarGraficaVentas()
    
    def dirigirseAPestaniaGastos(self):
        self.stackedWidget_menu.setCurrentWidget(self.page_grafica_gastos)
        self.actualizarGraficaGastos()

    def dirigirseAPestaniaProducto(self):
        self.stackedWidget_menu.setCurrentWidget(self.page_grafica_producto)
        self.actualizarGraficaProductos()

    def desbloquearPrograma(self, booleano):
        self.frame_control.setEnabled(booleano)
        self.frame_contenido.setEnabled(booleano)
        self.frame_superior.setEnabled(booleano)

    def agregarProductoACarrito(self, fila, columna):
        valor = self.tabla_ventas.item(fila, columna).text()
        try:
            self.desbloquearPrograma(False)
            cantidadProducto = askstring(
                'CANTIDAD DEL PRODUCTO', 'Proporcione la cantidad del producto a agregar al carrito:')
            self.desbloquearPrograma(True)

            # Vamos a verificar que en la tabla haya otro producto para agregarlo ahi mismo o denegar la venta por exceso de stock
            filaConProductoExistenteEnCarrito = self.verificarProductoExistenteEnCarrito(
                self.tabla_ventas.item(fila, 0).text())
            com = Comunicacion()
            resultadoCategoria=com.traerCategoriaDeProductos(self.tabla_ventas.item(fila, 0).text())
            productoSeRegistraEnKilogramos=False
            if(resultadoCategoria[0][0] == 'Carne' or (resultadoCategoria[0][0] == 'Despensa' and (resultadoCategoria[0][1]=="Fruta" or resultadoCategoria[0][1]=="Verdura"))):
                valorCantidadProducto=float(cantidadProducto)
                productoSeRegistraEnKilogramos=True
            else:
                valorCantidadProducto=int(cantidadProducto)
            cantidadExistenteEnCarrito = self.obtenerValorDeCantidadEnCarrito(
                filaConProductoExistenteEnCarrito)
            # Verificamos el producto
            if (float(valorCantidadProducto) > 0.0 and (float(valorCantidadProducto)+float(cantidadExistenteEnCarrito)) <= float(self.tabla_ventas.item(fila, 2).text().rstrip(" kg.").rstrip(" c/u"))):
                # Verificamos si ya existe el producto en la tabla de venta
                if (filaConProductoExistenteEnCarrito != -1):
                    # Vamos a modificar
                    cantidadTotalProducto = float(
                        cantidadProducto)+float(cantidadExistenteEnCarrito)
                    if(productoSeRegistraEnKilogramos):
                        itemCantidad = QtWidgets.QTableWidgetItem(f"{float(cantidadTotalProducto):.2f} kg.")
                    else:
                        itemCantidad = QtWidgets.QTableWidgetItem(f"{float(cantidadTotalProducto):.0f} c/u")
                    itemPrecio = QtWidgets.QTableWidgetItem(
                        str(float(cantidadTotalProducto)*float(self.tabla_ventas.item(fila, 3).text())))
                    self.tabla_carrito.setItem(
                        filaConProductoExistenteEnCarrito, 2, itemCantidad)
                    self.tabla_carrito.setItem(
                        filaConProductoExistenteEnCarrito, 3, itemPrecio)
                else:
                    # Movemos a la tabla en dado caso de que no encontro coincidencia
                    rowPosition = self.tabla_carrito.rowCount()
                    self.tabla_carrito.insertRow(rowPosition)
                    itemId = QtWidgets.QTableWidgetItem(
                        self.tabla_ventas.item(fila, 0).text())
                    itemNombre = QtWidgets.QTableWidgetItem(
                        self.tabla_ventas.item(fila, 1).text())
                    if(productoSeRegistraEnKilogramos):
                        itemCantidad = QtWidgets.QTableWidgetItem(f"{float(cantidadProducto):.2f} kg.")
                    else:
                        itemCantidad = QtWidgets.QTableWidgetItem(f"{float(cantidadProducto):.0f} c/u")
                    itemPrecio = QtWidgets.QTableWidgetItem(
                        str(float(cantidadProducto)*float(self.tabla_ventas.item(fila, 3).text())))
                    itemEliminar = QtWidgets.QTableWidgetItem("Eliminar")
                    self.tabla_carrito.setItem(rowPosition, 0, itemId)
                    self.tabla_carrito.setItem(rowPosition, 1, itemNombre)
                    self.tabla_carrito.setItem(rowPosition, 2, itemCantidad)
                    self.tabla_carrito.setItem(rowPosition, 3, itemPrecio)
                    self.tabla_carrito.setItem(rowPosition, 4, itemEliminar)

            else:
                messagebox.showwarning(
                    'NUMERO INVÁLIDO', 'El numero proporcionado no fue válido o excede la cantidad de producto en el inventario...')
        except:
            self.desbloquearPrograma(True)
            messagebox.showwarning(
                'PROCESO INTERRUMPIDO', 'El proceso fue cancelado o fallo durante la ejecución, de igual manera puede haber ingresado un valor no válido...')

    def verificarProductoExistenteEnCarrito(self, idBuscar):
        for fila in range(self.tabla_carrito.rowCount()):
            #print(self.tabla_carrito.item(fila, 1).text() + idBuscar + self.tabla_carrito.item(fila, 0).text())
            if (idBuscar in self.tabla_carrito.item(fila, 0).text()):
                # regresamos la fila pues el id ya existe
                return fila
        # regresamos -1 como dato que no lo encontro
        return -1

    def obtenerValorDeCantidadEnCarrito(self, fila):
        if (fila == -1):
            return 0
        else:
            return self.tabla_carrito.item(fila, 2).text().rstrip(" kg.").rstrip(" c/u")

    def seleccionarProductoDeCarrito(self, fila, columna):
        filaSeleccionada = self.tabla_carrito.currentRow()
        # Eliminar la fila seleccionada
        if (columna == 4 and filaSeleccionada >= 0):
            try:
                respuesta = messagebox.askokcancel(
                    'ELIMINAR PRODUCTO DEL CARRITO', '¿Desea borrar el elemento seleccionado de la venta?')
                self.desbloquearPrograma(False)
                if (respuesta == 1):
                    self.tabla_carrito.removeRow(filaSeleccionada)
                else:
                    messagebox.showInfo(
                        'ELIMINAR PRODUCTO DEL CARRITO', 'El elemento seguirá en el carrito de ventas')
                self.desbloquearPrograma(True)
            except:
                self.desbloquearPrograma(True)
                messagebox.showwarning(
                    'PROCESO INTERRUMPIDO', 'El proceso fue cancelado o fallo durante la ejecución...')
        # Modificar la fila seleccionada
        elif (columna == 2):
            try:
                self.desbloquearPrograma(False)
                cantidadProducto = askstring(
                    'CANTIDAD DEL PRODUCTO', 'Proporcione la cantidad del producto a modificar al carrito:')
                self.desbloquearPrograma(True)
                # Verificamos el producto
                com = Comunicacion()
                resultadoCantidad = com.traerCantidadDeProductoVentas(
                    self.tabla_carrito.item(fila, 0).text())
                resultadosPrecio = com.traerPrecioDeProductoVentas(
                    self.tabla_carrito.item(fila, 0).text())
                resultadoCategoria=com.traerCategoriaDeProductos(self.tabla_carrito.item(fila, 0).text())
                productoSeRegistraEnKilogramos=False
                if(resultadoCategoria[0][0] == 'Carne' or (resultadoCategoria[0][0] == 'Despensa' and (resultadoCategoria[0][1]=="Fruta" or resultadoCategoria[0][1]=="Verdura"))):
                    valorCantidadProducto=float(cantidadProducto)
                    productoSeRegistraEnKilogramos=True
                else:
                    valorCantidadProducto=int(cantidadProducto)
                if (float(valorCantidadProducto) > 0.0 and float(valorCantidadProducto) <= float(resultadoCantidad[0])):
                    # Modificamos la cantidad del producto a la tabla en dado caso de que sea valido
                    # Cambiar esto con validación de número
                    if(productoSeRegistraEnKilogramos):
                        itemCantidad = QtWidgets.QTableWidgetItem(f"{float(valorCantidadProducto):.2f} kg.")
                    else:
                        itemCantidad = QtWidgets.QTableWidgetItem(f"{float(valorCantidadProducto):.0f} c/u")
                    itemPrecio = QtWidgets.QTableWidgetItem(
                        str(float(cantidadProducto)*float(resultadosPrecio[0])))
                    self.tabla_carrito.setItem(fila, 2, itemCantidad)
                    self.tabla_carrito.setItem(fila, 3, itemPrecio)
                else:
                    messagebox.showwarning(
                        'NUMERO INVÁLIDO', 'El numero proporcionado no fue válido o excede la cantidad de producto en el inventario...')
            except:
                self.desbloquearPrograma(True)
                messagebox.showwarning(
                    'PROCESO INTERRUMPIDO', 'El proceso fue cancelado o fallo durante la ejecución al ingresar datos inválidos...')

    def obtenerPrecioTotalDeCarrito(self):
        precioTotal = 0
        for fila in range(self.tabla_carrito.rowCount()):
            precioTotal += float(self.tabla_carrito.item(fila, 3).text())
        # regresamos el valor del precio total de las filas de la tabla del carrito
        return precioTotal

    def realizarVentaDeCarrito(self):
        if (self.tabla_carrito.rowCount() != 0):
            # Actualizar tabla de venta con id :D
            fecha_actual_str = self.obtenerFechaActual()
            precioTotal = self.obtenerPrecioTotalDeCarrito()
            ventaCarrito = Venta(fecha_actual_str, precioTotal)

            com = Comunicacion()
            com.insertarVenta(ventaCarrito)

            #imprimirTicket

            ticket = Ticket(self.obtenerProductosCarrito(), precioTotal, self.obtenerFechaActual())
            ticket.imprimirTicket(ticket.obtenerRuta())
            # Actualizar tabla de inventario_venta :D
            # Actualizar stock en inventario :D
            com = Comunicacion()
            ultimoID = com.traerUltimoIdDeVenta()
            self.insertarProductosEnVentasSeparadas(com, ultimoID)
            
            # Actualizar tablas :D
            self.actualizarTablaGastos()
            self.lineEdit_busqueda_ventas.setText("")
            self.actualizarResultadosBusqueda()
            self.tabla_carrito.setRowCount(0)
        else:
            messagebox.showwarning(
                'CARRITO VACIO', 'El carrito no cuenta con productos suficientes para una venta...')

    def obtenerProductosCarrito(self):
        num_filas = self.tabla_carrito.rowCount()
        num_columnas = self.tabla_carrito.columnCount()

        # Crear una lista para almacenar los valores de la tabla
        valores_tabla = []

        # Iterar sobre las celdas de la tabla y obtener los valores
        for fila in range(num_filas):
            fila_actual = []
            for columna in range(num_columnas):
                if columna == 2:
                    item = QtWidgets.QTableWidgetItem(self.tabla_carrito.item(fila, columna).text().replace(' kg.', '').replace(' c/u', ''))
                else:
                    item = self.tabla_carrito.item(fila, columna)
                if item is not None:
                    fila_actual.append(item.text())
                else:
                    fila_actual.append(None)
            valores_tabla.append(fila_actual)
        return valores_tabla

    def insertarProductosEnVentasSeparadas(self, com, ultimoIDVenta):
        for fila in range(self.tabla_carrito.rowCount()):
            # Pasamos los datos del carrito a la tabla de inventario_ventas, pasandole el id del producto y la cantidad
            com.insertarVentaInventario(ultimoIDVenta[0], int(self.tabla_carrito.item(
                fila, 0).text()), float(self.tabla_carrito.item(fila, 2).text().rstrip(" kg.").rstrip(" c/u")))
            # Ahora actualizaremos el stock con la venta que realizamos
            com.actualizarStockDeVenta(int(self.tabla_carrito.item(
                fila, 0).text()), float(self.tabla_carrito.item(fila, 2).text().rstrip(" kg.").rstrip(" c/u")))

    # Funciones para validar cadenas
    def limpiarErroresAgregar(self):
        self.lbl_error_nombre_agregar.setText("")
        self.lbl_error_descripcion_agregar.setText("")
        self.lbl_error_cantidad_agregar.setText("")
        self.lbl_error_precio_agregar.setText("")

    def limpiarErroresEditar(self):
        self.lbl_error_nombre_editar.setText("")
        self.lbl_error_descripcion_editar.setText("")
        self.lbl_error_cantidad_editar.setText("")
        self.lbl_error_precio_editar.setText("")

    def validarNombre(self, texto, lineEdit):
        patron = r'^.{1,100}$'
        if re.match(patron, texto):
            lineEdit.setText("")
            return True
        else:
            lineEdit.setText("El nombre debe tener minimo un caracter y un máximo de 100 caracteres...")
            return False
    
    def validarDescripcion(self, texto, lineEdit):
        patron = r'^.{1,100}$'
    
        if re.match(patron, texto):
            lineEdit.setText("")
            return True
        else:
            lineEdit.setText("La descripción debe tener minimo un caracter y un máximo de 100 caracteres...")
            return False
    
    def validarCantidadFlotante(self, texto, lineEdit):
        patron = r'^[1-9]\d*(\.\d+)?$'
    
        if re.match(patron, texto):
            lineEdit.setText("")
            return True
        else:
            lineEdit.setText("La cantidad del producto debe ser un valor númerico...")
            return False

    def validarCantidadEntero(self, texto, lineEdit):
        patron = r'^[1-9]\d*$'
    
        if re.match(patron, texto):
            lineEdit.setText("")
            return True
        else:
            lineEdit.setText("La cantidad del producto debe ser mayor 0, no debe contener puntos decimales y ser un valor númerico...")
            return False
    
    def validarPrecio(self, texto, lineEdit):
        patron = r'^\d+(\.\d{1,2})?$'
    
        if re.match(patron, texto):
            lineEdit.setText("")
            return True
        else:
            lineEdit.setText("El precio debe ser un valor númerico y contener un máximo de dos decimales...")
            return False

# Graficas


class Canvas_grafica_ventas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),
                                         sharey=True, facecolor='white')
        super().__init__(self.fig)
        com = Comunicacion()
        resultados = com.estadisticasVentas()
        
        colores = ['red', 'blue', 'green', 'black', 'yellow']
        fechas = [(fila[0].strftime('%Y-%m-%d')) for fila in resultados]
        cantidad_ventas = [fila[1] for fila in resultados]

        self.ax.bar(fechas, cantidad_ventas, color=colores)
        self.fig.suptitle('Ventas de los ultimos cinco dias', size=9)


class Canvas_grafica_productos(FigureCanvas):
    def __init__(self, texto, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),
                                         sharey=True, facecolor='white')
        super().__init__(self.fig)
        com = Comunicacion()
        resultados = com.estadisticasProductos(texto)

        colores = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
        fechas = [(fila[0].strftime('%Y-%m-%d')) for fila in resultados]
        cantidad_ventas = [fila[1] for fila in resultados]

        self.ax.bar(fechas, cantidad_ventas, color=colores)
        self.fig.suptitle('Ventas de los ultimos cinco dias', size=9)


class Canvas_grafica_gastos(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),
                                         sharey=True, facecolor='white')
        super().__init__(self.fig)

        com = Comunicacion()
        ingresosConsulta = com.estadisticasIngresos()
        gastosConsulta = com.estadisticasGastos()
        nombres_mes_espanol = [
            'N/A', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]
        nombreMes = nombres_mes_espanol[datetime.now().month]
    

        if((gastosConsulta!=0 and ingresosConsulta==0) or (ingresosConsulta!=0 and gastosConsulta==0) or (ingresosConsulta!=0 and gastosConsulta!=0)):
            colores = ['red', 'green',]
            
            nombres = [f"Gastos: {float(gastosConsulta):.2f}",
                    f"Ingresos: {float(ingresosConsulta):.2f}"]
            tamaño = [gastosConsulta, ingresosConsulta]
            explotar = [0.05, 0.05]

            plt.title("Ingresos y gastos del mes de " + nombreMes,
                    color='black', size=9, family="Arial")

            self.ax.pie(tamaño, explode=explotar, labels=nombres,
                        colors=colores,
                        autopct='%1.0f%%', pctdistance=0.3,
                        shadow=True, startangle=90, radius=0.8,
                        labeldistance=1.1)
            self.ax.axis('equal')
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
