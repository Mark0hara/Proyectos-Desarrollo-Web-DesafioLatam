
print("Monitoreo Temperatura y Humedad")
temperatura = float(input("\nIngrese la temperatura en °C: "))
temp_max = 95
temp_Segura = 70
    
while True:
   

    if temperatura > temp_max:
        print("¡Alerta! La temperatura es demasiado alta. Se recomienda apagar el sistema.")
        accion = input("¿Activar enfriamiento? (s/n): ")
        if accion == "s":
        # Reduces temperatura
            temperatura -= 10
        elif accion == "n":
            break
    elif temperatura > temp_Segura:
        print("Advertencia: La temperatura está en un rango alto. Se recomienda monitorear de cerca.")
    else:
        print("La temperatura es segura.")  
    break

