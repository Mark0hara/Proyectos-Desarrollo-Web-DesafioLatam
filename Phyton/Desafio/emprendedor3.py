print("COMPARACIÓN DE UTILIDADES")
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))
U_anterior = float(input("Ingrese las utilidades del año anterior: "))

U_actuales = P * U - GT
if U_anterior == 0:
    print("⚠️ ADVERTENCIA: No se puede calcular la razón porque las utilidades del año anterior son 0.")
else:
    razon = U_actuales / U_anterior
    print(f"Utilidades actuales: ${U_actuales:.2f}")
    print(f"Razón actuales/anterior: {razon:.2f}")