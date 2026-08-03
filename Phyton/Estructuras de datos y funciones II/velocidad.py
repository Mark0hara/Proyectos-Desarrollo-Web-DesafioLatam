
velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1, 14, 14,
    16, 10, 6, 23, 13, 25, 4, 19, 14, 20,
    18, 9, 18, 4, 18, 1, 3, 4, 2, 14,
    23, 19, 23, 9, 18, 20, 22, 14, 1, 10,
    5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21
]


def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números
    sin usar librerías externas.
    """
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


def posiciones_sobre_promedio(lista):
    """
    Retorna una lista con las posiciones de los elementos
    que están estrictamente sobre el promedio.
    """
    promedio = calcular_promedio(lista)
    posiciones = []

    for indice, valor in enumerate(lista):
        if valor > promedio:
            posiciones.append(indice)

    return posiciones


if __name__ == '__main__':
    resultado = posiciones_sobre_promedio(velocidad)
    print(resultado)