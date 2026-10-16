"""
Script para poblar la base de datos con información geográfica de Chile
y crear usuarios de prueba (Arrendador y Arrendatario) con inmuebles.
Ejecutar con: python poblar_datos.py
"""
import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arriendos.settings')
django.setup()

from django.contrib.auth.models import User
from usuarios.models import Arrendador, Arrendatario
from inmuebles.models import Inmueble


def poblar():
    print("🗑️ Limpiando datos anteriores...")
    Inmueble.objects.all().delete()
    Arrendador.objects.all().delete()
    Arrendatario.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()

    print("👤 Creando usuarios de prueba...")

    # Crear usuario Arrendador
    user_arrendador = User.objects.create_user(
        username='arrendador1',
        email='arrendador@test.com',
        password='123456'
    )
    arrendador = Arrendador.objects.create(
        user=user_arrendador,
        nombre='Juan Pérez',
        rut='12345678-9',
        direccion='Av. Providencia 1234',
        telefono='+56912345678',
        email='arrendador@test.com'
    )

    # Crear usuario Arrendatario
    user_arrendatario = User.objects.create_user(
        username='arrendatario1',
        email='arrendatario@test.com',
        password='123456'
    )
    arrendatario = Arrendatario.objects.create(
        user=user_arrendatario,
        nombre='María González',
        rut='87654321-0',
        direccion='Calle Falsa 123',
        telefono='+56987654321',
        email='arrendatario@test.com'
    )

    print("🏠 Creando inmuebles con datos geográficos de Chile...")

    inmuebles_data = [
        # (titulo, descripcion, tipo, precio, region, comuna, direccion)
        ('Departamento en Providencia', 'Moderno depto de 2 dormitorios cerca del metro', 'DEPTO', 450000, 'Metropolitana', 'Providencia', 'Av. Providencia 1234'),
        ('Casa en Las Condes', 'Amplia casa de 3 dormitorios con jardín', 'CASA', 850000, 'Metropolitana', 'Las Condes', 'Av. Apoquindo 4500'),
        ('Oficina en Santiago Centro', 'Oficina de 50m2 ideal para emprendedores', 'OFICINA', 300000, 'Metropolitana', 'Santiago', 'Calle Ahumada 100'),
        ('Departamento en Ñuñoa', 'Depto acogedor cerca de la plaza', 'DEPTO', 380000, 'Metropolitana', 'Ñuñoa', 'Av. Irarrázaval 2000'),
        ('Casa en La Florida', 'Casa familiar con patio', 'CASA', 600000, 'Metropolitana', 'La Florida', 'Calle Vicuña Mackenna 5000'),
        ('Departamento en Valparaíso', 'Vista al mar, 2 dormitorios', 'DEPTO', 380000, 'Valparaíso', 'Valparaíso', 'Av. Brasil 500'),
        ('Casa en Viña del Mar', 'Casa de playa, 4 dormitorios', 'CASA', 700000, 'Valparaíso', 'Viña del Mar', 'Av. San Martín 200'),
        ('Departamento en Concepción', 'Céntrico, cerca de la UdeC', 'DEPTO', 320000, 'Biobío', 'Concepción', 'Calle Barros Arana 300'),
        ('Casa en Temuco', 'Casa familiar con estacionamiento', 'CASA', 550000, 'Araucanía', 'Temuco', 'Av. Alemania 1500'),
        ('Oficina en Antofagasta', 'Oficina corporativa en el centro', 'OFICINA', 400000, 'Antofagasta', 'Antofagasta', 'Calle Prat 450'),
        ('Departamento en La Serena', 'Frente al mar, amoblado', 'DEPTO', 420000, 'Coquimbo', 'La Serena', 'Av. del Mar 800'),
        ('Casa en Puerto Montt', 'Casa de madera, 3 dormitorios', 'CASA', 480000, 'Los Lagos', 'Puerto Montt', 'Calle Benavente 250'),
    ]

    for data in inmuebles_data:
        Inmueble.objects.create(
            arrendador=arrendador,
            titulo=data[0],
            descripcion=data[1],
            tipo=data[2],
            precio=data[3],
            region=data[4],
            comuna=data[5],
            direccion=data[6],
            disponible=True
        )
        print(f"  ✅ {data[0]} - {data[5]}")

    print("\n ¡Datos poblados exitosamente!")
    print("\n🔑 CREDENCIALES DE PRUEBA:")
    print("  Arrendador:  usuario='arrendador1'  |  password='123456'")
    print("  Arrendatario: usuario='arrendatario1' |  password='123456'")


if __name__ == '__main__':
    poblar()