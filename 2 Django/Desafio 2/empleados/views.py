# empleados/views.py
from django.shortcuts import render

def lista_empleados(request):
    nombres_empleados = [
        "Ana Pérez",
        "Carlos López",
        "María González",
        "Jorge Ramírez",
        "Nataly Abalos"
    ]
    
    contexto = {
        'empleados': nombres_empleados
    }
    
    return render(request, 'empleados/lista.html', contexto)