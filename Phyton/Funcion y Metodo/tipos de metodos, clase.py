# Reciben la propia clase como primer parámetro explícito, tradicionalmente denominado cls. 
# Tienen acceso al estado de la clase y se usan frecuentemente para implementar patrones de diseño como Factories (constructores alternativos).

class Usuario:
    def __init__(self, nombre:str, rol: str):
        self.nombre = nombre
        self.rol = rol

    @classmethod
    def crear_usuario(cls, nombre:str):
        return cls(nombre=nombre, rol="usuario")