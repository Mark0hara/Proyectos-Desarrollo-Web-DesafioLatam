class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalles(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def detalles(self):
        return f"{super().detalles()}, Puertas: {self.puertas}"

coche = Coche("Toyota", "Corolla", 4)
print(coche.detalles()) # Salida: Marca: Toyota, Modelo: Corolla, Puertas: 4