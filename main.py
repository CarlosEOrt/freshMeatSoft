import sys
import serial
import time
import datetime
import tempfile
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import messagebox
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

from Producto import Producto
from Gasto import Gasto
from Venta import Venta

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
        self.setWindowTitle('FRESH MEAT SOFT')

        # Setteo de datos de las tablas
        self.actualizarTablaInventario()
        self.actualizarTablaGastos()
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
        self.btn_validar_contrasena_eliminar_temperatura.clicked.connect(
            lambda: self.validacion_de_credenciales_eliminar_temperatura())

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
            lambda: self.stackedWidget_menu.setCurrentWidget(self.page_agregar_montos))
        self.btn_agregar_montos.clicked.connect(
            lambda: self.agregarMontosABaseDeDatos())

        # Botones de Funcionalidades de Ventas
        self.lineEdit_busqueda_ventas.textChanged.connect(
            lambda: self.actualizarResultadosBusqueda())
        self.tabla_ventas.cellClicked.connect(self.agregarProductoACarrito)
        self.tabla_carrito.cellClicked.connect(self.seleccionarProductoDeCarrito)
        self.btn_realizar_venta.clicked.connect(lambda: self.realizarVentaDeCarrito())

        # Funcion para actualizar el comboBox de agregar productos

        self.comboBox.currentIndexChanged.connect(
            lambda: self.actualizarComboBoxAgregarProducto())

        # Funcion para actualizar el comboBox de editar productos

        self.comboBox_13.currentIndexChanged.connect(
            lambda: self.actualizarComboBoxEditarProducto())

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
            self.lineEdit_25.setText(self.lbl_cantidad.text())
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
            self.lbl_contrasena_eliminar_temperatura.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_temperaturas)
        else:
            self.lbl_contrasena_eliminar_temperatura.setText("")
            self.stackedWidget_menu.setCurrentWidget(self.page_temperaturas)

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
        com = Comunicacion()
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

    def celda_clicada_tabla_temperaturas(self, fila, columna):
        # Acción específica cuando una celda se hace clic
        valor = self.tabla_temperaturas.item(fila, columna).text()
        if columna == 4:  # si es la columna de borrado nos lleva a la insercion de contraseña
            self.stackedWidget_menu.setCurrentWidget(
                self.page_credenciales_eliminar_temperatura)

    # Funciones Corte de Caja
    def agregarGastoABaseDeDatos(self):
        fecha_actual_str = self.obtenerFechaActual()
        gasto = Gasto(self.lineEdit_concepto_gasto.text(),
                      self.lineEdit_monto_gasto.text(), fecha_actual_str)
        com = Comunicacion()
        com.insertarGasto(gasto)
        self.borrarCamposGastosAgregar()
        self.stackedWidget_menu.setCurrentWidget(self.page_corte_de_caja)

    def obtenerFechaActual(self):
        fecha_actual = datetime.date.today()
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
            temp_file.write(f"{monto50c}\n{monto1}\n{monto2}\n{monto5}\n{monto10}\n{monto20}\n{monto50}\n{monto100}\n{monto200}\n{monto500}")

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
        #Sumatoria total de los montos en caja
        efectivoTotalCaja = monto50c+monto1+monto2+monto5+monto10+monto20+monto50+monto100+monto200+monto500
        com = Comunicacion()
        resultados = com.sumaGastos(self.obtenerFechaActual())
        
        return efectivoTotalCaja 
    
    def agregarMontosABaseDeDatos(self):
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

        self.guardarTemporalMontos(monto50c, monto1, monto2, monto5, monto10, monto20, monto50, monto100, monto200, monto500)
        self.borrarCamposMontosAgregar()

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
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.tabla_ventas.setItem(fila, columna, item)

    def desbloquearPrograma(self, booleano):
        self.frame_control.setEnabled(booleano)
        self.frame_contenido.setEnabled(booleano)
        self.frame_superior.setEnabled(booleano)

    def agregarProductoACarrito(self, fila, columna):
        valor = self.tabla_ventas.item(fila, columna).text()
        try:
            self.desbloquearPrograma(False)
            cantidadProducto = askstring('CANTIDAD DEL PRODUCTO', 'Proporcione la cantidad del producto a agregar al carrito:')
            self.desbloquearPrograma(True)
            
            # Vamos a verificar que en la tabla haya otro producto para agregarlo ahi mismo o denegar la venta por exceso de stock
            filaConProductoExistenteEnCarrito=self.verificarProductoExistenteEnCarrito(self.tabla_inventario.item(fila, 0).text())
            cantidadExistenteEnCarrito=self.obtenerValorDeCantidadEnCarrito(filaConProductoExistenteEnCarrito)
            #Verificamos el producto
            if(cantidadProducto.isdigit() and int(cantidadProducto)>0 and (int(cantidadProducto)+int(cantidadExistenteEnCarrito))<=int(self.tabla_ventas.item(fila, 2).text())):
                #Verificamos si ya existe el producto en la tabla de venta
                if(filaConProductoExistenteEnCarrito!=-1):
                    #Vamos a modificar
                    cantidadTotalProducto=int(cantidadProducto)+int(cantidadExistenteEnCarrito)
                    itemCantidad = QtWidgets.QTableWidgetItem(str(cantidadTotalProducto))
                    itemPrecio = QtWidgets.QTableWidgetItem(str(float(cantidadTotalProducto)*float(self.tabla_ventas.item(fila, 3).text())))
                    self.tabla_carrito.setItem(filaConProductoExistenteEnCarrito, 2, itemCantidad)
                    self.tabla_carrito.setItem(filaConProductoExistenteEnCarrito, 3, itemPrecio)
                else:
                    # Movemos a la tabla en dado caso de que no encontro coincidencia
                    rowPosition = self.tabla_carrito.rowCount()
                    self.tabla_carrito.insertRow(rowPosition)
                    itemId = QtWidgets.QTableWidgetItem(self.tabla_ventas.item(fila, 0).text())
                    itemNombre = QtWidgets.QTableWidgetItem(self.tabla_ventas.item(fila, 1).text())
                    itemCantidad = QtWidgets.QTableWidgetItem(cantidadProducto)
                    itemPrecio = QtWidgets.QTableWidgetItem(str(float(cantidadProducto)*float(self.tabla_ventas.item(fila, 3).text())))
                    itemEliminar = QtWidgets.QTableWidgetItem("Eliminar")
                    self.tabla_carrito.setItem(rowPosition, 0, itemId)
                    self.tabla_carrito.setItem(rowPosition, 1, itemNombre)
                    self.tabla_carrito.setItem(rowPosition, 2, itemCantidad)
                    self.tabla_carrito.setItem(rowPosition, 3, itemPrecio)
                    self.tabla_carrito.setItem(rowPosition, 4, itemEliminar)
                    
            else:
                messagebox.showwarning('NUMERO INVÁLIDO', 'El numero proporcionado no fue válido o excede la cantidad de producto en el inventario...')
        except:
            self.desbloquearPrograma(True)
            messagebox.showwarning('PROCESO INTERRUMPIDO', 'El proceso fue cancelado o fallo durante la ejecución...')

    def verificarProductoExistenteEnCarrito(self, idBuscar):
        for fila in range(self.tabla_carrito.rowCount()):
            if(idBuscar in self.tabla_carrito.item(fila, 0).text()):
                #regresamos la fila pues el id ya existe
                return fila
        #regresamos -1 como dato que no lo encontro
        return -1
    
    def obtenerValorDeCantidadEnCarrito(self, fila):
        if(fila==-1):
            return 0
        else:
            return self.tabla_carrito.item(fila, 2).text()

    def seleccionarProductoDeCarrito(self, fila, columna):
        filaSeleccionada = self.tabla_carrito.currentRow()
        # Eliminar la fila seleccionada
        if(columna==4 and filaSeleccionada >= 0):
            try:
                respuesta=messagebox.askokcancel('ELIMINAR PRODUCTO DEL CARRITO','¿Desea borrar el elemento seleccionado de la venta?')
                self.desbloquearPrograma(False)
                if(respuesta==1):
                    self.tabla_carrito.removeRow(filaSeleccionada)
                else:
                    messagebox.showInfo('ELIMINAR PRODUCTO DEL CARRITO','El elemento seguirá en el carrito de ventas')
                self.desbloquearPrograma(True)
            except:
                self.desbloquearPrograma(True)
                messagebox.showwarning('PROCESO INTERRUMPIDO', 'El proceso fue cancelado o fallo durante la ejecución...')
        # Modificar la fila seleccionada
        elif(columna==2):
            try:
                self.desbloquearPrograma(False)
                cantidadProducto = askstring('CANTIDAD DEL PRODUCTO', 'Proporcione la cantidad del producto a modificar al carrito:')
                self.desbloquearPrograma(True)
                #Verificamos el producto
                com = Comunicacion()
                resultadoCantidad = com.traerCantidadDeProductoVentas(self.tabla_carrito.item(fila, 0).text())
                resultadosPrecio = com.traerPrecioDeProductoVentas(self.tabla_carrito.item(fila, 0).text())
                if(cantidadProducto.isdigit() and int(cantidadProducto)>0 and int(cantidadProducto)<=int(resultadoCantidad[0])):
                    # Modificamos la cantidad del producto a la tabla en dado caso de que sea valido
                    # Cambiar esto con validación de número
                    itemCantidad = QtWidgets.QTableWidgetItem(cantidadProducto)
                    itemPrecio = QtWidgets.QTableWidgetItem(str(float(cantidadProducto)*float(resultadosPrecio[0])))
                    self.tabla_carrito.setItem(fila, 2, itemCantidad)
                    self.tabla_carrito.setItem(fila, 3, itemPrecio)
                else:
                    messagebox.showwarning('NUMERO INVÁLIDO', 'El numero proporcionado no fue válido o excede la cantidad de producto en el inventario...')
            except:
                self.desbloquearPrograma(True)
                messagebox.showwarning('PROCESO INTERRUMPIDO', 'El proceso fue cancelado o fallo durante la ejecución...')

    def obtenerPrecioTotalDeCarrito(self):
        precioTotal=0
        for fila in range(self.tabla_carrito.rowCount()):
            precioTotal+=float(self.tabla_carrito.item(fila, 3).text())
        #regresamos el valor del precio total de las filas de la tabla del carrito
        return precioTotal

    def realizarVentaDeCarrito(self):
        if(self.tabla_carrito.rowCount()!=0):
            # Actualizar tabla de venta con id :D
            fecha_actual_str = self.obtenerFechaActual()
            precioTotal = self.obtenerPrecioTotalDeCarrito()
            ventaCarrito=Venta(fecha_actual_str, precioTotal)

            com = Comunicacion()
            com.insertarVenta(ventaCarrito)
            
            # Actualizar tabla de inventario_venta :D
            # Actualizar stock en inventario :D
            com = Comunicacion()
            ultimoID=com.traerUltimoIdDeVenta()
            self.insertarProductosEnVentasSeparadas(com, ultimoID)

            # Actualizar tablas :D
            self.actualizarTablaGastos()
            self.lineEdit_busqueda_ventas.setText("")
            self.actualizarResultadosBusqueda()
            self.tabla_carrito.setRowCount(0)
        else:
            messagebox.showwarning('CARRITO VACIO', 'El carrito no cuenta con productos suficientes para una venta...')

    def insertarProductosEnVentasSeparadas(self, com, ultimoIDVenta):
        for fila in range(self.tabla_carrito.rowCount()):
            #Pasamos los datos del carrito a la tabla de inventario_ventas, pasandole el id del producto y la cantidad
            com.insertarVentaInventario(ultimoIDVenta[0], int(self.tabla_carrito.item(fila, 0).text()), int(self.tabla_carrito.item(fila, 2).text()))
            #Ahora actualizaremos el stock con la venta que realizamos
            com.actualizarStockDeVenta(int(self.tabla_carrito.item(fila, 0).text()), int(self.tabla_carrito.item(fila, 2).text()))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
