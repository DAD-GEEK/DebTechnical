from models.carrito import Carrito
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()

    def agregar_item_a_carrito(self, skuproducto, cantidad):
        self.carrito.agregar_item(skuproducto, cantidad)
