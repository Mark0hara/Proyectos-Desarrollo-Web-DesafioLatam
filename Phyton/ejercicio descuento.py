# Variables (números, no texto)
descuento = 0.50  # 50% se escribe como 0.50 o 50/100
monto_minimo = 10000

# Solicitar compra al usuario
compra = float(input("Ingrese el monto de compra: "))

# Verificar si aplica descuento
if compra > monto_minimo:
    # Calcular el descuento
    monto_descuento = compra * descuento
    total = compra - monto_descuento
    
    print("✓ Se ha aplicado descuento del 50%")
    print(f"Monto original: ${compra}")
    print(f"Descuento: -${monto_descuento}")
    print(f"Total a pagar: ${total}")
else:
    print("✗ No cumple con los requisitos para descuento")
    print(f"Su compra debe ser mayor a ${monto_minimo}")
    print(f"Total a pagar: ${compra}")





# Paso 1: Definir los datos
monto_minimo = 10000          # Si gastas más de esto, tienes descuento
porcentaje_descuento = 50     # 50% de descuento

# Paso 2: Preguntar cuánto gastó el cliente
compra = int(input("¿Cuánto gastaste? "))

# Paso 3: Verificar si gana descuento
if compra > monto_minimo:
    # Calcular descuento (la mitad)
    descuento = compra * 50 / 100
    total = compra - descuento
    
    print("¡GANASTE DESCUENTO!")
    print("Total a pagar:", total)
else:
    print("No tienes descuento :(")
    print("Total a pagar:", compra)