from orden_compra import OrdenCompra

oc = OrdenCompra()
oc.nueva_orden()

oc.identificador = int(input("Ingrese identificador de la OC:\n"))
oc.total_productos = int(input("Ingrese total de productos:\n"))
oc.monto = int(input("Ingrese monto:\n"))

# Lógica del descuento
if oc.monto > 20000:
    oc.codigo_descuento = "20PORCIENTO"
elif oc.monto > 10000:
    oc.codigo_descuento = "10PORCIENTO"

print("Código de descuento:", oc.codigo_descuento)