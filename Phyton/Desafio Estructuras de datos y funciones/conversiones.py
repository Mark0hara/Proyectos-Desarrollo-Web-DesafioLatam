import sys
if len(sys.argv) != 5:
    print("Error: Debe ingresar 4 argumentos: tasa_sol, tasa_ars, tasa_usd y monto_clp")
    sys.exit(1)

tasa_sol = float(sys.argv[1])
tasa_ars = float(sys.argv[2])
tasa_usd = float(sys.argv[3])
monto_clp = float(sys.argv[4])

tasas_conversion = {
    "Soles": tasa_sol,
    "Pesos Argentinos": tasa_ars,
    "Dólares": tasa_usd
}

print(f"Los {int(monto_clp)} pesos equivalen a :")
for moneda, tasa in tasas_conversion.items():
    resultado = monto_clp * tasa
    print(f"{resultado} {moneda}")