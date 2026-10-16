"""
Script: Reporte de inmuebles para arriendo agrupados por REGIÓN.
Conexión a la BD mediante Django + SQL crudo.
"""
import os
import sys
import django

# Configurar el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria.settings')
django.setup()

from django.db import connection

ARCHIVO_SALIDA = "reporte_por_region.txt"

# SQL que une inmueble con comuna y región
SQL = """
    SELECT r.nombre AS region,
           c.nombre AS comuna,
           i.nombre AS nombre,
           i.descripcion AS descripcion
      FROM inmuebles_inmueble i
      JOIN inmuebles_comuna c ON i.comuna_id = c.id
      JOIN inmuebles_region r ON c.region_id = r.id
     WHERE i.disponible = 1
  ORDER BY r.nombre ASC, c.nombre ASC, i.nombre ASC;
"""

def generar_reporte():
    with connection.cursor() as cursor:
        cursor.execute(SQL)
        filas = cursor.fetchall()

    lineas = ["REPORTE DE INMUEBLES PARA ARRIENDO POR REGIÓN", "=" * 55]
    region_actual = None
    total = 0

    for region, comuna, nombre, descripcion in filas:
        if region != region_actual:
            region_actual = region
            lineas.extend(["", f"REGIÓN: {region}", "-" * 40])
        
        lineas.append(f"  [{comuna}] {nombre} - {descripcion}")
        total += 1

    lineas.extend(["", f"Total de inmuebles disponibles: {total}"])

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))

    print(f"✔ Reporte generado exitosamente en: {ARCHIVO_SALIDA}")

if __name__ == "__main__":
    generar_reporte()