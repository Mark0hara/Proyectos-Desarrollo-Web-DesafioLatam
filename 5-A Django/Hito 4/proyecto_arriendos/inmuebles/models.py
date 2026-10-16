from django.db import models
from usuarios.models import Arrendador # Importamos el modelo del hito anterior

class Inmueble(models.Model):
    TIPO_CHOICES = [
        ('CASA', 'Casa'),
        ('DEPTO', 'Departamento'),
        ('OFICINA', 'Oficina'),
    ]
    
    arrendador = models.ForeignKey(Arrendador, on_delete=models.CASCADE, related_name='inmuebles')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='DEPTO')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Datos geográficos (simplificados como texto para este hito)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.comuna}"