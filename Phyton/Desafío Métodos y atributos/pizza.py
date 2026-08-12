class Pizza:
    precio = 10000
    tamano = "familiar"

    ingredientes_proteicos = [
        "pollo",
        "vacuno",
        "carne vegetal"
    ]

    ingredientes_vegetales = [
        "tomate",
        "aceitunas",
        "champiñones"
    ]

    tipos_masa = [
        "tradicional",
        "delgada"
    ]

    def __init__(self):

        self.proteico = None
        self.vegetal_1 = None
        self.vegetal_2 = None
        self.vegetales = []
        self.masa = None
        self.es_valida = False

    @staticmethod
    def validar(elemento, valores_posibles):

        elemento_normalizado = str(elemento).strip().lower()
        valores_normalizados = [
            str(valor).strip().lower() for valor in valores_posibles
        ]

        return elemento_normalizado in valores_normalizados

    def realizar_pedido(self):
        """
        Solicita al usuario los ingredientes y el tipo de masa.
        Luego valida si el pedido es correcto.
        """

        proteico = input(
            "Ingrese el ingrediente proteico: "
        ).strip().lower()

        vegetal_1 = input(
            "Ingrese el primer ingrediente vegetal: "
        ).strip().lower()

        vegetal_2 = input(
            "Ingrese el segundo ingrediente vegetal: "
        ).strip().lower()

        masa = input(
            "Ingrese el tipo de masa: "
        ).strip().lower()

        self.proteico = proteico
        self.vegetal_1 = vegetal_1
        self.vegetal_2 = vegetal_2
        self.vegetales = [vegetal_1, vegetal_2]
        self.masa = masa

        proteico_valido = Pizza.validar(
            self.proteico,
            Pizza.ingredientes_proteicos
        )

        vegetal_1_valido = Pizza.validar(
            self.vegetal_1,
            Pizza.ingredientes_vegetales
        )

        vegetal_2_valido = Pizza.validar(
            self.vegetal_2,
            Pizza.ingredientes_vegetales
        )

        masa_valida = Pizza.validar(
            self.masa,
            Pizza.tipos_masa
        )

        self.es_valida = (
            proteico_valido
            and vegetal_1_valido
            and vegetal_2_valido
            and masa_valida
        )