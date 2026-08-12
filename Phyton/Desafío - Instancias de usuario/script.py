import json
from usuario import Usuario

def main():
    lista_usuarios = []
    with open('error.log', 'w', encoding='utf-8') as error_log:
        
        try:
            with open('usuario.txt', 'r', encoding='utf-8') as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    linea_limpia = linea.strip()
                    if not linea_limpia:
                        continue
                       
                    try:
                        datos = json.loads(linea_limpia)
                        nuevo_usuario = Usuario(
                            nombre=datos['nombre'],
                            apellido=datos['apellido'],
                            email=datos['email'],
                            genero=datos['genero']
                        )
                        lista_usuarios.append(nuevo_usuario)
                        
                    except Exception as e:
                        error_log.write(f"Error en línea {num_linea}: {type(e).__name__} -> {e}\n")
                        
        except FileNotFoundError:
            print("Error crítico: No se encontró el archivo 'usuario.txt'.")

    print(f"Proceso terminado. Se instanciaron {len(lista_usuarios)} usuarios correctamente.")
    print("Revisa el archivo 'error.log' para ver el detalle de las líneas fallidas.")

if __name__ == "__main__":
    main()