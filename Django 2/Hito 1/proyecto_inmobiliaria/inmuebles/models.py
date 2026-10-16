from django.db import models


class Propietario(models.Model):
    """
    Modelo que representa al propietario de un inmueble.
    
    Attributes:
        nombre (str): Nombre completo del propietario.
        email (str): Correo electrónico de contacto.
        telefono (str): Número de teléfono.
    """
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    """
    Modelo que representa una comuna o localidad.
    
    Attributes:
        nombre (str): Nombre de la comuna.
        region (str): Región a la que pertenece.
    """
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}, {self.region}"


class Inmueble(models.Model):
    """
    Modelo que representa un inmueble disponible para arriendo.
    
    Attributes:
        nombre (str): Nombre o título del inmueble.
        descripcion (str): Descripción detallada.
        direccion (str): Dirección física.
        precio (Decimal): Precio de arriendo mensual.
        propietario (ForeignKey): Relación con el modelo Propietario.
        comuna (ForeignKey): Relación con el modelo Comuna.
        disponible (bool): Estado de disponibilidad.
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre