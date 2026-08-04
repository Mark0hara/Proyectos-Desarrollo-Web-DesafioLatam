from te import Te

objeto_te_1 = Te()
objeto_te_2 = Te()

tipo_objeto_1 = type(objeto_te_1)
tipo_objeto_2 = type(objeto_te_2)


print("Tipo del objeto 1:", tipo_objeto_1)
print("Tipo del objeto 2:", tipo_objeto_2)

if tipo_objeto_1 == tipo_objeto_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")