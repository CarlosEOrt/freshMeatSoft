import mysql.connector
import datetime


class Comunicacion:

    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root",
                                                password="", database="carniceria")

    def insertarProducto(self, producto):
        cursor = self.conexion.cursor()
        sentenciaSQL = "INSERT INTO inventario (nombre, descripcion, categoria, subcategoria, precio, cantidad) VALUES (%s, %s, %s, %s, %s ,%s)"
        valores = (producto.getNombre(), producto.getDescripcion(), producto.getCategoria(), producto.getSubCategoria(),
                   producto.getPrecio(), producto.getCantidad())
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def traerProductos(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * FROM inventario WHERE borrado !=1"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados

    def editarProducto(self, producto, idProducto):
        cursor = self.conexion.cursor()
        sentenciaSQL = "UPDATE inventario SET nombre = %s, descripcion = %s, categoria = %s, subcategoria = %s, precio = %s, cantidad = %s WHERE id = %s"
        valores = (producto.getNombre(), producto.getDescripcion(), producto.getCategoria(
        ), producto.getSubCategoria(), producto.getPrecio(), producto.getCantidad(), idProducto)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def eliminarProducto(self, idProducto):
        cursor = self.conexion.cursor()
        sentenciaSQL = "UPDATE inventario SET borrado = %s WHERE id = %s"
        valores = (1, idProducto)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    # Consultas Corte de Caja
    def insertarGasto(self, gasto):
        cursor = self.conexion.cursor()
        sentenciaSQL = "INSERT INTO gastos (concepto, monto, fecha) VALUES (%s, %s, %s)"
        valores = (gasto.getConcepto(), gasto.getMonto(), gasto.getFecha())
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def traerGastos(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT * FROM gastos ORDER BY fecha DESC;"
        cursor.execute(sentenciaSQL)
        resultados = cursor.fetchall()
        return resultados

    def sumaGastos(self, fecha):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT ROUND(SUM(monto), 2) FROM gastos WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        resultado = resultado if resultado is not None else 0
        cursor.close()
        return resultado

    def sumaVentas(self, fecha):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT ROUND(SUM(monto), 2) FROM ventas WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        resultado = resultado if resultado is not None else 0
        cursor.close()
        return resultado

    def insertarCorte(self, monto, fecha, efectivoEnCaja):
        cursor = self.conexion.cursor()
        sentenciaSQL = "INSERT INTO cortedecaja (monto, fecha, efectivoEnCaja) VALUES (%s, %s, %s)"
        valores = (monto, fecha, efectivoEnCaja)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def traerIDCorte(self, fecha):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT id FROM cortedecaja WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        resultado = resultado if resultado is not None else 0
        cursor.close()
        return resultado

    def verificacionCorteEnBase(self, fecha):
        cursor = self.conexion.cursor()
        try:
            # Consulta para verificar si no hay datos para la fecha de hoy
            consulta = f"SELECT * FROM cortedecaja WHERE fecha = '{fecha}'"

            # Ejecutar la consulta
            cursor.execute(consulta)

            # Obtener resultados
            resultados = cursor.fetchall()

            # Verificar si no hay resultados para la fecha de hoy
            return not resultados

        finally:
            # Cerrar el cursor y la conexión
            cursor.close()
            self.conexion.close()

    # Consultas Ventas
    # Cambio realizado a la consulta de traer ventas
    def traerProductosVentas(self, cadenaBusqueda):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT id, nombre, cantidad, precio, categoria, subcategoria FROM inventario WHERE borrado !=1 AND cantidad > 0 AND nombre LIKE %s "
        valores = ('%'+cadenaBusqueda+'%')
        cursor.execute(sentenciaSQL, (valores, ))
        resultados = cursor.fetchall()
        return resultados

    def traerCategoriaDeProductos(self, idBusqueda):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT categoria, subcategoria FROM inventario WHERE id = %s"
        valores = (idBusqueda)
        cursor.execute(sentenciaSQL, (valores, ))
        resultados = cursor.fetchall()
        return resultados


    def traerCantidadDeProductoVentas(self, idProducto):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT cantidad FROM inventario WHERE %s = id"
        valores = (idProducto)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()
        return resultado

    def traerPrecioDeProductoVentas(self, idProducto):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT precio FROM inventario WHERE %s = id"
        valores = (idProducto)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()
        return resultado

    def insertarVenta(self, venta):
        cursor = self.conexion.cursor()
        sentenciaSQL = "INSERT INTO ventas (fecha, monto) VALUES (%s, %s)"
        valores = (venta.getFecha(), venta.getMonto())
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def traerUltimoIdDeVenta(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT MAX(id) FROM ventas"
        cursor.execute(sentenciaSQL)
        resultado = cursor.fetchone()
        return resultado

    def insertarVentaInventario(self, idVenta, idProducto, cantidad):
        cursor = self.conexion.cursor()
        sentenciaSQL = "INSERT INTO inventario_ventas (idVenta, idProducto, cantidad) VALUES (%s, %s, %s)"
        valores = (idVenta, idProducto, cantidad)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    def actualizarStockDeVenta(self, idProducto, cantidadDeVenta):
        cursor = self.conexion.cursor()
        sentenciaSQL = "UPDATE inventario SET cantidad = cantidad - %s WHERE id = %s"
        valores = (cantidadDeVenta, idProducto)
        cursor.execute(sentenciaSQL, (valores))
        self.conexion.commit()
        cursor.close()

    # Consultas Temperaturas
    def insertarTemperatura(self, fecha, tempPromedio, tempMax, tempMin):
        cursor = self.conexion.cursor()
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

    def traerTemperaturaMin(self, fecha):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT minima FROM temperaturas WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado

    def traerTemperaturaMax(self, fecha):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT maxima FROM temperaturas WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado

    def traerTemperaturaProm(self, fecha):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT promedio FROM temperaturas WHERE fecha = %s; "
        valores = (fecha)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchone()[0]
        cursor.close()
        return resultado

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
        cursor = self.conexion.cursor()
        sentenciaSQL = "DELETE FROM temperaturas WHERE id = %s"
        valores = (idTemperatura)
        cursor.execute(sentenciaSQL, (valores, ))
        self.conexion.commit()
        cursor.close()

    # Consultas para estadistica
    def estadisticasVentas(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT fecha, COUNT(*) as cantidad_ventas FROM ventas GROUP BY fecha ORDER BY fecha DESC LIMIT 5;"
        cursor.execute(sentenciaSQL)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def estadisticasGastos(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT SUM(monto) FROM gastos WHERE MONTH(fecha) = MONTH(CURDATE()) AND YEAR(fecha) = YEAR(CURDATE());"
        cursor.execute(sentenciaSQL)
        resultado = cursor.fetchone()[0]
        resultado = resultado if resultado is not None else 0
        cursor.close()
        return resultado

    def estadisticasIngresos(self):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT SUM(monto) FROM ventas WHERE MONTH(fecha) = MONTH(CURDATE()) AND YEAR(fecha) = YEAR(CURDATE());"
        cursor.execute(sentenciaSQL)
        resultado = cursor.fetchone()[0]
        resultado = resultado if resultado is not None else 0
        cursor.close()
        return resultado

    def estadisticasProductos(self, nombreProducto):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT ventas.fecha, SUM(inventario_ventas.cantidad) as cantidad_ventas FROM ventas JOIN inventario_ventas ON ventas.id = inventario_ventas.idVenta JOIN inventario ON inventario_ventas.idProducto = inventario.id WHERE ventas.fecha >= CURRENT_DATE - INTERVAL 7 DAY AND inventario.nombre = %s GROUP BY ventas.fecha;"
        valores = (nombreProducto)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    
    def traerVentasDeTicket(self, idTicket):
        cursor = self.conexion.cursor()
        sentenciaSQL = "SELECT inventario.id, inventario.nombre, inventario_ventas.cantidad, inventario_ventas.cantidad*inventario.precio, ventas.fecha, inventario.categoria, inventario.subcategoria FROM inventario  JOIN inventario_ventas ON inventario.id = inventario_ventas.idProducto  JOIN ventas ON inventario_ventas.idVenta = ventas.id  WHERE inventario_ventas.idVenta = %s;"
        valores = (idTicket)
        cursor.execute(sentenciaSQL, (valores, ))
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
