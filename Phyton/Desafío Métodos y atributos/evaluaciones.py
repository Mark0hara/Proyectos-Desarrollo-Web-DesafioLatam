from pizza import Pizza

print("Atributos de clase de Pizza:")
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.tamano)
print("Ingredientes proteicos:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("Tipos de masa:", Pizza.tipos_masa)

print("-" * 40)

lista_salsas = ["salsa de tomate", "salsa bbq"]

print(
    "¿La salsa de tomate está en la lista?",
    Pizza.validar("salsa de tomate", lista_salsas)
)

print("-" * 40)

mi_pedido = Pizza()
mi_pedido.realizar_pedido()

print("-" * 40)

print("Ingredientes vegetales:", mi_pedido.vegetales)
print("Ingrediente proteico:", mi_pedido.proteico)
print("Tipo de masa:", mi_pedido.masa)
print("¿La instancia es una pizza válida?", mi_pedido.es_valida)

print("-" * 40)
print(Pizza.es_valida)