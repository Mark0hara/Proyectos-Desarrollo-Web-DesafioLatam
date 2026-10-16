"""
Script para generar reportes sobre la aplicación de arriendos.
Ejecutar con: python reportes.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arriendos.settings')
django.setup()

from django.db.models import Count, Avg
from inmuebles.models import Inmueble
from usuarios.models import Arrendador, Arrendatario


def generar_reportes():
    print("=" * 60)
    print("📊 REPORTE GENERAL DE LA APLICACIÓN DE ARRIENDOS")
    print("=" * 60)

    # Reporte 1: Totales
    total = Inmueble.objects.count()
    disponibles = Inmueble.objects.filter(disponible=True).count()
    no_disponibles = total - disponibles
    print(f"\n🏠 Total de inmuebles registrados: {total}")
    print(f"  ✅ Disponibles: {disponibles}")
    print(f"  ❌ No disponibles: {no_disponibles}")

    # Reporte 2: Inmuebles por región
    print("\n INMUEBLES POR REGIÓN:")
    regiones = Inmueble.objects.values('region').annotate(total=Count('id')).order_by('-total')
    for r in regiones:
        print(f"  - {r['region']}: {r['total']} inmueble(s)")

    # Reporte 3: Inmuebles por comuna
    print("\n🏘️ INMUEBLES POR COMUNA:")
    comunas = Inmueble.objects.values('comuna').annotate(total=Count('id')).order_by('-total')
    for c in comunas:
        print(f"  - {c['comuna']}: {c['total']} inmueble(s)")

    # Reporte 4: Precio promedio por tipo
    print("\n💰 PRECIO PROMEDIO POR TIPO:")
    tipos = Inmueble.objects.values('tipo').annotate(promedio=Avg('precio')).order_by('tipo')
    for t in tipos:
        print(f"  - {t['tipo']}: ${int(t['promedio']):,}")

    # Reporte 5: Precio más caro y más barato
    mas_caro = Inmueble.objects.order_by('-precio').first()
    mas_barato = Inmueble.objects.order_by('precio').first()
    print(f"\n Inmueble más caro: {mas_caro.titulo} (${mas_caro.precio:,})")
    print(f"💵 Inmueble más barato: {mas_barato.titulo} (${mas_barato.precio:,})")

    # Reporte 6: Total de usuarios
    print(f"\n👥 USUARIOS:")
    print(f"  - Arrendadores: {Arrendador.objects.count()}")
    print(f"  - Arrendatarios: {Arrendatario.objects.count()}")

    print("\n" + "=" * 60)
    print("✅ Fin del reporte")


if __name__ == '__main__':
    generar_reportes()