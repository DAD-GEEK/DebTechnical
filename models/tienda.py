from models.carrito import Carrito
from models.producto import Producto
from reglas.manejador_reglas import ManejadorReglas
class Tienda:
    def __init__(self):
        self.total_ventas = 0.0
        self.productos = []
        self.usuarios = []
        self.manejador_reglas = ManejadorReglas()

    def agregar_producto_a_carrito(self, usuario, producto, cantidad):
        if producto.tiene_unidades(cantidad):
            usuario.carrito.agregar_item(producto, cantidad, self.manejador_reglas)
            return True

        else:
            print("No hay suficientes unidades disponibles para agregar al carrito.")
            return False

    def eliminar_item_de_carrito(self, usuario, item):
        usuario.carrito.borrar_item(item)


    def finalizar_compra(self, usuario):
        total = usuario.carrito.calcular_total()
        for item in usuario.carrito.items:
            item.producto.descontar_unidades(item.cantidad)
        self.total_ventas += total
        usuario.carrito.vaciar_carrito()
        return total
