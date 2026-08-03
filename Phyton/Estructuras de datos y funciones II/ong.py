def factorial(numero):
    """
    Calcula el factorial de un número entero no negativo.

    Ejemplo:
    5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    if not isinstance(numero, int):
        numero = int(numero)

    if numero < 0:
        return None

    resultado = 1

    for i in range(2, numero + 1):
        resultado *= i

    return resultado


def productoria(lista):
    """
    Calcula la productoria de una lista de números.

    Ejemplo:
    [3, 6, 4, 2, 8] = 3 * 6 * 4 * 2 * 8 = 1152
    """
    resultado = 1

    for elemento in lista:
        resultado *= elemento

    return resultado


def calcular(**kwargs):
    """
    Función que controla los cálculos de factorial y productoria.

    Recibe argumentos dinámicos.
    Si el nombre del argumento contiene 'fact', calcula factorial.
    Si contiene 'prod', calcula productoria.

    Ejemplos:
    calcular(fact_1=5)
    calcular(prod_1=[3, 6, 4, 2, 8])
    calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
    """
    for nombre, valor in kwargs.items():
        if 'fact' in nombre:
            resultado = factorial(valor)

            if resultado is None:
                print(f'El factorial de {valor} no está definido')
            else:
                print(f'El factorial de {valor} es {resultado}')

        elif 'prod' in nombre:
            resultado = productoria(valor)
            print(f'La productoria de {valor} es {resultado}')

        else:
            print(f'El parámetro {nombre} no es válido')


if __name__ == '__main__':
    calcular(
        fact_1=5,
        prod_1=[4, 6, 7, 4, 3],
        fact_2=6
    )
