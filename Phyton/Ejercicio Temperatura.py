print("Monitoreo Temperatura y Humedad")
temperatura = float(input("\nIngrese la temperatura en °C: "))
temp_max = 95
temp_Segura = 70

print("\n=== CONTROLES ===")
print("1 - Ver temperatura")
print("2 - Activar enfriamiento (-10°C)")
print("3 - Simular paso de tiempo (+5°C)")
print("4 - Salir")

while True:
    print(f"\n🌡️  Temperatura: {temperatura}°C")
    
    if temperatura > temp_max:
        print("🚨 ¡ALERTA CRÍTICA!")
    elif temperatura > temp_Segura:
        print("⚠️  Advertencia")
    else:
        print("✅ Normal")
    
    opcion = input("\n¿Qué desea hacer? (1-4): ")
    
    if opcion == "1":
        pass  # Solo muestra
    elif opcion == "2":
        temperatura -= 10
        print("❄️  Enfriando...")
    elif opcion == "3":
        temperatura += 5
        print("🔥 Generando calor...")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")