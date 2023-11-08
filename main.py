import sys
import serial, time
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

from Producto import Producto

from Comunicacion import Comunicacion

class MyWindow(QMainWindow):
    global arduino 
    #arduino = serial.Serial('COM3', 9600)

    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('carniceria.ui', self)

        #Control al cargar interfaz
        self.control_btn_pestana()
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        self.actualizarTablaInventario()

        #self.timer = QTimer(self) # se crea una variable para constante actualizacion
        #self.timer.timeout.connect(lambda:self.actualizarTemperatura())#actualiza el label
        #self.timer.start(5000)#tiempo que tarda en el contador

        #Redireccion de botones menu
        self.btn_inventario.clicked.connect(lambda: self.actualizarTablaInventario())
        self.btn_ventas.clicked.connect(lambda: self.stackedWidget_menu.setCurrentWidget(self.page_ventas))
        self.btn_cote_de_caja.clicked.connect(lambda: self.stackedWidget_menu.setCurrentWidget(self.page_corte_de_caja))
        self.btn_estadisticas.clicked.connect(lambda: self.stackedWidget_menu.setCurrentWidget(self.page_estadisticas))
        self.btn_temperaturas.clicked.connect(lambda: self.stackedWidget_menu.setCurrentWidget(self.page_temperaturas))

        #Botones de la barra superior
        self.btn_cerrar.clicked.connect(lambda: self.close())
        self.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.btn_pestana.clicked.connect(self.control_btn_pestana)
        self.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        #self.btn_menu.clicked.connect()

        #Botones del CRUD botones de redireccion a metodos del CRUD
        self.btn_agregar_inventario.clicked.connect(lambda: self.stackedWidget_menu.setCurrentWidget(self.page_agregar_inventario))
        self.btn_eliminar_inventario.clicked.connect(lambda: self.stackedWidget_menu.setCurrentWidget(self.page_credenciales_eliminar))
        self.btn_editar_inventario.clicked.connect(lambda: self.stackedWidget_menu.setCurrentWidget(self.page_credenciales_editar))

        
        #Boton Credenciales
        self.btn_validar_contrasena_editar.clicked.connect(lambda: self.validacion_de_credenciales_editar())
        self.btn_validar_contrasena_eliminar.clicked.connect(lambda: self.validacion_de_credenciales_eliminar())

        #Botones de Funcionalidades de CRUD Inventario
        self.btn_agregar_producto.clicked.connect(lambda: self.agregarProductoABaseDeDatos())
        self.tabla_inventario.cellClicked.connect(self.celda_clicada)

    def validacion_de_credenciales_editar(self):
        contrasena = self.lbl_contrasena_editar.text()
        if contrasena == '123':
            self.lbl_contrasena_editar.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_editar_inventario)
        else:
            self.lbl_contrasena_editar.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_inventario)
    
    def validacion_de_credenciales_eliminar(self):
        contrasena = self.lbl_contrasena_eliminar.text()
        if contrasena == '123':
            #en esta linea se realizara la eliminacion
            self.actualizarTablaInventario()
        else:
            self.stackedWidget_menu.setCurrentWidget(self.page_inventario)


    def actualizarTemperatura(self):
        datosCelsius = arduino.readline()
        datosFahrenheit = arduino.readline()
        datosHumedad = arduino.readline()

        if self.comboBox_temperaturas.currentIndex()==0:
            self.lbl_temperatura_actual.setText(str(datosCelsius.decode('utf-8')))#Este es el label que muestra la temperatura actual
        elif self.comboBox_temperaturas.currentIndex()==1:
            self.lbl_temperatura_actual.setText(str(datosFahrenheit.decode('utf-8')))#Este es el label que muestra la temperatura actual
        else:
            self.lbl_temperatura_actual.setText(str(datosHumedad.decode('utf-8')))#Este es el label que muestra la temperatura actual

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


    #funcionalides de CRUD de inventario
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
        resultados=com.traerProductos()
        self.tabla_inventario.setRowCount(0)
        self.tabla_inventario.setRowCount(len(resultados))
        
        for fila, datos in enumerate(resultados):
            for columna, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_inventario.setItem(fila, columna, item)

        self.stackedWidget_menu.setCurrentWidget(self.page_inventario)

    def celda_clicada(self, fila, columna):
        # Acción específica cuando una celda se hace clic
        valor = self.tabla_inventario.item(fila, columna).text()
        print(f"Celda en la fila {fila}, columna {columna} fue clicada. Valor: {valor}")

    #funcionalidades de borrado de campos
    def borrarCamposInventarioAgregar(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())