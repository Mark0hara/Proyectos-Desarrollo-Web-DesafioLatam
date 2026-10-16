from django.db import models

class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50) # Puedes usar BooleanField si prefieres True/False

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
    # Relación hacia Tarea. related_name nos ayudará a consultar las subtareas desde la tarea
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')

    def __str__(self):
        return self.descripcion