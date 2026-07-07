edad_minima = 18
contrasena = "python"


edad_usuario = int(input("Ingresa tu edad: "))
contrasena_usuario = input("Ingresa tu contraseña: ")

if edad_usuario >= edad_minima and contrasena_usuario == contrasena:
    print("¡Acceso exitoso! Bienvenido al sistema.")
    
elif edad_usuario < edad_minima:
    print("Acceso denegado. Eres menor de edad.")
    
else:
    print("Error de credenciales. La contraseña es incorrecta.")