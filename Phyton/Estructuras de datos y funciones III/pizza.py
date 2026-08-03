# =========
# PIZZA JAT 
# =========

masas = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
salsas = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
disponibles = ["Tomate", "Champiñones", "Aceituna", "Cebolla",
               "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

masa = masas[0]
salsa = salsas[0]
ingredientes = []


def mostrar_lista(lista):
    for i in range(len(lista)):
        print(i + 1, "-", lista[i])

def cambiar_masa():
    global masa
    print("\nElige la masa:")
    mostrar_lista(masas)
    op = int(input("Opción: "))
    masa = masas[op - 1]
    print("Masa elegida:", masa)


def cambiar_salsa():
    global salsa
    print("\nElige la salsa:")
    mostrar_lista(salsas)
    op = int(input("Opción: "))
    salsa = salsas[op - 1]
    print("Salsa elegida:", salsa)


def agregar_ingrediente():
    print("\nElige un ingrediente para agregar:")
    mostrar_lista(disponibles)
    op = int(input("Opción: "))
    ingrediente = disponibles[op - 1]
    if ingrediente in ingredientes:
        print("Ese ingrediente ya está.")
    else:
        ingredientes.append(ingrediente)
        print("Agregado:", ingrediente)


def eliminar_ingrediente():
    print("\nElige un ingrediente para eliminar:")
    if len(ingredientes) == 0:
        print("No hay ingredientes para eliminar.")
    else:
        mostrar_lista(ingredientes)
        op = int(input("Opción: "))
        eliminado = ingredientes.pop(op - 1)
        print("Eliminado:", eliminado)

def ver_ingredientes():
    print("\n--- TU PIZZA ---")
    print("Masa:", masa)
    print("Salsa:", salsa)
    print("Ingredientes:", ingredientes)

def estimar_tiempo():
    tiempo = 20 + 2 * len(ingredientes)
    ver_ingredientes()
    print("Tiempo estimado:", tiempo, "minutos")
    respuesta = input("¿Deseas ordenar? (s/n): ")
    if respuesta.lower() == "s":
        print("¡Pedido confirmado! Tu pizza está en preparación 🍕")
        return True
    else:
        print("Pedido cancelado.")
        return False

while True:
    print("\n========== MENÚ ==========")
    print("1. Cambiar masa")
    print("2. Cambiar salsa")
    print("3. Agregar ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Ver mi pizza")
    print("6. Ordenar pizza")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        cambiar_masa()
    elif opcion == "2":
        cambiar_salsa()
    elif opcion == "3":
        agregar_ingrediente()
    elif opcion == "4":
        eliminar_ingrediente()
    elif opcion == "5":
        ver_ingredientes()
    elif opcion == "6":
        if estimar_tiempo():
            break 
    elif opcion == "7":
        print("¡Gracias! Hasta pronto.")
        break
    else:
        print("Opción no válida.")