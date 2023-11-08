from Producto import Producto

from Comunicacion import Comunicacion

producto = Producto("nombre", "descripcion", "categoria", "subcategoria", 40, 10) 

com = Comunicacion()

resultados=com.traerProductos()
#com.insertarProducto(producto)

for fila in resultados:
    # Realiza operaciones con los datos de cada fila
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Descripcion: {fila[2]}, Categoria: {fila[3]}, Subcategoria: {fila[4]}, Precio: {fila[5]}, Cantidad: {fila[6]}")

