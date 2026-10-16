from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    print("=== CREACIÓN DE TIENDA ===")
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = int(input("Ingrese el costo de delivery: "))
    
    print("\nSeleccione el tipo de tienda:")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")
    
    opcion = input("Opción: ")
    if opcion == "1":
        return Restaurante(nombre, costo_delivery)
    elif opcion == "2":
        return Supermercado(nombre, costo_delivery)
    elif opcion == "3":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Opción inválida. Se creará un Supermercado por defecto.")
        return Supermercado(nombre, costo_delivery)

def main():
    tienda = crear_tienda()
    print(f"\n✅ Tienda '{tienda.nombre}' creada exitosamente.\n")

    while True:
        print("--- INGRESO DE PRODUCTOS ---")
        nombre_prod = input("Nombre del producto: ")
        precio_prod = int(input("Precio del producto: "))
        stock_prod = input("Stock (Enter para 0): ")
        stock_prod = int(stock_prod) if stock_prod.isdigit() else 0
        
        tienda.ingresar_producto(nombre_prod, precio_prod, stock_prod)
        
        continuar = input("¿Desea ingresar otro producto? (s/n): ").lower()
        if continuar != 's':
            break

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Listar productos")
        print("2. Realizar venta")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\n📋 PRODUCTOS DISPONIBLES:")
            print(tienda.listar_productos())
            
        elif opcion == "2":
            nombre_venta = input("Nombre del producto a vender: ")
            cantidad_venta = int(input("Cantidad requerida: "))
            tienda.realizar_venta(nombre_venta, cantidad_venta)
            print("✅ Venta procesada (si aplica según reglas de la tienda).")
            
        elif opcion == "3":
            print("👋 Finalizando programa...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()