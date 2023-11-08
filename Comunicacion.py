import mysql.connector 

class Comunicacion:
    
    def __init__(self):
        self.conexion=mysql.connector.connect(host = "localhost", user = "root", 
                                              password = "", database= "carniceria")
    
    def insertarProducto(self, producto):
        cursor = self.conexion.cursor();
        sentenciaSQL = "INSERT INTO inventario (nombre, descripcion, categoria, subcategoria, precio, cantidad) VALUES (%s, %s, %s, %s, %s ,%s)"
        valores = (producto.getNombre(), producto.getDescripcion(), producto.getCategoria(), producto.getSubCategoria(), 
                   producto.getPrecio(), producto.getCantidad())
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def traerProductos(self):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT * FROM inventario WHERE borrado !=1"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados
