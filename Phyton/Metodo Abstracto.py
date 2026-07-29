from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

# Uso
perro = Perro()
gato = Gato()
print(perro.sonido()) # Salida: Guau
print(gato.sonido()) # Salida: Miau