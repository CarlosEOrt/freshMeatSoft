class Venta:
    def __init__(self, fecha, monto):
        self.monto=monto
        self.fecha=fecha
    
    def getMonto(self):
        return self.monto
    
    def getFecha(self):
        return self.fecha
