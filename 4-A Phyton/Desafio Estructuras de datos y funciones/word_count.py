import sys

if len(sys.argv) != 2:
    print("Uso: python word_count.py <nombre_archivo.txt>")
    sys.exit(1)

nombre_archivo = sys.argv[1]

try:
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        texto = file.read()
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo}'")
    sys.exit(1)

caracteres_distintos = len(set(texto))
palabras = texto.split()
palabras_distintas = len(set(palabras))
# python word_count.py lorem_ipsum.txt --> Me cuenta 241 palabras distintas en vez de 243 originales, porque hay 2 palabras que tienen un caracter especial al final (punto y coma) y no las reconoce como iguales.
print(f"El número de caracteres distintos es: {caracteres_distintos}")
print(f"El número de palabras distintas es : {palabras_distintas}")