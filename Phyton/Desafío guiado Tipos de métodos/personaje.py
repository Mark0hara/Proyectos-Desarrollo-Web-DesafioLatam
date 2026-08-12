class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def get_estado(self):
        texto = (
            f"NOMBRE: {self.nombre}\n"
            f"NIVEL: {self.nivel}\n"
            f"EXP: {self.experiencia}"
        )
        print(texto)
        return texto

    def set_estado(self, experiencia_recibida):
        exp_temporal = self.experiencia + experiencia_recibida

        while exp_temporal >= 100:
            exp_temporal -= 100
            self.nivel += 1
        while exp_temporal < 0 and self.nivel > 1:
            exp_temporal += 100
            self.nivel -= 1
        if self.nivel == 1 and exp_temporal < 0:
            exp_temporal = 0

        self.experiencia = exp_temporal

    def __lt__(self, otro):
        if not isinstance(otro, Personaje):
            return NotImplemented
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        if not isinstance(otro, Personaje):
            return NotImplemented
        return self.nivel > otro.nivel

    def __eq__(self, otro):
        if not isinstance(otro, Personaje):
            return NotImplemented
        return self.nivel == otro.nivel

    def probabilidad_ganar(self, otro):
        if self > otro:
            return 0.66
        elif self < otro:
            return 0.33
        else:
            return 0.50

    @staticmethod
    def dialogo_enfrentamiento(probabilidad, anunciar_aparicion=False):
        if anunciar_aparicion:
            print("¡Oh no!, ¡Ha aparecido un Orco!")

        porcentaje = round(probabilidad * 100, 1)

        print(f"Con tu nivel actual, tienes {porcentaje}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        print("¿Qué deseas hacer?")
        print("1. Atacar")
        print("2. Huir")

        while True:
            opcion = input().strip()
            if opcion in ("1", "2"):
                return int(opcion)
            print("Opción inválida. Ingresa 1 para Atacar o 2 para Huir.")