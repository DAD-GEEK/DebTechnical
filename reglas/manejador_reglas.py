from reglas.regla_precio_normal import ReglaPrecioNormal
from reglas.regla_precio_peso import ReglaPrecioPorPeso
from reglas.regla_precio_especial import ReglaPrecioEspecial

class ManejadorReglas:
    def __init__(self):
        self.reglas = [ReglaPrecioNormal(), ReglaPrecioPorPeso(), ReglaPrecioEspecial()]

    def obtener_regla(self, sku):
        for regla in self.reglas:
            if regla.es_aplicable(sku):
                return regla
        raise ValueError("No hay una regla aplicable para este SKU")
