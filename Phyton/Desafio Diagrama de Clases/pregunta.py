from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, requerida, alternativas, ayuda=None):
        self.enunciado = enunciado    # libre
        self.ayuda = ayuda            # libre
        self.requerida = requerida    # libre
        self.__alternativas = [
            Alternativa(a["contenido"], a.get("ayuda")) for a in alternativas
        ]

    @property
    def alternativas(self):
        return self.__alternativas

    def mostrar(self):
        print(f"Pregunta: {self.enunciado}")
        if self.ayuda is not None:
            print(f"Ayuda: {self.ayuda}")
        print(f"Requerida: {'Sí' if self.requerida else 'No'}")
        for alt in self.__alternativas:
            alt.mostrar()