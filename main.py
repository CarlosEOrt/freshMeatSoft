import sys
import serial, time
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class MyWindow(QMainWindow):
    global arduino 
    arduino = serial.Serial('COM3', 9600)

    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('carniceria.ui', self)
        
        self.timer = QTimer(self) # se crea una variable para constante actualizacion
        self.timer.timeout.connect(lambda:self.actualizarTemperatura())#actualiza el label
        self.timer.start(5000)#tiempo que tarda en el contador

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())