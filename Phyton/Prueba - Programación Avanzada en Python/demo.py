from campaña import Campaña
from anuncio import Anuncio

campana = Campaña("Campaña 1", "2026-08-01", "2026-08-31", (
    {"tipo": "video", "url_archivo": "intro.mp4", "url_clic": "https://ejemplo.com",
     "duracion": 15, "sub_tipo": "instream"},
))

print(campana)
Anuncio.mostrar_formatos()

try:
    campana.nombre = input("Ingrese un nuevo nombre para la campaña: ")
    campana.anuncios[0].sub_tipo = input("Ingrese un nuevo sub_tipo para el anuncio: ")
except Exception as error:
    with open("error.log", "a") as archivo:      # añade el mensaje al .log ✔
        archivo.write(str(error) + "\n")
    print("Ocurrió un error; mensaje registrado en error.log")
else:
    print("Campaña actualizada:\n", campana)