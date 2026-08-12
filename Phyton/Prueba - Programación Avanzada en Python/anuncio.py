from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho=1, alto=1, url_archivo="", url_clic="", sub_tipo=None):
        # Regla de negocio: mayor a 0, si no, 1
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto  = alto  if alto  > 0 else 1
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self): return self.__ancho
    @ancho.setter
    def ancho(self, valor): self.__ancho = valor if valor > 0 else 1

    @property
    def alto(self): return self.__alto
    @alto.setter
    def alto(self, valor): self.__alto = valor if valor > 0 else 1

    @property
    def url_archivo(self): return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self, valor): self.__url_archivo = valor

    @property
    def url_clic(self): return self.__url_clic
    @url_clic.setter
    def url_clic(self, valor): self.__url_clic = valor

    @property
    def sub_tipo(self): return self.__sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, valor):
        if valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(
                f"Sub tipo '{valor}' inválido para {type(self).__name__}. Permitidos: {self.SUB_TIPOS}")
        self.__sub_tipo = valor

    @staticmethod
    def mostrar_formatos():
        for clase in (Video, Display, Social):
            print(f"{clase.FORMATO}:")
            print("==========")
            for sub in clase.SUB_TIPOS:
                print(f"- {sub}")
            print()

    @abstractmethod
    def comprimir_anuncio(self): pass
    @abstractmethod
    def redimensionar_anuncio(self): pass


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, duracion, sub_tipo="instream"):
        super().__init__(ancho=1, alto=1, url_archivo=url_archivo,
                         url_clic=url_clic, sub_tipo=sub_tipo)  # llamado al padre ✔
        self.duracion = duracion

    @Anuncio.ancho.setter
    def ancho(self, valor): pass
    @Anuncio.alto.setter
    def alto(self, valor): pass

    @property
    def duracion(self): return self.__duracion
    @duracion.setter
    def duracion(self, valor): self.__duracion = valor if valor > 0 else 5

    def comprimir_anuncio(self): print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self): print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("traditional", "native")
    def comprimir_anuncio(self): print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self): print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def comprimir_anuncio(self): print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self): print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")