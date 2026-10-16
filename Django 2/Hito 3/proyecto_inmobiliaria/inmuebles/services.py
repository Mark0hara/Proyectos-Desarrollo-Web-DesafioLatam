"""
Módulo de servicios para manejar las operaciones CRUD 
de los modelos de la aplicación inmuebles.
"""
from inmuebles.models import Inmueble, Propietario, Comuna


def crear_inmueble():
    """
    Crea registros de prueba en la base de datos: 
    un Propietario, una Comuna y un Inmueble relacionado.
    """
    try:
        propietario = Propietario.objects.create(
            nombre="Juan Pérez",
            email="juan.perez@correo.com",
            telefono="912345678"
        )
        
        # 2. Crear comuna
        comuna = Comuna.objects.create(
            nombre="Providencia",
            region="Metropolitana"
        )
        
        # 3. Crear inmueble (usando las Foreign Keys)
        inmueble = Inmueble.objects.create(
            nombre="Departamento céntrico",
            descripcion="Hermoso depto de 2 dormitorios cerca del metro.",
            direccion="Av. Providencia 1234",
            precio=450000.00,
            propietario=propietario,
            comuna=comuna,
            disponible=True
        )
        print(f"✅ Inmueble creado exitosamente: {inmueble.nombre}")
        return inmueble
        
    except Exception as e:
        print(f" Error al crear el inmueble: {e}")


def listar_inmuebles():
    """
    Enlista todos los inmuebles disponibles en la base de datos.
    """
    try:
        inmuebles = Inmueble.objects.all()
        print(f"\n--- Listado de Inmuebles ({inmuebles.count()} encontrados) ---")
        for inm in inmuebles:
            print(f"- {inm.nombre} | Precio: ${inm.precio} | Dueño: {inm.propietario.nombre}")
        return inmuebles
        
    except Exception as e:
        print(f"❌ Error al listar inmuebles: {e}")


def actualizar_inmueble(id_inmueble, nuevo_precio):
    """
    Actualiza el precio de un inmueble específico.
    
    Args:
        id_inmueble (int): ID del inmueble a actualizar.
        nuevo_precio (float): Nuevo precio de arriendo.
    """
    try:
        inmueble = Inmueble.objects.get(id=id_inmueble)
        inmueble.precio = nuevo_precio
        inmueble.save()
        print(f"✅ Inmueble '{inmueble.nombre}' actualizado. Nuevo precio: ${inmueble.precio}")
        return inmueble
        
    except Inmueble.DoesNotExist:
        print(f"❌ Error: No existe un inmueble con el ID {id_inmueble}")
    except Exception as e:
        print(f"❌ Error al actualizar: {e}")


def borrar_inmueble(id_inmueble):
    """
    Borra un inmueble de la base de datos según su ID.
    
    Args:
        id_inmueble (int): ID del inmueble a borrar.
    """
    try:
        inmueble = Inmueble.objects.get(id=id_inmueble)
        nombre = inmueble.nombre
        inmueble.delete()
        print(f"️ Inmueble '{nombre}' borrado exitosamente.")
        
    except Inmueble.DoesNotExist:
        print(f"❌ Error: No existe un inmueble con el ID {id_inmueble}")
    except Exception as e:
        print(f"❌ Error al borrar: {e}")