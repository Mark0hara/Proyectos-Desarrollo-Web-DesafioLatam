import preguntas as p
import random
from shuffle import shuffle_alt

opciones = {
    'basicas': [1, 2, 3],
    'intermedias': [1, 2, 3],
    'avanzadas': [1, 2, 3]
}

def choose_q(dificultad):
    preguntas = p.pool_preguntas[dificultad]
    
    global opciones
    
    n_elegido = random.choice(opciones[dificultad])
    
    opciones[dificultad].remove(n_elegido)
    
    pregunta = preguntas[f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(pregunta)
    
    return pregunta['enunciado'], alternativas


if __name__ == '__main__':
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')