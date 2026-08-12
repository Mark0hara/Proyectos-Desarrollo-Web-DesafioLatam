class Error(Exception):
    """Clase base de errores personalizados."""
    pass

class LargoExcedidoError(Error):
    """Nombre de campaña demasiado largo."""
    pass

class SubTipoInvalidoError(Error):
    """Sub_tipo no permitido para el tipo de anuncio."""
    pass