import psycopg2

try:
    conn = psycopg2.connect(
        dbname='inmobiliaria_db',
        user='postgres',
        password='admin123',  # Cambia esto por tu contraseña real
        host='localhost',
        port='5432'
    )
    print("¡Conexión exitosa!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")