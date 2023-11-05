import mysql.connector 

class Comunicacion:
    
    def __init__(self):
        self.conexion=mysql.connector.connect(host = "localhost", user = "root", password = "", database= "pruebas")
    
    def insertarNumero(self):
        cursor = self.conexion.cursor();
        sentenciaSQL = "INSERT INTO numero (numero) VALUES (%s)"
        valores = (60)
        cursor.execute(sentenciaSQL, (valores,))
        self.conexion.commit()
        cursor.close()


