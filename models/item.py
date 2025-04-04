class Item:
    def __init__(self, producto, cantidad, manejador_reglas):
        self.producto = producto
        self.cantidad = cantidad
        self.regla_precio = manejador_reglas.obtener_regla(producto.sku)
        self.valor_total_item = self.calcular_total()

    def calcular_total(self):#usado
        return self.regla_precio.calcular_total(self.cantidad, self.producto.precio_unitario)
