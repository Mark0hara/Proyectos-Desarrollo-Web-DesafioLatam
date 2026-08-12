class DimensionError(Exception):
    def __init__(self, mensaje, dimension=None, maximo=None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        texto = self.mensaje

        if self.dimension is not None:
            texto += f" | Dimensión: {self.dimension}"

        if self.maximo is not None:
            texto += f" | Máximo permitido: {self.maximo}"

        return texto