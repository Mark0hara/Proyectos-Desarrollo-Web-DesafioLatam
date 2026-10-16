print("UTILIDADES BÁSICAS")
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))

utilidades = P * U - GT
print(f"Las utilidades del proyecto son: ${utilidades:.2f}")