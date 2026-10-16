import sys

ventas = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000,
    "Abril": 17000, "Mayo": 81000, "Junio": 13000,
    "Julio": 21000, "Agosto": 41200, "Septiembre": 25000,
    "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000
}

if len(sys.argv) < 2:
    print("Debe ingresar un umbral. Ejemplo: python mayor_a.py 40000")
    sys.exit()

umbral = int(sys.argv[1])
filtrado = {}
for mes, valor in ventas.items():
    if valor > umbral:
        filtrado[mes] = valor

print(filtrado)