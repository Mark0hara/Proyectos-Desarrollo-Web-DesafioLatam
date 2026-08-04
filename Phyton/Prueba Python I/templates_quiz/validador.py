def validate(opciones, eleccion):
    ##########################################################################
    opciones_validas = [str(opcion).strip().lower() for opcion in opciones]
    eleccion = str(eleccion).strip().lower()

    while eleccion not in opciones_validas:
        eleccion = input(
            'Opción no válida, ingrese una de las opciones válidas:\n> '
        ).strip().lower()

    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    numeros = ['0','1']
    validate(numeros, eleccion)