class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido   
        self.ayuda = ayuda           

    def mostrar(self):
        print(f"- {self.contenido}")
        if self.ayuda is not None:
            print(f"  Ayuda: {self.ayuda}")