from django.db import models


class Region(models.Model):
    """
    Clase Region: Representa una región geográfica de Chile.

    Atributos:
        - nombre: Nombre de la región.
    """
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    """
    Clase Comuna: Representa una comuna de Chile.

    Atributos:
        - nombre: Nombre de la comuna.
        - region: FK hacia Region (una región tiene muchas comunas).
    """
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='comunas')

    def __str__(self):
        return self.nombre


class TipoInmueble(models.Model):
    """
    Clase TipoInmueble: Clasificación del inmueble.

    Atributos:
        - nombre: Nombre del tipo (Casa, Departamento, Oficina...).
        - descripcion: Descripción del tipo de inmueble.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)


class Inmueble(models.Model):
    """
    Clase Inmueble: Inmueble disponible para arriendo.

    Atributos:
        - nombre: Nombre del inmueble.
        - descripcion: Descripción detallada.
        - tipo: FK a TipoInmueble.
        - comuna: FK a Comuna.
        - precio: Precio de arriendo mensual.
        - disponible: Indica si está disponible para arriendo.
    """
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    tipo = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE,
                             related_name='inmuebles')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,
                               related_name='inmuebles')
    precio = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    disponible = models.BooleanField(default=True)


class Usuario(models.Model):
    """
    Clase Usuario: Usuario de la plataforma de arriendo.

    Atributos:
        - nombre: Nombre completo del usuario.
        - email: Correo electrónico (único).
    """
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)