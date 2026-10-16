#python prueba.py probamos si fucniona importando lo anterior
from encuesta import EncuestaLimitadaEdad, EncuestaLimitadaRegion
from usuario import Usuario

preguntas = [
    {"enunciado": "¿Cuál es tu color favorito?", "ayuda": "Elige uno",
     "requerida": True,
     "alternativas": [{"contenido": "Rojo"},
                      {"contenido": "Azul", "ayuda": "Como el cielo"}]}
]

enc_edad = EncuestaLimitadaEdad("Encuesta colores", preguntas, 18, 99)
enc_edad.mostrar()

ana = Usuario("ana@mail.com", 25, 1)
pedro = Usuario("pedro@mail.com", 15, 1)

ana.contestar_encuesta(enc_edad, [0])     # ✔ se agrega
pedro.contestar_encuesta(enc_edad, [1])   # ✘ rechazado por edad
print("Listados por edad:", len(enc_edad.listados_respuestas))

enc_region = EncuestaLimitadaRegion("Encuesta zonas", preguntas, [1, 2])
ana.contestar_encuesta(enc_region, [1])   # ✔ región 1 permitida
print("Listados por región:", len(enc_region.listados_respuestas))