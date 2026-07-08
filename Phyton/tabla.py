print("=== Generador de Tablas de Multiplicar ===")

while True:
    numero = int(input("\n¿Qué tabla deseas ver? (0 para salir): "))
    
    if numero == 0:
        print("¡Hasta luego!")
        break
    
    print(f"\n--- Tabla del {numero} ---")
    for i in range(1, 13):
        print(f"{numero} x {i} = {numero * i}")
    
    # Preguntar si desea continuar
    continuar = input("\n¿Deseas ver otra tabla? (s/n): ").lower()
    
    if continuar == "n":
        print("¡Hasta luego!")
        break