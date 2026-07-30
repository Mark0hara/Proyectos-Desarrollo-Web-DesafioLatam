from orden_compra import OrdenCompra

oc = OrdenCompra()
oc.nueva_orden()

oc.identificador = int(input("Ingrese identificador de la OC:\n"))
oc.total_productos = int(input("Ingrese total de productos:\n"))

monto = int(input("Ingrese monto:\n"))
oc.asigna_monto(monto)  # ¡Aquí se asigna el monto Y el descuento automáticamente!

print("Código de descuento:", oc.codigo_descuento)