from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self): return self.__correo
    @correo.setter
    def correo(self, valor): self.__correo = valor

    @property
    def edad(self): return self.__edad
    @edad.setter
    def edad(self, valor): self.__edad = valor

    @property
    def region(self): return self.__region
    @region.setter
    def region(self, valor): self.__region = valor

    def contestar_encuesta(self, encuesta, respuestas):
        listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado)