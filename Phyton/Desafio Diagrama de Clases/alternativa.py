class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido   # consulta y modificación libre
        self.ayuda = ayuda           # opcional

    def mostrar(self):
        print(f"- {self.contenido}")
        if self.ayuda is not None:
            print(f"  Ayuda: {self.ayuda}")