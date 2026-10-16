from abc import ABC, abstractmethod


class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):

        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta
        self._dias_regalo = 0

    @property
    def correo_suscriptor(self) -> str:
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self) -> str:
        return self.__numero_tarjeta

    @property
    def dias_regalo(self) -> int:
        return self._dias_regalo
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int):
        pass
    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        return self


class Gratis(Membresia):

    costo = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        # Gratis puede cambiar a Básica (1), Familiar (2), Sin Conexión (3) o Pro (4)
        if nueva_membresia in (1, 2, 3, 4):
            return self._crear_nueva_membresia(nueva_membresia)

        return self


class Basica(Membresia):

    costo = 3000
    cantidad_dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia: int):
        # Básica puede cambiar a Familiar (2), Sin Conexión (3) o Pro (4)
        if nueva_membresia in (2, 3, 4):
            return self._crear_nueva_membresia(nueva_membresia)

        return self

    def cancelar_suscripcion(self):
        """
        Cancela la suscripción y retorna una membresía Gratis
        con el mismo correo y número de tarjeta.
        """
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)


class Familiar(Basica):

    costo = 5000
    cantidad_dispositivos = 5

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._dias_regalo = 7

    def cambiar_suscripcion(self, nueva_membresia: int):
        # Familiar puede cambiar a Básica (1), Sin Conexión (3) o Pro (4)
        if nueva_membresia in (1, 3, 4):
            return self._crear_nueva_membresia(nueva_membresia)
        return self
    def modificar_control_parental(self):
        pass

class SinConexion(Basica):

    costo = 3500
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._dias_regalo = 7

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in (1, 2, 4):
            return self._crear_nueva_membresia(nueva_membresia)
        return self
    def incrementar_contenido_sin_conexion(self):
        pass


class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._dias_regalo = 15

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia in (1, 2, 3):
            return self._crear_nueva_membresia(nueva_membresia)
        return self
Basico = Basica