# fuerza_bruta.py
from string import ascii_lowercase
import getpass

# 1. Pedimos la contraseña de manera oculta usando getpass
# (Si tu IDE no soporta getpass, puedes cambiarlo por input())
password = getpass.getpass("Ingrese la contraseña: ")

# 2. Convertimos todo a minúsculas para cumplir el requerimiento
password = password.lower()

intentos = 0

# 3. Recorremos la contraseña letra por letra (de izquierda a derecha)
for letra_password in password:
    
    # 4. Recorremos el abecedario en orden alfabético
    for letra_abecedario in ascii_lowercase:
        intentos += 1  # Cada comparación suma 1 intento
        
        # Si encontramos la letra, rompemos el ciclo interno y pasamos a la siguiente letra
        if letra_password == letra_abecedario:
            break

# 5. Mostramos el resultado final
print(f"La contraseña fue forzada en {intentos} intentos")