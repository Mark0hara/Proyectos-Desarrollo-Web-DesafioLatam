from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre   
        self.__preguntas = [
            Pregunta(p["enunciado"], p["requerida"], p["alternativas"], p.get("ayuda"))
            for p in preguntas
        ]
        self.__listados_respuestas = []   

    @property
    def preguntas(self): return self.__preguntas

    @property
    def listados_respuestas(self): return self.__listados_respuestas

    def mostrar(self):
        print(f"Encuesta: {self.nombre}")
        for p in self.__preguntas:
            p.mostrar()

    def agregar_listado_respuestas(self, listado):
        self.__listados_respuestas.append(listado)


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, preguntas, edad_minima, edad_maxima):
        super().__init__(nombre, preguntas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima

    @property
    def edad_minima(self): return self.__edad_minima
    @edad_minima.setter
    def edad_minima(self, valor):   
        if isinstance(valor, int) and 0 <= valor <= self.__edad_maxima:
            self.__edad_minima = valor

    @property
    def edad_maxima(self): return self.__edad_maxima
    @edad_maxima.setter
    def edad_maxima(self, valor):  
        if isinstance(valor, int) and valor >= self.__edad_minima:
            self.__edad_maxima = valor

    def agregar_listado_respuestas(self, listado):
        if self.__edad_minima <= listado.usuario.edad <= self.__edad_maxima:
            super().agregar_listado_respuestas(listado)
        else:
            print("Edad fuera del rango permitido.")


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, preguntas, regiones):
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    @property
    def regiones(self): return self.__regiones
    @regiones.setter
    def regiones(self, valor):  
        if isinstance(valor, list) and all(isinstance(r, int) for r in valor):
            self.__regiones = valor

    def agregar_listado_respuestas(self, listado):
        if listado.usuario.region in self.__regiones:
            super().agregar_listado_respuestas(listado)
        else:
            print("Región no habilitada.")