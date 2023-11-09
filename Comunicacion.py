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
    
    def editarProducto(self, producto, idProducto):
        cursor = self.conexion.cursor();
        sentenciaSQL = "UPDATE inventario SET nombre = %s, descripcion = %s, categoria = %s, subcategoria = %s, precio = %s, cantidad = %s WHERE id = %s"
        valores = (producto.getNombre(), producto.getDescripcion(), producto.getCategoria(), producto.getSubCategoria(), producto.getPrecio(), producto.getCantidad(), idProducto)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def eliminarProducto(self, idProducto):
        cursor = self.conexion.cursor();
        sentenciaSQL = "UPDATE inventario SET borrado = %s WHERE id = %s"
        valores = (1, idProducto)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()
