
class Producto:
    def __init__(self, nombre, descripcion, categoria, subcategoria, precio, cantidad):
        self.nombre=nombre
        self.descripcion=descripcion
        self.categoria=categoria
        self.subcategoria=subcategoria
        self.precio=precio
        self.cantidad=cantidad

    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion

    def getCategoria(self):
        return self.categoria

    def getSubCategoria(self):
        return self.subcategoria

    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad