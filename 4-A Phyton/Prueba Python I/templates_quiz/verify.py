import preguntas as p


def verificar(alternativas, eleccion):
    eleccion = str(eleccion).strip().lower()

    if eleccion not in ['a', 'b', 'c', 'd']:
        print('Respuesta Incorrecta')
        return False

    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)
    correcto = alternativas[eleccion][1] == 1

    if correcto:
        print('Respuesta Correcta')
    else:
        print('Respuesta Incorrecta')

    return correcto


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)