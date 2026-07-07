print("Hola Mundo")

# Print multitext: se separa con "," y agrega un espacio
nombre = "Ana"
edad = 33
print("Hola", nombre, "tengo", edad, "años y vivo en Chile")
# Hola Ana tengo 33 años y vivo en Chile

# Print modernos con cadena de formateadas (f-string)
# El indica que se insertarán directamente llaves {}
producto = "Laptop"
precio = 450000.00
print(f"El precio de la {producto} es {precio}") #El precio de la Laptop es 450000.00
print(f"El precio tiene 10% de descuento {precio * 1.10:.2f}")

# Print "Modificando el separador sep"
# Separar elementos con un guion
print("Región", "Zona", "Código", sep="-")  # Resultado: Región-Zona-Código

# Salto de línea entre cada elemento
print("Una", "Dos", "Tres", sep="\n")

# Print "Modificando el final de la línea end"
# Reemplazar el salto de línea por un espacio
print("Cargando sistema", end="...")
print("Listo")

# print multicomilla triple comilla
print("""
***Menu Opciones**
      1. Iniciar juego      
      2.Configuracion
      3.Salir   
""")

# Print con Métodos transformaciones de texto directas
# Quita espacios extra en los extremos (.strip) y pone mayúsculas (.title)
nombre_cliente = "  Juan Castellano  "
print(f"Cliente registrado: {nombre_cliente.strip().title()}")

# Print con Expresiones condicionales directas (Operador ternario)
# Decide qué texto mostrar en una sola línea según el valor de la variable
es_miembro_vip = True
print(f"Tipo de envío: {'Gratis por ser VIP' if es_miembro_vip else '$250 estándar'}")