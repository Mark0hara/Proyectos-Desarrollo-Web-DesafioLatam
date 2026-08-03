import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(precios, umbral, operacion='mayor'):
    """
    Filtra los productos cuyo precio sea estrictamente mayor o menor
    que el umbral indicado.

    :param precios: Diccionario con productos y precios.
    :param umbral: Valor de referencia para comparar.
    :param operacion: 'mayor' o 'menor'. Por defecto es 'mayor'.
    :return: Diccionario filtrado o None si la operación no es válida.
    """
    if operacion == 'mayor':
        return {
            producto: precio
            for producto, precio in precios.items()
            if precio > umbral
        }
    elif operacion == 'menor':
        return {
            producto: precio
            for producto, precio in precios.items()
            if precio < umbral
        }
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Debe ingresar un umbral. Ejemplo: python filtro.py 30000')
    else:
        try:
            umbral = float(sys.argv[1])
        except ValueError:
            print('El umbral debe ser un número.')
            sys.exit(1)

        if len(sys.argv) >= 3:
            operacion = sys.argv[2]
        else:
            operacion = 'mayor'

        if operacion not in ('mayor', 'menor'):
            print('Lo sentimos, no es una operación válida')
        else:
            productos_filtrados = filtrar_productos(
                precios,
                umbral,
                operacion
            )

            nombres_productos = ', '.join(productos_filtrados.keys())

            if operacion == 'mayor':
                print(f'Los productos mayores al umbral son: {nombres_productos}')
            else:
                print(f'Los productos menores al umbral son: {nombres_productos}')