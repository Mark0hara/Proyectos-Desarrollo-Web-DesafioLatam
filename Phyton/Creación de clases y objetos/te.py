class Te:
    """
    Clase que representa un té de hoja artesanal.
    """
    duracion = 365

    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor):
        """
        Retorna el tiempo de preparación y la recomendación
        según el sabor ingresado por parámetro.
        """

        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno"
        elif sabor == 2:
            return 5, "Se recomienda consumir al mediodía"
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer"
        else:
            return 0, "Sabor no disponible"

    @staticmethod
    def obtener_precio(formato):
        """
        Retorna el precio según el formato ingresado por parámetro.
        """

        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return 0

    @staticmethod
    def obtener_nombre_sabor(sabor):
        """
        Método auxiliar para transformar el número del sabor
        a un texto legible.
        """

        if sabor == 1:
            return "Té negro"
        elif sabor == 2:
            return "Té verde"
        elif sabor == 3:
            return "Agua de hierbas"
        else:
            return "Sabor no disponible"