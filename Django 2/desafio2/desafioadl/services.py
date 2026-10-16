from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    """Devuelve un arreglo (lista de diccionarios) con las tareas y sus subtareas"""
    tareas = Tarea.objects.all().prefetch_related('subtareas')
    resultado = []
    
    for tarea in tareas:
        subtareas_data = []
        for sub in tarea.subtareas.all():
            subtareas_data.append({
                'id': sub.id, 
                'descripcion': sub.descripcion, 
                'estado': sub.estado
            })
        
        resultado.append({
            'id': tarea.id,
            'descripcion': tarea.descripcion,
            'estado': tarea.estado,
            'subtareas': subtareas_data
        })
        
    return resultado

def crear_nueva_tarea(descripcion, estado):
    Tarea.objects.create(descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion, estado):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(arreglo):
    """Imprime las tareas y subtareas en el formato solicitado"""
    for tarea in arreglo:
        print(f"[{tarea['id']}] {tarea['descripcion']}")
        for sub in tarea['subtareas']:
            print(f"....[{sub['id']}] {sub['descripcion']}")