def hacer_encuesta():
    preguntas = [
        "1. ¿Cuál es tu nombre?",
        "2. ¿Cuál es tu edad?",
        "3. ¿Cuál es tu pasatiempo favorito?"
    ]
    respuestas_usuario = []
    
    print("--- INICIO DE LA ENCUESTA ---")
    for pregunta in preguntas:
        respuesta = input(pregunta + " ")
        respuestas_usuario.append(respuesta)
        
    print("--- ENCUESTA FINALIZADA ---\n")
    return respuestas_usuario

def mostrar_resultados(lista_de_respuestas):
    print("TUS RESPUESTAS FUERON:")
    print("-" * 25)
    
    for numero, respuesta in enumerate(lista_de_respuestas, start=1):
        print(f"Pregunta {numero}: {respuesta}")    
    print("-" * 25)

if __name__ == "__main__":
    mis_respuestas = hacer_encuesta()
    mostrar_resultados(mis_respuestas)