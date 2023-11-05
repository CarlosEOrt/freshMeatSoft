import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('carniceria.ui', self)

        self.timer = QTimer(self) # se crea una variable para constante actualizacion
        self.timer.timeout.connect(lambda:self.actualizarTemperatura())#actualiza el label
        self.timer.start(1000)#tiempo que tarda en el contador

    def actualizarTemperatura(self):
        temperatura = self.lbl_temperatura_actual.text() #ejemplo de agarrar texto de un label
        temperatura2 = (int(temperatura) + 5) #ejemplo de transformar texto a variable usable 
        self.lbl_temperatura_actual.setText(str(temperatura2)) #Este es el label que muestra la temperatura actual

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())