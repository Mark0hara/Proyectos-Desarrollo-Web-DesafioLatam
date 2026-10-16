import math

print("CÁLCULO DE VELOCIDAD DE ESCAPE")
r_km = float(input("Ingrese el radio en Kilómetros: "))
g = float(input("Ingrese la constante g en [m/s²]: "))
r_m = r_km * 1000
velocidad_escape = math.sqrt(2 * g * r_m)
print(f"La velocidad de Escape es {velocidad_escape:.1f} [m/s]")