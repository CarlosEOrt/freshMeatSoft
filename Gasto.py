class Gasto:
    def __init__(self, concepto, monto, fecha):
        self.concepto=concepto
        self.monto=monto
        self.fecha=fecha

    def getConcepto(self):
        return self.concepto
    
    def getMonto(self):
        return self.monto
    
    def getFecha(self):
        return self.fecha
