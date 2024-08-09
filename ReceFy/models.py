from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.images import get_image_dimensions

class MiUsuario(AbstractUser):
    imagen1 = models.ImageField(upload_to='perfil_usuario/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='perfil_usuario/', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
  

#region Recetas  
class Receta(models.Model):
    STATUS_CHOICES = [
        ('habilitado', 'Habilitado'),
        ('inhabilitado', 'Inhabilitado'),
    ]

    id_receta = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=50)
    categoria = models.CharField(max_length=255)
    temporada = models.CharField(max_length=255)
    origen = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=255)
    instrucciones = models.CharField(max_length=255)
    tiempo_preparacion = models.CharField(max_length=10)
    dificultad = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="recetas/")
    fecha_registro_receta = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(MiUsuario, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='habilitado', null=True)
    class Meta:
        db_table = "tbl_recetas"
        
#endregion