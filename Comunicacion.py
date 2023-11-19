import mysql.connector 
import datetime

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

    #Consultas Corte de Caja
    def insertarGasto(self, gasto):
        cursor = self.conexion.cursor();
        sentenciaSQL = "INSERT INTO gastos (concepto, monto, fecha) VALUES (%s, %s, %s)"
        valores = (gasto.getConcepto(), gasto.getMonto(), gasto.getFecha())
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()
    
    def traerGastos(self):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT * FROM gastos ORDER BY fecha DESC;"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados
    
    def sumaGastos(self, fecha):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT ROUND(SUM(monto), 2) FROM gastos WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        print("Gasto DIA:",resultado)
        return resultado
    
    def sumaVentas(self, fecha):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT ROUND(SUM(monto), 2) FROM ventas WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        print("VENTA DIA:",resultado)
        return resultado
    
    #Consultas Ventas
    #Cambio realizado a la consulta de traer ventas
    def traerProductosVentas(self, cadenaBusqueda):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT id, nombre, cantidad, precio FROM inventario WHERE borrado !=1 AND cantidad > 0 AND nombre LIKE %s "
        valores = ('%'+cadenaBusqueda+'%')
        cursor.execute(sentenciaSQL, (valores, ))
        resultados = cursor.fetchall()
        return resultados
    
    def traerCantidadDeProductoVentas(self, idProducto):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT cantidad FROM inventario WHERE %s = id"
        valores = (idProducto)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()
        return resultado
    
    def traerPrecioDeProductoVentas(self, idProducto):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT precio FROM inventario WHERE %s = id"
        valores = (idProducto)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()
        return resultado
    
    def insertarVenta(self, venta):
        cursor = self.conexion.cursor();
        sentenciaSQL = "INSERT INTO ventas (fecha, monto) VALUES (%s, %s)"
        valores = (venta.getFecha(), venta.getMonto())
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def traerUltimoIdDeVenta(self):
        cursor = self.conexion.cursor();
        sentenciaSQL = "SELECT MAX(id) FROM ventas"
        cursor.execute(sentenciaSQL)
        resultado = cursor.fetchone()
        return resultado

    def insertarVentaInventario(self, idVenta, idProducto, cantidad):
        cursor = self.conexion.cursor();
        sentenciaSQL = "INSERT INTO inventario_ventas (idVenta, idProducto, cantidad) VALUES (%s, %s, %s)"
        valores = (idVenta, idProducto, cantidad)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()
    
    def actualizarStockDeVenta(self, idProducto, cantidadDeVenta):
        cursor = self.conexion.cursor();
        sentenciaSQL = "UPDATE inventario SET cantidad = cantidad - %s WHERE id = %s"
        valores = (cantidadDeVenta, idProducto)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def insertarTemperatura(self, fecha, tempPromedio, tempMax, tempMin):
        cursor = self.conexion.cursor();
        sentenciaSQL = "INSERT INTO temperaturas (minima, maxima, promedio, fecha) VALUES (%s, %s, %s, %s)"
        valores = (tempMin, tempMax, tempPromedio, fecha)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def traerTemperaturas(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * FROM temperaturas;"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados
    
    def verificarFechaTemperaturas(self, fecha):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT id FROM temperaturas WHERE %s = fecha;"
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()
        return resultado
    
    def verificarUnidadesTemperatura(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT minima FROM temperaturas WHERE id = (SELECT Min(id) FROM temperaturas);"
        cursor.execute(sentenciaSQL)
        resultado = cursor.fetchone()
        return resultado
    
    def eliminarTemperatura(self, idTemperatura):
        cursor = self.conexion.cursor();
        sentenciaSQL = "DELETE FROM temperaturas WHERE id = %s"
        valores = (idTemperatura)
        cursor.execute(sentenciaSQL, (valores, ))
        self.conexion.commit()
        cursor.close()