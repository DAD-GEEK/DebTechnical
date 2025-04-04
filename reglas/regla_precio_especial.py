from reglas.regla_precio import ReglaPrecio
class ReglaPrecioEspecial(ReglaPrecio):
    def es_aplicable(self, sku):
        return sku.startswith("SP")

    def calcular_total(self, cantidad, precio):
        descuento = min((cantidad // 3) * 0.2, 0.5)
        return cantidad * precio * (1 - descuento)
