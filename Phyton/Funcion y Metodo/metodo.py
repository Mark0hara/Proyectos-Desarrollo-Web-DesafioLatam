class Producto:
    def __init__(self, precio:float):
        self.precio = precio

    def calcular_total(self, impuesto: float) -> float:
        return self.precio * (1 + impuesto)