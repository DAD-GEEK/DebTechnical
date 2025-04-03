from abc import ABC, abstractmethod

class ReglaPrecio(ABC):
    @abstractmethod
    def es_aplicable(self, sku):
        pass

    @abstractmethod
    def calcular_total(self, cantidad, precio):
        pass
