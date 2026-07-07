huevos = True
sarten = True
gas = True
encendedor = True
aceite = True
sal = True

if huevos:
    print("Tenemos Huevo")
else:
    print("Comprar Huevos")

if sarten and gas and encendedor and sal and aceite:
    print("tenemos todos los materiales")
else:
    print("Faltan implementos:", + "sarten: ", "gas: ", "sal: ", "aceite: ", "encendedor")

respuesta = input("Que preparacion Quieres (1=duro, 2=frito, 3=revuelto):")

if respuesta == "1":
    print("Preparando Huevo duro")
if respuesta == "2":
    print("Preparando huevo frito")
if respuesta == "3":
    print("Preparando huevo revueltos")

print("Su huevo esta listo")