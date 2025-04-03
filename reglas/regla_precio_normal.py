from reglas.regla_precio import ReglaPrecio

class ReglaPrecioNormal(ReglaPrecio):
    def es_aplicable(self, sku):
        return sku.startswith("EA")

    def calcular_total(self, cantidad, precio):
        return cantidad * precio
