from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.images import get_image_dimensions

class MiUsuario(AbstractUser):
    imagen1 = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    
