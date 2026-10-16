class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #atributo
        self.edad = edad #atributo

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar() 
    