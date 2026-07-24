
import sys

# Diccionario de ventas proporcionado
ventas = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000,
    "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200,
    "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000
}

# Capturamos el umbral desde los argumentos de la línea de comandos (sys.argv[1])
# y lo convertimos a entero
umbral = int(sys.argv[1])

# Creamos un nuevo diccionario filtrando los meses que superan el umbral
# Usamos comprensión de diccionarios para hacerlo "compacto"
resultado = {mes: valor for mes, valor in ventas.items() if valor > umbral}

# Imprimimos el resultado
print(resultado)