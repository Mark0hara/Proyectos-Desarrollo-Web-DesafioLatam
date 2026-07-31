class Calculadorafinanciera:
    @staticmethod
    def es_monto_valido(monto: float) -> bool:
        return monto > 0    #No usa datos de la clase, solo procesa sus argumentos, por eso es estatico