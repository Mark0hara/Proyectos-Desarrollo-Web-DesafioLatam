from te import Te

print("Bienvenido al sistema de pedidos de té")
print()

print("Sabores disponibles:")
print("1: Té negro")
print("2: Té verde")
print("3: Agua de hierbas")
print()

sabor = int(input("Ingrese el número del sabor deseado: "))
formato = int(input("Ingrese el formato en gramos (300 o 500): "))
nombre_sabor = Te.obtener_nombre_sabor(sabor)
tiempo, recomendacion = Te.obtener_tiempo_y_recomendacion(sabor)
precio = Te.obtener_precio(formato)
print()

print("Detalle del pedido")
print("-" * 30)
print(f"Sabor: {nombre_sabor}")
print(f"Formato: {formato} gr")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")
print(f"Duración del producto: {Te.duracion} días")