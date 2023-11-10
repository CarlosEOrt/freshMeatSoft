import sys
import serial
import time
import datetime
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

from Producto import Producto
from Gasto import Gasto

from Comunicacion import Comunicacion


class MyWindow(QMainWindow):
    global arduino
    # arduino = serial.Serial('COM3', 9600)

    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('carniceria.ui', self)

        # Control al cargar interfaz
        self.control_btn_pestana()
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.actualizarTablaInventario()
        self.actualizarResultadosBusqueda()

        # self.timer = QTimer(self) # se crea una variable para constante actualizacion
        # self.timer.timeout.connect(lambda:self.actualizarTemperatura())#actualiza el label
        # self.timer.start(5000)#tiempo que tarda en el contador

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
        # self.btn_menu.clicked.connect()

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

        # Botones de Funcionalidades de CRUD Inventario
        self.btn_agregar_producto.clicked.connect(
            lambda: self.agregarProductoABaseDeDatos())
        self.btn_agregar_producto_7.clicked.connect(lambda: self.actualizarProducto())
        self.tabla_inventario.cellClicked.connect(self.celda_clicada)

        # Botones de Funcionalidades de CRUD Corte de Caja
        self.btn_agregar_gasto.clicked.connect(
            lambda: self.agregarGastoABaseDeDatos())
        
        # Botones de Funcionalidades de Ventas
        self.lineEdit_busqueda_ventas.textChanged.connect(
            lambda: self.actualizarResultadosBusqueda())
        
        
        # Funcion para actualizar el comboBox de agregar productos

        self.comboBox.currentIndexChanged.connect(lambda: self.actualizarComboBoxAgregarProducto())

        # Funcion para actualizar el comboBox de editar productos

        self.comboBox_13.currentIndexChanged.connect(lambda: self.actualizarComboBoxEditarProducto())

    def validacion_de_credenciales_editar(self):
        contrasena = self.lbl_contrasena_editar.text()
        if contrasena == '123':
            self.lbl_contrasena_editar.setText("")
            self.stackedWidget_menu.setCurrentWidget(
                self.page_editar_inventario)
            self.lineEdit_26.setText(self.lbl_nombre.text())
            self.lineEdit_27.setText(self.lbl_descripcion.text())
            self.lineEdit_28.setText(self.lbl_precio.text())
            self.lineEdit_25.setText(self.lbl_cantidad.text())
            self.comboBox_13.setCurrentText(self.lbl_categoria.text())
            self.comboBox_14.setCurrentText(self.lbl_subcategoria.text())
        else:
            self.lbl_contrasena_editar.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_inventario)

    def validacion_de_credenciales_eliminar(self):
        contrasena = self.lbl_contrasena_eliminar.text()
        if contrasena == '123':
            # en esta linea se realizara la eliminacion
            self.borrarProductoDeBaseDeDatos()
        else:
            self.stackedWidget_menu.setCurrentWidget(self.page_inventario)

    def actualizarTemperatura(self):
        datosCelsius = arduino.readline()
        datosFahrenheit = arduino.readline()
        datosHumedad = arduino.readline()

        if self.comboBox_temperaturas.currentIndex() == 0:
            # Este es el label que muestra la temperatura actual
            self.lbl_temperatura_actual.setText(
                str(datosCelsius.decode('utf-8')))
        elif self.comboBox_temperaturas.currentIndex() == 1:
            # Este es el label que muestra la temperatura actual
            self.lbl_temperatura_actual.setText(
                str(datosFahrenheit.decode('utf-8')))
        else:
            # Este es el label que muestra la temperatura actual
            self.lbl_temperatura_actual.setText(
                str(datosHumedad.decode('utf-8')))

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

    # funcionalides de CRUD de inventario

    def agregarProductoABaseDeDatos(self):
        producto = Producto(self.lineEdit.text(), self.lineEdit_2.text(),
                            self.comboBox.currentText(), self.comboBox_2.currentText(),
                            self.lineEdit_3.text(), self.lineEdit_4.text())
        com = Comunicacion()
        com.insertarProducto(producto)
        self.borrarCamposInventarioAgregar()
        self.actualizarTablaInventario()

    def actualizarTablaInventario(self):
        com = Comunicacion()
        resultados = com.traerProductos()
        self.tabla_inventario.setRowCount(0)
        self.tabla_inventario.setRowCount(len(resultados))

        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_inventario.setItem(fila, columna, item)

        self.stackedWidget_menu.setCurrentWidget(self.page_inventario)

    def actualizarProducto(self):
        producto = Producto(self.lineEdit_26.text(), self.lineEdit_27.text(),
                            self.comboBox_13.currentText(), self.comboBox_14.currentText(),
                            self.lineEdit_28.text(), self.lineEdit_25.text())
        com=Comunicacion()
        com.editarProducto(producto, self.lbl_id.text())
        self.actualizarTablaInventario()

    def borrarProductoDeBaseDeDatos(self):
        com = Comunicacion()
        com.eliminarProducto(self.lbl_id.text())
        self.actualizarTablaInventario()

    def celda_clicada(self, fila, columna):
        # Acción específica cuando una celda se hace clic
        valor = self.tabla_inventario.item(fila, columna).text()
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
    
    #Funciones Insercion de Gastos
    def agregarGastoABaseDeDatos(self):
        fecha_actual = datetime.date.today()
        fecha_actual_str = fecha_actual.strftime('%Y-%m-%d')
        gasto = Gasto(self.lineEdit_concepto_gasto.text(), self.lineEdit_monto_gasto.text(), fecha_actual_str)
        com = Comunicacion()
        com.insertarGasto(gasto)
        self.borrarCamposGastosAgregar()
        

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
    
    #Funciones del apartado Ventas
    def actualizarResultadosBusqueda(self):
        com = Comunicacion()
        resultados = com.traerProductosVentas(self.lineEdit_busqueda_ventas.text())
        self.tabla_ventas.setRowCount(0)
        self.tabla_ventas.setRowCount(len(resultados))

        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_ventas.setItem(fila, columna, item)

        self.stackedWidget_menu.setCurrentWidget(self.page_ventas)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
