from models.item import Item
class Carrito:
    def __init__(self):
        self.items = []
        self.cantidad_items = 0
        self.total_compra = 0.0
        
    def agregar_item(self, producto, cantidad, manejador_reglas):
        item = Item(producto, cantidad, manejador_reglas)
        self.items.append(item)
        self.cantidad_items += 1
        self.total_compra += item.valor_total_item
        

    def calcular_total(self):
        return sum(item.calcular_total() for item in self.items)
        
    def borrar_item(self, item):
        self.total_compra -= item.valor_total_item
        self.cantidad_items -= 1
        self.items.remove(item)

    def vaciar_carrito(self):
        self.items.clear()
