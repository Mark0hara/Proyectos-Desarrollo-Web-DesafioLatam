from string import ascii_lowercase
import getpass
contrasena = getpass.getpass("Ingrese la contraseña: ").lower()
for caracter in contrasena:
    if caracter not in ascii_lowercase:
        print("Error: la contraseña solo puede contener letras (sin ñ).")
        exit()

intentos = 0

for letra in contrasena:
    for candidato in ascii_lowercase:
        intentos += 1            # cada comparación es un intento
        if candidato == letra:   # si coincide, pasa a la siguiente letra
            break

print(f"La contraseña fue forzada en {intentos} intentos")