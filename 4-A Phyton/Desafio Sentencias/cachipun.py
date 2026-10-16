import sys
import random

jugada_usuario = sys.argv[1].lower()
if jugada_usuario not in ["piedra", "papel", "tijera"]:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    exit()

jugada_compu = random.choice(["piedra", "papel", "tijera"])

if jugada_usuario == jugada_compu:
    resultado = "Empataron!!"
elif (jugada_usuario == "piedra" and jugada_compu == "tijera") or \
     (jugada_usuario == "tijera" and jugada_compu == "papel") or \
     (jugada_usuario == "papel" and jugada_compu == "piedra"):
    resultado = "Ganaste!!"
else:
    resultado = "Perdiste!!"

print(f"Tu jugaste {jugada_usuario.capitalize()} Computador jugó {jugada_compu} {resultado}")