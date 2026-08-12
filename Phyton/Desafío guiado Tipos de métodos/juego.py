from random import uniform
from personaje import Personaje

class Juego:
    def iniciar(self):
        print("¡Bienvenido a Gran Fantasía!")
        nombre = input("Por favor indique nombre de su personaje: ").strip()
        self.jugador = Personaje(nombre)
        self.jugador.get_estado()
        self.orco = Personaje("Orco")
        self.probabilidad = self.jugador.probabilidad_ganar(self.orco)
        self.opcion = Personaje.dialogo_enfrentamiento(
            self.probabilidad,
            anunciar_aparicion=True
        )

        while self.opcion == 1:
            self._turno_ataque()
            self.opcion = Personaje.dialogo_enfrentamiento(self.probabilidad)
        print("¡Has huido! El orco ha quedado atrás.")

    def _turno_ataque(self):
        numero_azar = uniform(0, 1)
        resultado = "Gana" if numero_azar <= self.probabilidad else "Pierde"

        if resultado == "Gana":
            print("¡Le has ganado al orco, felicidades!")
            print("¡Recibirás 50 puntos de experiencia!")

            self.jugador.set_estado(50)
            self.orco.set_estado(-30)

        else:
            print("¡Oh no! ¡El orco te ha ganado!")
            print("¡Has perdido 30 puntos de experiencia!")

            self.jugador.set_estado(-30)
            self.orco.set_estado(50)
        self.jugador.get_estado()
        self.orco.get_estado()
        self.probabilidad = self.jugador.probabilidad_ganar(self.orco)

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar()