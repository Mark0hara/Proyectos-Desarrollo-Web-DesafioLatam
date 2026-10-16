from django.db import models
from django.contrib.auth.models import User

# Modelo ARRENDATARIO (Inquilino)
class Arrendatario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='arrendatario')
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} - {self.rut}"


# Modelo ARRENDADOR (Dueño)
class Arrendador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='arrendador')
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} - {self.rut}"