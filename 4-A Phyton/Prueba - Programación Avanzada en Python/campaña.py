from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoError

class Campaña:
    LARGO_MAXIMO = 250 

    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios=()):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.__anuncios = []
        self.__crear_anuncios(anuncios)

    def __crear_anuncios(self, estructura):
        for d in estructura:
            tipo = d["tipo"].lower()
            if tipo == "video":
                a = Video(d["url_archivo"], d["url_clic"], d.get("duracion", 5), d.get("sub_tipo", "instream"))
            elif tipo == "display":
                a = Display(d.get("ancho", 1), d.get("alto", 1), d["url_archivo"], d["url_clic"], d.get("sub_tipo", "traditional"))
            elif tipo == "social":
                a = Social(d.get("ancho", 1), d.get("alto", 1), d["url_archivo"], d["url_clic"], d.get("sub_tipo", "facebook"))
            else:
                continue
            self.__anuncios.append(a)

    def addAnuncio(self, anuncio: Anuncio):
        self.__anuncios.append(anuncio)

    @property
    def nombre(self): return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        if len(valor) > self.LARGO_MAXIMO:
            raise LargoExcedidoError(f"El nombre supera los {self.LARGO_MAXIMO} caracteres")
        self.__nombre = valor

    @property
    def fecha_inicio(self): return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, valor): self.__fecha_inicio = valor

    @property
    def fecha_termino(self): return self.__fecha_termino
    @fecha_termino.setter
    def fecha_termino(self, valor): self.__fecha_termino = valor

    @property
    def anuncios(self): return self.__anuncios

    def __str__(self):
        v = sum(1 for a in self.__anuncios if isinstance(a, Video))
        d = sum(1 for a in self.__anuncios if isinstance(a, Display))
        s = sum(1 for a in self.__anuncios if isinstance(a, Social))
        return (f"Nombre de la campaña: {self.__nombre}\n"
                f"Fechas: {self.__fecha_inicio} a {self.__fecha_termino}\n"
                f"Anuncios: {v} Video, {d} Display, {s} Social")