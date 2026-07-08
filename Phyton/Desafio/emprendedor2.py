print("=== UTILIDADES CON USUARIOS PREMIUM ===")
P = float(input("Ingrese el precio de suscripción base: "))
U_normal = int(input("Número de usuarios normales: "))
U_premium = int(input("Número de usuarios premium: "))
GT = float(input("Ingrese los gastos totales: "))

utilidades = (P * U_normal) + (P * 1.5 * U_premium) - GT
print(f"Las utilidades con usuarios diferenciados son: ${utilidades:.2f}")