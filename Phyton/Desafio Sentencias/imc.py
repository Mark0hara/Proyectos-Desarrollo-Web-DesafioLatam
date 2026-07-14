import sys

peso = float(sys.argv[1])      # Peso en Kg
altura_cm = float(sys.argv[2]) # Altura en centímetros
altura_m = altura_cm / 100
imc = peso / (altura_m ** 2)

if imc < 18.5:
    print("Bajo Peso")
elif imc < 25:
    print("Adecuado")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidad Grado I")
elif imc < 40:
    print("Obesidad Grado II")
else:
    print("Obesidad Grado III")

print(f"Su IMC es {round(imc, 2)}")
