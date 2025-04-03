from reglas.regla_precio import ReglaPrecio

class ReglaPrecioPorPeso(ReglaPrecio):
    def es_aplicable(self, sku):
        return sku.startswith("WE")

    def calcular_total(self, cantidad, precio):
        return (cantidad / 1000) * precio  # Precio por kilogramo
