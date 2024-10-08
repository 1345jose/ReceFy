from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class MiUsuario(AbstractUser):
    imagen1 = models.ImageField(upload_to='perfil_usuario/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='perfil_usuario/', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    
    def tiene_rol(self, rol_id):
        return self.rol_set.filter(id=id).exists()

    def tiene_rol(self, rol_id):
        return self.rol_set.filter(id=rol_id).exists()

#region Recetas  
class Receta(models.Model): 
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
    me_gusta = models.IntegerField(default=0)

    
    class Meta:
        db_table = "tbl_recetas"
        
#endregion



#region Plan Nutricional (Calendario)

class PlanNutricional(models.Model):
    nombre = models.CharField(max_length=255)
    user = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    desayuno_domingo = models.TextField(blank=True, null=True)
    media_manana_domingo = models.TextField(blank=True, null=True)
    almuerzo_domingo = models.TextField(blank=True, null=True)
    merienda_domingo = models.TextField(blank=True, null=True)
    cena_domingo = models.TextField(blank=True, null=True)

    desayuno_lunes = models.TextField(blank=True, null=True)
    media_manana_lunes = models.TextField(blank=True, null=True)
    almuerzo_lunes = models.TextField(blank=True, null=True)
    merienda_lunes = models.TextField(blank=True, null=True)
    cena_lunes = models.TextField(blank=True, null=True)

    desayuno_martes = models.TextField(blank=True, null=True)
    media_manana_martes = models.TextField(blank=True, null=True)
    almuerzo_martes = models.TextField(blank=True, null=True)
    merienda_martes = models.TextField(blank=True, null=True)
    cena_martes = models.TextField(blank=True, null=True)

    desayuno_miercoles = models.TextField(blank=True, null=True)
    media_manana_miercoles = models.TextField(blank=True, null=True)
    almuerzo_miercoles = models.TextField(blank=True, null=True)
    merienda_miercoles = models.TextField(blank=True, null=True)
    cena_miercoles = models.TextField(blank=True, null=True)

    desayuno_jueves = models.TextField(blank=True, null=True)
    media_manana_jueves = models.TextField(blank=True, null=True)
    almuerzo_jueves = models.TextField(blank=True, null=True)
    merienda_jueves = models.TextField(blank=True, null=True)
    cena_jueves = models.TextField(blank=True, null=True)

    desayuno_viernes = models.TextField(blank=True, null=True)
    media_manana_viernes = models.TextField(blank=True, null=True)
    almuerzo_viernes = models.TextField(blank=True, null=True)
    merienda_viernes = models.TextField(blank=True, null=True)
    cena_viernes = models.TextField(blank=True, null=True)

    desayuno_sabado = models.TextField(blank=True, null=True)
    media_manana_sabado = models.TextField(blank=True, null=True)
    almuerzo_sabado = models.TextField(blank=True, null=True)
    merienda_sabado = models.TextField(blank=True, null=True)
    cena_sabado = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_plan_nutricional'

#endregion

#region Consejeros
class Consejero(models.Model):
    id_consejero = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    titulacion = models.CharField(max_length=225)
    experiencia = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=225)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'tbl_consejeros'
#endregion

#region Dietas Disponibles

class Dieta(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to="dietas/")
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    calorias = models.IntegerField()
    condicion_medica = models.CharField(max_length=255)
    valor_nutricional = models.IntegerField()
    actividad_fisica = models.CharField(max_length=255)
    consejos = models.CharField(max_length=255)
    dispositivos = models.CharField(max_length=255)
    bibliografia = models.CharField(max_length=255)
    fecha_registro_dieta = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE, null=True)
    categoria = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'tbl_dietas'

#endregion

#region Ingredientes

class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    cantidad = models.IntegerField()
    variedad = models.CharField(max_length=255, null=True, blank=True)
    usos = models.CharField(max_length=255, null=True, blank=True)
    p_nutricional = models.CharField(max_length=255, null=True, blank=True)
    consejos = models.CharField(max_length=255, null=True, blank=True)
    grasas_saturadas = models.IntegerField(null=True, blank=True)
    calorias = models.IntegerField(null=True, blank=True)
    hidratos_de_carbono = models.IntegerField(null=True, blank=True)
    grasas_trans = models.IntegerField(null=True, blank=True)
    total_carbohidratos = models.IntegerField(null=True, blank=True)
    azucares = models.IntegerField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    fecha_registro_ingredientes = models.DateTimeField(auto_now_add=True)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "tbl_ingredientes"

#endregion

#region Roles

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    permisos = models.CharField(max_length=255)

    class Meta:
        db_table = "tbl_roles"

class UsuarioRol(models.Model):
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'rol')
        db_table = 'tbl_usuarior'

#enregion

#region Mensajes Usuarios

class Conversacion(models.Model):
    emisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversaciones_enviadas')
    receptor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversaciones_recibidas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_conversaciones'
        verbose_name = 'Conversación'
        verbose_name_plural = 'Conversaciones'

    def __str__(self):
        return f"Conversación entre {self.emisor} y {self.receptor}"


class Mensaje(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_mensaje'
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return f"Mensaje: {self.contenido[:50]}"  # Muestra los primeros 50 caracteres del mensaje


class ConversacionMensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
    mensaje = models.ForeignKey(Mensaje, on_delete=models.CASCADE)
    emisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_conversaciones_mensaje'
        verbose_name = 'Conversación Mensaje'
        verbose_name_plural = 'Conversaciones Mensajes'

    def __str__(self):
        return f"Mensaje en la conversación {self.conversacion.id} entre {self.emisor} y {self.receptor}"






class Amistad(models.Model):
    usuario1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        related_name='amistades_usuario1'
    )
    usuario2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        related_name='amistades_usuario2'
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aceptada = models.BooleanField(default=False) 
    class Meta:
        db_table = "tbl_amistades"
        unique_together = ('usuario1', 'usuario2')  

    def __str__(self):
        return f"Amistad entre {self.usuario1} y {self.usuario2}"
    

#endregion

#region Comentarios

class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios', null=True, blank=True)
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=1500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    me_gusta = models.IntegerField(default=0)  
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE, related_name='comentarios', null=True, blank=True)  # Agregar related_name

    class Meta:
        db_table = "tbl_comentarios"


#endregion

#region Me Gusta

class MeGusta(models.Model):
    comentario = models.ForeignKey(Comentario, related_name='megustas', on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=True, blank=True)
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_like_c"
        unique_together = (('comentario', 'usuario'), ('receta', 'usuario'), ('dieta', 'usuario'))

    def __str__(self):
        if self.comentario:
            return f'Like by {self.usuario} on Comment {self.comentario.id}'
        elif self.receta:
            return f'Like by {self.usuario} on Recipe {self.receta.id}'
        elif self.dieta:
            return f'Like by {self.usuario} on Diet {self.dieta.id}'
        else:
            return f'Like by {self.usuario}'

#endregion

#region Licencias 

class Licencias(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=500)    
    dias = models.BigIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        db_table = "tbl_licencias"

class LicenciasInter(models.Model):
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    licencia = models.ForeignKey(Licencias, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'licencia')
        db_table = 'tbl_licencias_inter'



#endregion

#region Notificaciones

class Notificacion(models.Model):
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE, related_name='notificaciones')
    mensaje = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)

    class Meta:
        db_table = "tbl_notificaciones"

    def __str__(self):
        return f'Notificación para {self.usuario.username}: {self.mensaje}'

#endregion

