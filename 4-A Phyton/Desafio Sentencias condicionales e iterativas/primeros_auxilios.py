# primeros_auxilios.py

def primeros_auxilios():
    print("--- SISTEMA DE PRIMEROS AUXILIOS ---")
    
    # Paso 1: ¿Requiere apoyo de profesionales?
    apoyo = input("¿Requiere apoyo de profesionales? (si/no): ").lower()
    
    if apoyo == "no":
        print("No es necesario intervenir. Fin.")
        return
    
    # Paso 2: ¿La persona está consciente?
    consciente = input("¿La persona está consciente? (si/no): ").lower()
    
    if consciente == "no":
        # Paso 3: ¿Respira?
        respira = input("¿La persona respira? (si/no): ").lower()
        
        if respira == "no":
            print("Acción: Aplicar RCP (Reanimación Cardiopulmonar) inmediatamente.")
        else:
            print("Acción: Colocar en posición lateral de seguridad.")
    else:
        # Paso 4: Si está consciente, ¿Tiene sangramiento?
        sangramiento = input("¿La persona tiene sangramiento? (si/no): ").lower()
        
        if sangramiento == "si":
            print("Acción: Presionar la herida para detener el sangramiento y llamar a emergencias.")
        else:
            print("Acción: Acompañar a la persona y esperar a los profesionales.")

# Ejecutar la aplicación
if __name__ == "__main__":
    primeros_auxilios()