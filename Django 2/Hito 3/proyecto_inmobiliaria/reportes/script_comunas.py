"""
Script: Reporte de inmuebles para arriendo agrupados por COMUNA.
Conexión a la BD mediante Django + SQL crudo.
Solo se muestran los campos 'nombre' y 'descripcion' del inmueble.
"""
import os
import sys
import django

# Configurar el entorno de Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria.settings')
django.setup()

from django.db import connection

ARCHIVO_SALIDA = "reporte_por_comuna.txt"

# SQL que une inmueble con comuna, filtrando solo los disponibles
SQL = """
    SELECT c.nombre AS comuna,
           i.nombre AS nombre,
           i.descripcion AS descripcion
      FROM inmuebles_inmueble i
      JOIN inmuebles_comuna c ON i.comuna_id = c.id
     WHERE i.disponible = 1
  ORDER BY c.nombre ASC, i.nombre ASC;
"""

def generar_reporte():
    with connection.cursor() as cursor:
        cursor.execute(SQL)
        filas = cursor.fetchall()

    lineas = ["REPORTE DE INMUEBLES PARA ARRIENDO POR COMUNA", "=" * 55]
    comuna_actual = None
    total = 0

    for comuna, nombre, descripcion in filas:
        if comuna != comuna_actual:
            comuna_actual = comuna
            lineas.extend(["", f"COMUNA: {comuna}", "-" * 40])
        
        # Solo mostramos nombre y descripción, como pide la rúbrica
        lineas.append(f"  - {nombre}")
        lineas.append(f"    {descripcion}")
        total += 1

    lineas.extend(["", f"Total de inmuebles disponibles: {total}"])

    # Guardar en archivo de texto con codificación UTF-8
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))

    print(f"✔ Reporte generado exitosamente en: {ARCHIVO_SALIDA}")

if __name__ == "__main__":
    generar_reporte()