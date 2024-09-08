from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import  DietaForm, IngredienteForm, RecetaForm
from .models import Consejero, Dieta, Ingrediente, MiUsuario, Notificacion, Receta , Comentario, MeGusta, PlanNutricional, Rol, UsuarioRol ,  Licencias, LicenciasInter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
import matplotlib.pyplot as plt
from django.db import IntegrityError
from io import BytesIO
import base64
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Q
import re
from django.db.models import Count

#region Importaciones Sistema Generado de PDF
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
import io
from django.utils import timezone
#endregion


def index(request):
    if request.user.is_authenticated:
        tiene_rol_7 = UsuarioRol.objects.filter(usuario=request.user, rol_id=7).exists()
        tiene_rol_5 = UsuarioRol.objects.filter(usuario=request.user, rol_id=5).exists()
    else:
        tiene_rol_7 = False
        tiene_rol_5 = False

    return render(request, 'index.html', {'tiene_rol_7': tiene_rol_7, 'tiene_rol_5': tiene_rol_5})

#region Novedades
    
def apartado_novedades(request):
    pagina_actual = "informacion"

    # Obtener las recetas que tienen al menos un "me gusta" y ordenarlas por cantidad de "me gusta"
    recetas_mas_likes = Receta.objects.annotate(
        me_gusta_count=Count('megusta')  
    ).filter(me_gusta_count__gt=0).order_by('-me_gusta_count')  # Filtrar recetas con más de 0 "me gusta"

    # Obtener las recetas que tienen al menos un comentario y ordenarlas por cantidad de comentarios
    recetas_mas_comentarios = Receta.objects.annotate(
        comentario_count=Count('comentarios')  # Asegúrate de que 'comentarios' es el nombre correcto
    ).filter(comentario_count__gt=0).order_by('-comentario_count')  # Filtrar recetas con más de 0 comentarios

    return render(request, "apartado_novedades.html", {
        "pagina": pagina_actual,
        "recetas_mas_likes": recetas_mas_likes,
        "recetas_mas_comentarios": recetas_mas_comentarios,  # Pasar las recetas con más comentarios al contexto
    })

#region Salud Nutricion

def salud_nutricion(request):
    pagina_actual = "salud_nutricion"
    return render(request, "salud_nutricion/salud_nutricion.html", {"pagina": pagina_actual})

#endregion
def registro_usuario(request):
    pagina_actual = "registro"
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmar_contraseña = request.POST.get("confirmar_contraseña")

        if not username or not email or not password or not confirmar_contraseña:
            messages.error(request, "Por favor, completa todos los campos.")
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, "Ingresa un correo electrónico válido.")
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

        if email.endswith(("edu", "org", "gov", "mil", "net")):
            messages.error(request, "Por favor, utiliza un correo personal y no institucional o laboral.")
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

        if password != confirmar_contraseña:
            messages.error(request, "Las contraseñas no coinciden. Por favor, intenta nuevamente.")
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

        if len(password) < 8 or not re.search(r'[A-Z].*[A-Z]', password) or not re.search(r'\d.*\d.*\d', password) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            messages.error(request, "La contraseña debe tener al menos 8 caracteres, incluyendo 2 letras mayúsculas, 3 números y 1 carácter especial.")
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

        if MiUsuario.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso. Por favor, utiliza otro.")
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

        if MiUsuario.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso. Por favor, elige otro.")
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

        user = MiUsuario.objects.create_user(username=username, email=email, password=password)
        
        licencia = get_object_or_404(Licencias, id=1)  
        LicenciasInter.objects.create(usuario=user, licencia=licencia)

        rol = get_object_or_404(Rol, id=6) 
        UsuarioRol.objects.create(usuario=user, rol=rol)

        messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
        return render(request, "usuarios/registro.html", {"pagina": pagina_actual, "registro_exitoso": True})

    return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

def loginusuarios(request):
    pagina_actual = "loginusuarios"
    mensaje = ""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            try:
                user = MiUsuario.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    mensaje = "Correo Electronico o Contraseña incorrectos, Intente de nuevo."  
            except MiUsuario.DoesNotExist:
                mensaje = "Este usuario NO Exite, Por favor Registrese o Intente de nuevo."
        else:
            mensaje = "Por favor, ingrese ambos campos."

    return render(request, "usuarios/login.html", {"pagina": pagina_actual, "mensaje": mensaje})

def logoutusuarios(request):
    logout(request)
    return redirect('/')

def mi_perfil(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    usuario = request.user
    return render(request,'usuarios/mi_perfil.html',{'usuario':usuario})

def completar_info(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    pagina_actual = "completar_info"
    usuario = request.user
    if usuario.first_name and usuario.last_name and usuario.telefono and usuario.fecha_nacimiento and usuario.biografia and usuario.pais and usuario.idioma and usuario.edad:
        messages.info(request, 'Ya has completado tu información.')
        return redirect('/usuarios/mi_perfil') 
    if request.method == "POST":
        usuario = request.user
        if request.POST.get('first_name'):
            usuario.first_name = request.POST.get('first_name')
        if request.POST.get('last_name'):
            usuario.last_name = request.POST.get('last_name')
        if request.POST.get('telefono'):
            usuario.telefono = request.POST.get('telefono')
        if request.POST.get('fecha_nacimiento'):
            usuario.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        if request.POST.get('biografia'):
            usuario.biografia = request.POST.get('biografia')
        if request.POST.get('pais'):
            usuario.pais = request.POST.get('pais')
        if request.POST.get('idioma'):
            usuario.idioma = request.POST.get('idioma')
        if request.POST.get('edad'):
            usuario.edad = request.POST.get('edad')
        
        usuario.save()
        return redirect('/usuarios/mi_perfil')  
    return render(request,'usuarios/completar_info.html',{'pagina':pagina_actual})

def actualizar_info(request, idusuario):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    if request.user.id != idusuario:
        return redirect('/usuarios/mi_perfil')
    pagina_actual = "configuracion"
    act = request.user
    if request.method == "POST":
        if  request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('biografia') and request.POST.get('telefono') and request.POST.get('fecha_nacimiento') and request.POST.get('pais') and request.POST.get('idioma'):
            act = MiUsuario.objects.get(id=idusuario)
            act.first_name = request.POST.get('first_name')
            act.last_name = request.POST.get('last_name')
            act.biografia = request.POST.get('biografia')
            act.telefono = request.POST.get('telefono')
            act.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            act.pais = request.POST.get('pais')
            act.idioma = request.POST.get('idioma')
            act.save()
            return redirect('/usuarios/mi_perfil')
    else:
        act = MiUsuario.objects.filter(id=idusuario)
        return render(request,'configuracion/actualizar_usuario.html', {'act':act, 'pagina':pagina_actual})
    


@login_required
def imagen2(request):
    if request.method == "POST":
        usuario = request.user  
        if request.FILES.get('imagen2'):
            usuario.imagen2 = request.FILES.get('imagen2')
        usuario.save()
    return render(request, 'configuracion/imagenes_usuario.html')

def subir_imagen_perfil(request):
    if request.method == 'POST':
        usuario = request.user
        if 'imagen2' in request.FILES:
            usuario.imagen2 = request.FILES['imagen2']
            usuario.save()
            messages.success(request, 'Imagen de perfil actualizada.')
        else:
            messages.error(request, 'No se seleccionó ninguna imagen.')
        return redirect('mi_perfil')

def eliminar_imagen_perfil(request):
    usuario = get_object_or_404(MiUsuario, id=request.user.id)

    # Verificamos si el usuario tiene una imagen de perfil
    if usuario.imagen2:
        usuario.imagen2.delete()  # Esto elimina el archivo de la carpeta de medios
        usuario.imagen2 = None    # Esto vacía el campo de imagen en la base de datos
        usuario.save()
        messages.success(request, "La imagen de perfil ha sido eliminada.")
    else:
        messages.error(request, "No tienes una imagen de perfil para eliminar.")

    return redirect('mi_perfil')


#mis megustas
def usuariosLikes(request, usuario_id):
    pagina_actual = "megustas"
    usuario = request.user 
    likes_comentarios = MeGusta.objects.filter(usuario=usuario, comentario__isnull=False)
    likes_recetas = MeGusta.objects.filter(usuario=usuario, receta__isnull=False)
    likes_dietas = MeGusta.objects.filter(usuario=usuario, dieta__isnull=False)

    context = {
        'likes_comentarios': likes_comentarios,
        'likes_recetas': likes_recetas,
        'likes_dietas': likes_dietas,
        'pagina': pagina_actual, 

    }
    
    return render(request, 'usuarios/mis_likes.html', context)
#endmegustas


#endregion

#region Configuraciones

def rest_email(request):
    pagina_actual = "reset_password"
    if request.method == "POST":
        email = request.POST.get("email")
        User = get_user_model()

        if email:
            try:
                user = User.objects.get(email=email)

                password_update_url = request.build_absolute_uri(
                    reverse('passwordUpdate', kwargs={'idusuario': user.id})
                )

                plain_message = (
                    f"De: Grupo ReceFy\n"
                    f"Correo para: {email}\n\n"
                    "Hola, Recupera tu contraseña en el siguiente link: "
                    f"{password_update_url}"
                )

                html_message = f"""
                <html>
                    <body style="background-color: #198d57a9; font-family: 'Courgette', cursive; font-family: 'Lobster', sans-serif; line-height: 1.5; color: white; padding:20px; border-radius: 25px;">
                        <div style="backgroud-color: rgba(255, 255, 255, 0.486);">
                            <h2>ReceFy</h2>
                            <p>Hola,</p>
                            <p>Recupera tu contraseña haciendo clic en el siguiente enlace:</p>
                            <a href="{password_update_url}" style="display: inline-block; padding: 10px 20px; background-color: #28a56b; color: white; text-decoration: none; border-radius: 15px;">Recuperar Contraseña</a>
                            <p>Si el botón anterior no funciona, copia y pega el siguiente enlace en tu navegador:</p>
                            <p><a href="{password_update_url}">{password_update_url}</a></p>
                            <p>Saludos,<br>El equipo de ReceFy</p>
                        </div>
                    </body>
                </html>
                """

                send_mail(
                    "Recuperación de Contraseña",
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                    html_message=html_message, 
                )

                messages.success(request, 'El correo de recuperación ha sido enviado exitosamente.')

                return redirect('/configuracion/recuperar_contraseña')
            except User.DoesNotExist:
                return render(request, 'configuracion/cambiar_contraseña/recuperacion_contraseña.html', {'error': 'El correo electrónico no está registrado.'})
            except Exception as e:
                return render(request, 'configuracion/cambiar_contraseña/recuperacion_contraseña.html', {'error': str(e)})
        else:
            return render(request, 'configuracion/cambiar_contraseña/recuperacion_contraseña.html', {'error': 'Por favor, proporciona un correo electrónico válido.'})
        
    return render(request, 'configuracion/cambiar_contraseña/recuperacion_contraseña.html',{'pagina':pagina_actual})

         
def passwordUpdate(request,idusuario):
    pagina_actual = "passwordUpdate"
    if request.method == "POST":
        usuario = request.user  
        if request.POST.get('password'):
            usuario = MiUsuario.objects.get(id=idusuario)
            usuario.set_password(request.POST.get('password'))
            usuario.save()
            return redirect('/usuarios/login')
    else:   
        return render(request, 'configuracion/cambiar_contraseña/passwordUpdate.html',{'pagina':pagina_actual})

def updateUser(request, idusuario):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    pagina_actual = "updateUser"
    usuario = get_object_or_404(MiUsuario, id=idusuario)
    
    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not usuario.check_password(current_password):
            messages.error(request, 'La contraseña actual no es correcta.')
        elif new_password != confirm_password:
            messages.error(request, 'Las nuevas contraseñas no coinciden.')
        else:
            usuario.set_password(new_password)
            usuario.save()
            update_session_auth_hash(request, usuario)  # Mantiene la sesión del usuario actualizada
            messages.success(request, 'La contraseña ha sido cambiada exitosamente.')
            return redirect('/usuarios/login')
    
    return render(request, 'configuracion/cambiar_contraseña/usuario_pass_act.html', {'usuario': usuario, 'pagina': pagina_actual})

#endregion



# region Soperte Tecnico
def soporte_tecnico(request):
    pagina_actual = "soporte_tecnico"

    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        email = request.POST.get("email")

        # Validar si la descripción no está vacía
        if descripcion and email:
            # Enviar correo
            send_mail(
                "Nuevo problema reportado",
                f"Descripción del problema:\n{descripcion}\n\nCorreo del remitente:\n{email}",
                settings.DEFAULT_FROM_EMAIL,
                ["recetarium19@gmail.com"],
                fail_silently=False,
            )
            # Mostrar mensaje de éxito
            messages.success(
                request,
                "Tu solicitud ha sido enviada correctamente. Nos pondremos en contacto contigo pronto.",
            )
            # Redirigir a una página de confirmación o regresar al formulario (según el flujo de tu aplicación)
            return redirect('/configuracion/soporte_tecnico')
        else:
            # Mostrar mensaje de error si la descripción o el email están vacíos
            messages.error(
                request, "Por favor proporciona una descripción del problema y tu correo electrónico."
            )

    # Renderizar la plantilla del formulario
    return render(request, "soporte/soporte_tecnico.html", {"pagina": pagina_actual})
    # Renderizar el formulario inicial si no es método POST o si hay errores

#endregion

#region RECETAS DISPONIBLES

def lista_recetas(request):
    recetas = Receta.objects.all()
    recetas_desayuno = recetas.filter(categoria="Desayuno")
    recetas_entradas = recetas.filter(categoria="Entrante")
    recetas_platos_principales = recetas.filter(categoria="Plato Principal")
    recetas_postres = recetas.filter(categoria="Postre")
    recetas_sopas = recetas.filter(categoria="Sopa")

    context = {
        'recetas': recetas,
        'recetas_desayuno': recetas_desayuno,
        'recetas_entradas': recetas_entradas,
        'recetas_platos_principales': recetas_platos_principales,
        'recetas_postres': recetas_postres,
        'recetas_sopas': recetas_sopas,

    }
    return render(request, 'recetas_disponibles/lista_recetas.html', context)

def detalle_receta(request, id_receta):
    pagina_actual = "detalle_receta"
    receta = get_object_or_404(Receta, pk=id_receta)
    comentarios = receta.comentarios.all()

    if request.method == 'POST':
        if 'contenido' in request.POST:
            contenido = request.POST.get('contenido')
            if contenido and request.user.is_authenticated:
                Comentario.objects.create(
                    receta=receta,
                    usuario=request.user,
                    contenido=contenido
                )
            return redirect('detalle_receta', id_receta=id_receta)

        if 'me_gusta' in request.POST:
            if request.user.is_authenticated:
                # Manejo de "me gusta" en receta
                receta_id = request.POST.get('receta_id')
                if receta_id:
                    receta = get_object_or_404(Receta, pk=receta_id)
                    me_gusta, created = MeGusta.objects.get_or_create(
                        receta=receta,
                        usuario=request.user
                    )
                    if not created:
                        me_gusta.delete()
                    else:
                        # Crear una notificación si el usuario que le dio "me gusta" es diferente al autor de la receta
                        if receta.usuario != request.user:
                            mensaje = f"{request.user.username} le dio 'me gusta' a tu receta: {receta.nombre_plato}."
                            Notificacion.objects.create(
                                usuario=receta.usuario,
                                mensaje=mensaje,
                                fecha_creacion=timezone.now()
                            )

                    # Actualiza el conteo de "me gusta" en el modelo Receta
                    receta_me_gusta_count = MeGusta.objects.filter(receta=receta).count()
                    receta.me_gusta = receta_me_gusta_count
                    receta.save()
                    
                    return redirect('detalle_receta', id_receta=id_receta)

                # Manejo de "me gusta" en comentario
                comentario_id = request.POST.get('comentario_id')
                if comentario_id:
                    comentario = get_object_or_404(Comentario, pk=comentario_id)
                    me_gusta, created = MeGusta.objects.get_or_create(
                        comentario=comentario,
                        usuario=request.user
                    )
                    if not created:
                        me_gusta.delete()
                    else:
                        # Crear una notificación si el usuario que le dio "me gusta" es diferente al autor del comentario
                        if comentario.usuario != request.user:
                            mensaje = f"{request.user.username} le dio 'me gusta' a tu comentario."
                            Notificacion.objects.create(
                                usuario=comentario.usuario,
                                mensaje=mensaje,
                                fecha_creacion=timezone.now()
                            )

                    # Actualiza el conteo de "me gusta" para el comentario
                    comentario_me_gusta_count = MeGusta.objects.filter(comentario=comentario).count()
                    comentario.me_gusta = comentario_me_gusta_count
                    comentario.save()
                    
                    return redirect('detalle_receta', id_receta=id_receta)

    # Contar el total de "Me gusta" para cada comentario
    for comentario in comentarios:
        comentario.me_gusta_count = MeGusta.objects.filter(comentario=comentario).count()
    
    receta_me_gusta_count = MeGusta.objects.filter(receta=receta).count()

    return render(request, "recetas_disponibles/detalle_receta.html", {
        "receta": receta,
        "pagina": pagina_actual,
        "comentarios": comentarios,
        "receta_me_gusta_count": receta_me_gusta_count
    })


def receta_crear(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    pagina_actual = "receta_crear"
    if request.method == 'POST':
        nombre_plato = request.POST.get('nombre_plato')
        categoria = request.POST.get('categoria')
        temporada = request.POST.get('temporada')
        origen = request.POST.get('origen')
        ingredientes = request.POST.get('ingredientes')
        descripcion = request.POST.get('descripcion')
        instrucciones = request.POST.get('instrucciones')
        tiempo_preparacion = request.POST.get('tiempo_preparacion')
        dificultad = request.POST.get('dificultad')
        imagen = request.FILES.get('imagen')  

        usuario = request.user

        nueva_receta = Receta(
            nombre_plato=nombre_plato,
            categoria=categoria,
            temporada=temporada,
            origen=origen,
            ingredientes=ingredientes,
            descripcion=descripcion,
            instrucciones=instrucciones,
            tiempo_preparacion=tiempo_preparacion,
            dificultad=dificultad,
            imagen=imagen,
            usuario=usuario  # Asignar el usuario actual
        )

        # Guardar la receta en la base de datos
        nueva_receta.save()
    
        return redirect('lista_recetas')
    else:
        # Manejar el caso de solicitud GET si es necesario
        return render(request, 'recetas_disponibles/receta_crear.html', {"pagina": pagina_actual})
    
def crear_ver(request):
    pagina_actual = "apartado_recetas"
    return render(request,'recetas_disponibles/apartado_recetas.html',{'pagina':pagina_actual})

def recetas_usuarios(request, usuario_id):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    pagina_actual = "recetas_usuarios"
    user = get_object_or_404(MiUsuario, id=usuario_id)
    recetas_usuario = Receta.objects.filter(usuario=user)
    return render(
        request,
        "recetas_disponibles/recetas_usuarios.html",
        {"user": user, "recetas_usuario": recetas_usuario, "pagina":pagina_actual},
    )

def actualizar_recetas_usuarios(request, id_receta):
    receta = get_object_or_404(Receta, id_receta=id_receta)
    
    if request.method == 'GET':
        data = {
            'nombre_plato': receta.nombre_plato,
            'categoria': receta.categoria,
            'temporada': receta.temporada,
            'origen': receta.origen,
            'ingredientes': receta.ingredientes,
            'descripcion': receta.descripcion,
            'instrucciones': receta.instrucciones,
            'tiempo_preparacion': receta.tiempo_preparacion,
            'dificultad': receta.dificultad,
        }
        return JsonResponse(data)

    elif request.method == 'POST':
        receta.nombre_plato = request.POST['nombre_plato']
        receta.categoria = request.POST['categoria']
        receta.temporada = request.POST['temporada']
        receta.origen = request.POST['origen']
        receta.ingredientes = request.POST['ingredientes']
        receta.descripcion = request.POST['descripcion']
        receta.instrucciones = request.POST['instrucciones']
        receta.tiempo_preparacion = request.POST['tiempo_preparacion']
        receta.dificultad = request.POST['dificultad']
        receta.save()

        usuario_id = receta.usuario.id

        return redirect(reverse('recetas_usuarios', args=[usuario_id]))


def eliminar_receta_usuarios(request, pk):
    try:
        receta = get_object_or_404(Receta, pk=pk)

        if request.method == "POST":
            receta.delete()
            return JsonResponse({'success': True, 'message': 'Receta eliminada.'})
        
        return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)
    
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

#region Comentarios Usuario
def comentUser(request, usuario_id):
    user = get_object_or_404(MiUsuario, id=usuario_id)
    comentarios = Comentario.objects.filter(usuario=user)
    return render(request, 'usuarios/mi_perfil.html', {'user': user, 'comentarios': comentarios})
#endregion


#region Plan Nutricional (Calendario)

def crear_plan(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")

    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        # Crear una instancia del modelo PlanNutricional
        plan = PlanNutricional(nombre=nombre, user=request.user)
        
        # Asignar los datos del formulario a los campos del modelo
        meals = ['desayuno', 'media_manana', 'almuerzo', 'merienda', 'cena']
        days = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
        
        for meal in meals:
            for day in days:
                field_name = f'{meal}_{day}'
                setattr(plan, field_name, request.POST.get(field_name, ''))
        
        # Guardar el plan en la base de datos
        plan.save()
        
        messages.success(request, '¡Calendario creado correctamente!')

    # En caso de GET, pasar datos necesarios a la plantilla
    meals = [
        {'name': 'desayuno'},
        {'name': 'media_manana'},
        {'name': 'almuerzo'},
        {'name': 'merienda'},
        {'name': 'cena'}
    ]
    days = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
    
    return render(request, 'salud_nutricion/plan_nutricional/plan_nutricional.html', {'meals': meals, 'days': days})

def ver_calendarios(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    
    # Obtener todos los calendarios del usuario actual
    calendarios = PlanNutricional.objects.filter(user=request.user)
    
    return render(request, 'salud_nutricion/plan_nutricional/ver_calendarios_por_usuario.html', {
        'calendarios': calendarios,
    })


def ver_calendario(request, id):
    calendario = get_object_or_404(PlanNutricional, id=id)
    return render(request, 'salud_nutricion/plan_nutricional/calendarios_detalle.html', {'calendario': calendario})

def Eliminar_Plan(request,id_plan):
    plan = PlanNutricional.objects.filter(id=id_plan)
    plan.delete()
    return redirect('/ver_calendarios/')

def generar_pdf(request, calendario_id):
    # Obtener el objeto calendario
    calendario = get_object_or_404(PlanNutricional, id=calendario_id)
    
    # Configurar la respuesta HTTP con el nombre del calendario
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{calendario.nombre}.pdf"'
    
    # Crear el documento PDF
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Definir estilos
    styles = getSampleStyleSheet()
    
    # Registrar la fuente Lobster
    pdfmetrics.registerFont(TTFont('Lobster', 'ReceFy/Public/Fonts/Lobster-Regular.ttf'))  # Cambia la ruta al archivo de la fuente

    # Crear un estilo para el título del calendario
    title_style = ParagraphStyle(
        name='CalendarTitleStyle',
        fontName='Lobster',  # Usa la fuente Lobster
        fontSize=14,
        leading=12,  # Reduce el espacio entre líneas
        leftIndent=20,  # Alejamiento del borde izquierdo
    )

    # Crear un estilo para el título "ReceFy" con la misma fuente y tamaño
    recefy_style = ParagraphStyle(
        name='ReceFyStyle',
        fontName='Lobster',  # Cambia la fuente a Lobster
        fontSize=14,
        leading=12,  # Reduce el espacio entre líneas
        textColor=colors.HexColor('#28a56b'),  # Color verde
        alignment=2,  # Alineado a la derecha
    )

    # Crear los párrafos de los títulos
    calendar_title = Paragraph(calendario.nombre, title_style)
    recefy_title = Paragraph("ReceFy", recefy_style)

    # Crear una tabla para alinear los títulos
    title_table = Table([[calendar_title, recefy_title]], colWidths=[doc.width * 0.45, doc.width * 0.45])
    title_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Alineación vertical en la parte superior
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación horizontal centrada
    ]))
    
    elements.append(title_table)

    # Añadir un pequeño espaciador después de los títulos
    elements.append(Spacer(1, 0.2 * inch))  # Ajusta la altura según lo necesites

    # Crear una tabla de comidas
    small_font_style = ParagraphStyle(
        name='SmallFontStyle',
        fontSize=8,
        leading=10,
        spaceAfter=5,
    )

    meal_data = [
        ['Comida', 'Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        ['Desayuno', 
         Paragraph(str(calendario.desayuno_domingo), small_font_style),
         Paragraph(str(calendario.desayuno_lunes), small_font_style),
         Paragraph(str(calendario.desayuno_martes), small_font_style),
         Paragraph(str(calendario.desayuno_miercoles), small_font_style),
         Paragraph(str(calendario.desayuno_jueves), small_font_style),
         Paragraph(str(calendario.desayuno_viernes), small_font_style),
         Paragraph(str(calendario.desayuno_sabado), small_font_style)],
        ['Media Mañana', 
         Paragraph(str(calendario.media_manana_domingo), small_font_style),
         Paragraph(str(calendario.media_manana_lunes), small_font_style),
         Paragraph(str(calendario.media_manana_martes), small_font_style),
         Paragraph(str(calendario.media_manana_miercoles), small_font_style),
         Paragraph(str(calendario.media_manana_jueves), small_font_style),
         Paragraph(str(calendario.media_manana_viernes), small_font_style),
         Paragraph(str(calendario.media_manana_sabado), small_font_style)],
        ['Almuerzo', 
         Paragraph(str(calendario.almuerzo_domingo), small_font_style),
         Paragraph(str(calendario.almuerzo_lunes), small_font_style),
         Paragraph(str(calendario.almuerzo_martes), small_font_style),
         Paragraph(str(calendario.almuerzo_miercoles), small_font_style),
         Paragraph(str(calendario.almuerzo_jueves), small_font_style),
         Paragraph(str(calendario.almuerzo_viernes), small_font_style),
         Paragraph(str(calendario.almuerzo_sabado), small_font_style)],
        ['Merienda', 
         Paragraph(str(calendario.merienda_domingo), small_font_style),
         Paragraph(str(calendario.merienda_lunes), small_font_style),
         Paragraph(str(calendario.merienda_martes), small_font_style),
         Paragraph(str(calendario.merienda_miercoles), small_font_style),
         Paragraph(str(calendario.merienda_jueves), small_font_style),
         Paragraph(str(calendario.merienda_viernes), small_font_style),
         Paragraph(str(calendario.merienda_sabado), small_font_style)],
        ['Cena', 
         Paragraph(str(calendario.cena_domingo), small_font_style),
         Paragraph(str(calendario.cena_lunes), small_font_style),
         Paragraph(str(calendario.cena_martes), small_font_style),
         Paragraph(str(calendario.cena_miercoles), small_font_style),
         Paragraph(str(calendario.cena_jueves), small_font_style),
         Paragraph(str(calendario.cena_viernes), small_font_style),
         Paragraph(str(calendario.cena_sabado), small_font_style)],
    ]

    # Crear la tabla de comidas con columnas más estrechas
    meal_table = Table(meal_data, colWidths=[doc.width * 0.12] * 8)
    meal_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4CAF50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#fafafa')),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#f9f9f9')),
        ('BACKGROUND', (0, 2), (-1, 2), colors.white),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#f9f9f9')),
        ('BACKGROUND', (0, 4), (-1, 4), colors.white),
        ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor('#f9f9f9')),
        ('BACKGROUND', (0, 6), (-1, 6), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ]))

    # Añadir la tabla de comidas
    elements.append(meal_table)

    # Añadir un espaciador grande antes de la fecha de creación
    elements.append(Spacer(1, 0.6 * inch))  # Ajusta la altura según lo necesites

    # Crear un estilo para la fecha de creación
    date_style = ParagraphStyle(
        name='DateStyle',
        fontName='Helvetica',
        fontSize=10,
        alignment=1,  # Alineado al centro
    )

    # Añadir la fecha de creación centrada
    creation_date = Paragraph(f"Fecha de creación: {calendario.fecha_creacion.strftime('%d/%m/%Y')}", date_style)
    elements.append(creation_date)

    # Construir el PDF
    doc.build(elements)

    return response



#endregion

#region Dietas Disponibles

def lista_dietas(request):
    dietas = Dieta.objects.all()
    dietas_subir_peso = Dieta.objects.filter(categoria='Dieta para subir de peso')
    dietas_bajar_peso = Dieta.objects.filter(categoria='Dieta para bajar de peso')
    dietas_deshidratacion = Dieta.objects.filter(categoria='Deshidratacion')
    dietas_cardiovasculares = Dieta.objects.filter(categoria='Cardiovascular')
    dietas_diabetes = Dieta.objects.filter(categoria='Diabetes')

    context = {
        'dietas': dietas,
        'dietas_subir_peso': dietas_subir_peso,
        'dietas_bajar_peso': dietas_bajar_peso,
        'dietas_deshidratacion': dietas_deshidratacion,
        'dietas_cardiovasculares': dietas_cardiovasculares,
        'dietas_diabetes': dietas_diabetes,

    }
    return render(request, 'salud_nutricion/dietas_disponibles/lista_dietas.html', context)


def detalle_dietas(request, id_dietas):
    pagina_actual = "detalle_dietas"
    dieta = get_object_or_404(Dieta, pk=id_dietas)
    comentarios = dieta.comentarios.all()

    if request.method == 'POST':
       
        if 'contenido' in request.POST:
            contenido = request.POST.get('contenido')
            if contenido.strip() and request.user.is_authenticated: 
                Comentario.objects.create(
                    dieta=dieta,
                    usuario=request.user,
                    contenido=contenido
                )
            return redirect('detalle_dietas', id_dietas=id_dietas)

        if 'me_gusta' in request.POST:
            if request.user.is_authenticated:
                dieta_id = request.POST.get('dieta_id')
                if dieta_id:
                    dieta = get_object_or_404(Dieta, pk=dieta_id)
                    me_gusta, created = MeGusta.objects.get_or_create(
                        dieta=dieta,
                        usuario=request.user
                    )
                    if not created:
                        me_gusta.delete()  
                    dieta_me_gusta_count = MeGusta.objects.filter(dieta=dieta).count()
                    dieta.me_gusta = dieta_me_gusta_count
                    dieta.save()

                    return redirect('detalle_dietas', id_dietas=id_dietas)

        if 'me_gusta_comentario' in request.POST:
            comentario_id = request.POST.get('comentario_id')
            if comentario_id:
                comentario = get_object_or_404(Comentario, pk=comentario_id)
                me_gusta, created = MeGusta.objects.get_or_create(
                    comentario=comentario,
                    usuario=request.user
                )
                if not created:
                    me_gusta.delete()

                comentario.me_gusta = MeGusta.objects.filter(comentario=comentario).count()
                comentario.save()

                return redirect('detalle_dietas', id_dietas=id_dietas)

    for comentario in comentarios:
        comentario.me_gusta_count = MeGusta.objects.filter(comentario=comentario).count()

    dieta_me_gusta_count = MeGusta.objects.filter(dieta=dieta).count()

    return render(request, "salud_nutricion/dietas_disponibles/detalle_dietas.html", {
        "dieta": dieta, 
        "comentarios": comentarios,
        "pagina": pagina_actual,
        "dieta_me_gusta_count": dieta_me_gusta_count,
    })


#endregion

#region Panel Administrativo

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    total_usuarios = MiUsuario.objects.count()
    total_consejeros = Consejero.objects.count()
    total_recetas = Receta.objects.count()
    total_dietas = Dieta.objects.count()
    total_ingredientes = Ingrediente.objects.count()
    total_licencias = Licencias.objects.count()

    context = {
        "total_usuarios": total_usuarios,
        "total_consejeros": total_consejeros,
        "total_recetas": total_recetas,
        "total_dietas": total_dietas,
        "total_ingredientes": total_ingredientes,
        "total_licencias": total_licencias,
    }

    consejeros_recientes = Consejero.objects.order_by('-fecha_registro')[:3]
    recetas_recientes = Receta.objects.order_by('-fecha_registro_receta')[:3]
    dietas_recientes = Dieta.objects.order_by('-fecha_registro_dieta')[:3]
    usuarios_recientes = MiUsuario.objects.order_by('-date_joined')[:3]
    comentarios_recientes = Comentario.objects.order_by('-fecha_creacion')[:3]
    ingredientes_recientes = Ingrediente.objects.order_by('-fecha_registro_ingredientes')[:3]

    context = {
        'total_usuarios': total_usuarios,
        'total_consejeros': total_consejeros,
        'total_recetas': total_recetas,
        'total_dietas': total_dietas,
        'total_ingredientes': total_ingredientes,

        'consejeros_recientes': consejeros_recientes,
        'comentarios_recientes': comentarios_recientes,
        'usuarios_recientes': usuarios_recientes,
        'recetas_recientes': recetas_recientes,
        'dietas_recientes': dietas_recientes,
        'ingredientes_recientes': ingredientes_recientes,
    }


    return render(request, 'administracion/Home_Administracion.html', context)

#estadisticas
def Estadisticas_generales(request):
    # Obtener los totales de los diferentes modelos
    total_usuarios = MiUsuario.objects.count()
    total_consejeros = Consejero.objects.count()
    total_recetas = Receta.objects.count()
    total_dietas = Dieta.objects.count()
    total_ingredientes = Ingrediente.objects.count()

    # Crear el diccionario de contexto
    context = {
        "total_usuarios": total_usuarios,
        "total_consejeros": total_consejeros,
        "total_recetas": total_recetas,
        "total_dietas": total_dietas,
        "total_ingredientes": total_ingredientes,
    }

    plt.switch_backend('Agg')

    fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
    labels = ['Usuarios', 'Consejeros', 'Recetas', 'Dietas', 'Ingredientes']
    totals = [total_usuarios, total_consejeros, total_recetas, total_dietas, total_ingredientes]

    bars = ax.bar(labels, totals, color='none', edgecolor=['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'], linewidth=2, width=0.5)

    ax.set_xlabel('Categorías', fontsize=12, fontweight='bold', color='#333333')
    ax.set_ylabel('Totales', fontsize=12, fontweight='bold', color='#333333')
    ax.set_title('Totales por Categoría', fontsize=14, fontweight='bold', color='#333333')
    ax.tick_params(axis='both', which='major', labelsize=10, colors='#333333')

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), va='bottom', ha='center', fontsize=10, fontweight='bold', color='#333333')

    # Configuración de ejes y fondo
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['left'].set_linewidth(1)
    ax.spines['bottom'].set_color('#cccccc')
    ax.spines['bottom'].set_linewidth(1)
    
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#f9f9f9')

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', transparent=True)
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')

    context['graphic'] = graphic

    return render(request, "administracion/cruds/estadisticas/general.html", context)


#fin estadisticas 

#CRUD CONSEJEROS
def listar_consejeros(request):
    usuarios_ids = UsuarioRol.objects.filter(rol_id=7).values_list('usuario_id', flat=True)
    
    consejeros = Consejero.objects.filter(usuario__id__in=usuarios_ids).order_by('-fecha_registro')
    
    paginator = Paginator(consejeros, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'consejeros': page_obj,
        'paginator': paginator
    }
    return render(request, 'administracion/cruds/consejeros/listar.html', context)

def cambiar_rol(request, usuario_id):
    usuario_rol = get_object_or_404(UsuarioRol, usuario_id=usuario_id)
    
    usuario_rol.rol_id = 6
    usuario_rol.save()
    
    if usuario_rol.rol_id == 6:
        Consejero.objects.filter(usuario=usuario_rol.usuario).delete()
    
    return redirect('/administracion/roles/listado/')
    


def ver_consejero(request, consejero_id):
    consejero = Consejero.objects.filter(id_consejero=consejero_id).first()
    if not consejero:
        messages.error(request, "Consejero no encontrado.")
        return redirect("listar_consejeros")
    
    return render(request, "administracion/cruds/consejeros/ver_consejero.html", {"consejero": consejero})

#FIN CRUD CONSEJEROS

#CRUD RECETAS

def listar_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_registro_receta')
    
    paginator = Paginator(recetas, 15) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'recetas': page_obj,
        'paginator': paginator
    }
    return render(request, 'administracion/cruds/recetas/listar.html', context)

def insertar_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receta creada exitosamente.')
            return redirect('listar_recetas')
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = RecetaForm()

    return render(request, "administracion/cruds/recetas/insertar.html", {"form": form})

def borrar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)

    if request.method == "POST":
        receta.delete()
        messages.success(request, "¡La receta ha sido eliminado correctamente!")
        return redirect("listar_recetas")

    messages.error(request, "Método no permitido")
    return redirect("listar_recetas")

def actualizar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    
    if request.method == "POST":
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect("listar_recetas")
    else:
        form = RecetaForm(instance=receta)

    context = {
        "form": form,
        "receta": receta,
    }
    return render(request, "administracion/cruds/recetas/actualizar.html", context)

def ver_receta(request, receta_id):
    receta = Receta.objects.filter(id_receta=receta_id).first()
    if not receta:
        messages.error(request, "Ingrediente no encontrado.")
        return redirect("listar_recetas")
    
    return render(request, "administracion/cruds/recetas/ver_receta.html", {"receta": receta})


#FIN CRUD RECETAS

#CRUD DIETAS

def listar_dietas(request):
    dietas = Dieta.objects.all().order_by('-fecha_registro_dieta')
    return render(request, "administracion/cruds/dietas/listar.html", {"dietas": dietas})

def insertar_dieta(request):
    if request.method == "POST":
        form = DietaForm(request.POST, request.FILES)
        if form.is_valid():
            dieta = form.save(commit=False)
            dieta.usuario = form.cleaned_data['usuario_id']
            dieta.consejero = form.cleaned_data['consejero_id']
            dieta.save()  # Guarda la dieta con los campos correctos
            messages.success(request, 'Dieta creada exitosamente.')
            return redirect('listar_dietas')
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = DietaForm()

    return render(request, "administracion/cruds/dietas/insertar.html", {"form": form})

def borrar_dieta(request, pk):
    dieta = get_object_or_404(Dieta, pk=pk)

    if request.method == "POST":
        dieta.delete()
        messages.success(request, "¡La dieta ha sido eliminado correctamente!")
        return redirect("listar_dietas")

    messages.error(request, "Método no permitido")
    return redirect("listar_dietas")

def actualizar_dieta(request, pk):
    dieta = get_object_or_404(Dieta, pk=pk)
    
    if request.method == "POST":
        form = DietaForm(request.POST, request.FILES, instance=dieta)
        if form.is_valid():
            form.save()
            return redirect("listar_dietas")
    else:
        form = DietaForm(instance=dieta)

    context = {
        "form": form,
        "dieta": dieta,
    }
    
    return render(request, "administracion/cruds/dietas/actualizar.html", context)

def ver_dieta(request, dieta_id):
    dieta = Dieta.objects.filter(id=dieta_id).first()
    if not dieta:
        messages.error(request, "Dieta no encontrado.")
        return redirect("listar_dietas")
    
    return render(request, "administracion/cruds/dietas/ver_dieta.html", {"dieta": dieta})

#FIN CRUD DIETAS

#CRUD INGREDIENTES

def listado_ingredientes(request):
    ingredientes = Ingrediente.objects.all().order_by('-fecha_registro_ingredientes')
    return render(request, "administracion/cruds/ingredientes/listar.html", {"ingredientes": ingredientes})

def insertar_ingrediente(request):
    if request.method == "POST":
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("listado_ingredientes"))
    else:
        form = IngredienteForm()

    context = {"form": form}
    return render(request, "administracion/cruds/ingredientes/insertar.html", context)

def actualizar_ingrediente(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    
    if request.method == "POST":
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect("listado_ingredientes")
    else:
        form = IngredienteForm(instance=ingrediente)

    context = {
        "form": form,
        "ingrediente": ingrediente,
    }
    
    return render(request, "administracion/cruds/ingredientes/actualizar.html", context)

def borrar_ingrediente(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == "POST":
        ingrediente.delete()
        messages.success(request, "¡El ingrediente ha sido eliminado correctamente!")
        return redirect("listado_ingredientes")

    messages.error(request, "Método no permitido")
    return redirect("listado_ingredientes")

def ver_ingrediente(request, ingrediente_id):
    ingrediente = Ingrediente.objects.filter(id_ingrediente=ingrediente_id).first()
    if not ingrediente:
        messages.error(request, "Ingrediente no encontrado.")
        return redirect("listado_ingredientes")
    
    return render(request, "administracion/cruds/ingredientes/ver_ingrediente.html", {"ingrediente": ingrediente})


#FIN CRUD INGREDIENTES

#region CRUD ROLES
def listado_roles(request):
    roles = Rol.objects.all()  
    usuarios_roles = UsuarioRol.objects.all()   
    return render(request, "administracion/cruds/roles/listar.html", {"roles": roles, 'usuarios_roles': usuarios_roles } )


def insertar_roles(request):
    if request.method == "POST":
        if (
            request.POST.get("nombre")
            and request.POST.get("descripcion")
            and request.POST.get("permisos")
        ):
            roles = Rol()
            roles.nombre = request.POST.get("nombre")
            roles.descripcion = request.POST.get("descripcion")
            roles.permisos = request.POST.get("permisos")
            roles.save()
            return redirect("/administracion/roles/listado")
        else:
            return render(request, "crud_roles/insertar.html")
    else:
        return render(request, "administracion/cruds/roles/insertar.html")

def borrar_rol(request, idroles):
    roles = Rol.objects.filter(id=idroles)
    roles.delete()
    return redirect("/administracion/roles/listado")

def actualizar_rol(request, idroles):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        permisos = request.POST.get("permisos")

        if nombre and descripcion and permisos:
            roles = Rol.objects.get(id=idroles)
            roles.nombre = nombre
            roles.descripcion = descripcion
            roles.permisos = permisos
            roles.save()
            return redirect("/administracion/roles/listado")
    else:
        roles = Rol.objects.get(id=idroles)
        return render(request, "administracion/cruds/roles/actualizar.html", {"roles": roles})

def editarRolu(request, idinter):
    if request.method == "POST":
        usuario_id = request.POST.get('usuario_id')
        rol_id = request.POST.get('rol_id')
        
        if usuario_id and rol_id:
            mant = UsuarioRol.objects.get(id=idinter)
            
            nuevo_usuario = MiUsuario.objects.get(id=usuario_id)
            nuevo_rol = Rol.objects.get(id=rol_id)
            
            mant.usuario = nuevo_usuario
            mant.rol = nuevo_rol
            mant.save()
            
            if rol_id == '7': 
                if not Consejero.objects.filter(usuario=nuevo_usuario).exists():
                    Consejero.objects.create(
                        usuario=nuevo_usuario,
                        titulacion="Título por defecto",
                        categoria="Categoría por defecto",
                        experiencia="Experiencia por defecto",
                        descripcion="Descripción por defecto",
                        fecha_registro=datetime.now()
                    )
            elif rol_id == '6':
                Consejero.objects.filter(usuario=nuevo_usuario).delete()
            
            return redirect('/administracion/roles/listado')
    
    mant = UsuarioRol.objects.get(id=idinter)
    usuario = MiUsuario.objects.all()
    rol = Rol.objects.all()
    return render(request, 'administracion/cruds/roles/editarRolu.html',{"mant": mant, "usuario": usuario, "rol": rol})
#FIN CRUD ROLES

#CRUD USUARIOS


def listadoUsuarios(request):
    usuarios = MiUsuario.objects.all().order_by('-date_joined')

    paginator = Paginator(usuarios, 15) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'usuarios': page_obj,
        'paginator': paginator
    }

    return render(request, 'administracion/cruds/usuarios/listar.html', context)

def borrarUsuario(request, idusuario):
    usuario = MiUsuario.objects.filter(id=idusuario)
    usuario.delete()
    return redirect('/administracion/usuarios/listado/')

def actualizarUsuario(request, idusuario):
    usuario = get_object_or_404(MiUsuario, id=idusuario)
    if request.method == "POST":
        imagen2 = request.FILES.get('imagen2')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        biografia = request.POST.get('biografia')
        pais = request.POST.get('pais')
        idioma = request.POST.get('idioma')
        telefono = request.POST.get('telefono')

        if username and first_name and last_name and email and fecha_nacimiento and biografia and pais and idioma and telefono:
            usuario.username = username
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.email = email
            usuario.fecha_nacimiento = fecha_nacimiento
            usuario.biografia = biografia
            usuario.pais = pais
            usuario.idioma = idioma
            usuario.telefono = telefono

            if imagen2:
                usuario.imagen2 = imagen2 
                
            usuario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Faltan campos obligatorios.'}, status=400)
    
    return render(request, 'administracion/cruds/usuarios/actualizar.html', {'st': usuario})
#FIN CRUD USUARIOS

#CRUD COMENTARIOS

def listadoComentarios(request):
    comentario = Comentario.objects.all().order_by('-fecha_creacion')

    paginator = Paginator(comentario, 15) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'comentario': page_obj,
        'paginator': paginator
    }

    return render(request,'administracion/cruds/comentarios/listar.html', context)

def borrarComentario(request, idcomentario):
    comentario = Comentario.objects.filter(id=idcomentario)
    comentario.delete()
    return redirect('/administracion/comentarios/listado/')

#FIN CRUD COMENT

#CRUD LICENCIAS 

def InsertarLicencia(request):
    if request.method == "POST":
        if request.POST.get('nombre') and request.POST.get('descripcion') and request.POST.get('dias') and request.POST.get('precio'):
           licencia = Licencias()
           licencia.nombre = request.POST.get('nombre')
           licencia.descripcion = request.POST.get('descripcion')
           licencia.dias = request.POST.get('dias')
           licencia.precio = request.POST.get('precio')
           licencia.save()
           return redirect('/administracion/licencias/listado')
    else:
        return render(request, 'administracion/licencias/insertar.html') 

def licencias(request):
    licencia = Licencias.objects.all()
    inter = LicenciasInter.objects.all()
    return render(request,'administracion/licencias/listado.html',{'licencia': licencia , 'inter': inter } )


#FIN CRUD LICENCIAS

#endregion

#region Calculadora Imc

def calculadora_imc(request):
    pagina_actual = "calculadora_imc"
    dietas = None
    imc = None
    resultado = ''
    mensaje_error = ''

    if request.method == 'POST':
        estatura = request.POST.get('estatura')
        peso = request.POST.get('peso')

        # Validar entrada
        if not estatura or not peso:
            mensaje_error = 'Por favor, completa ambos campos.'
        else:
            # Convertir valores
            estatura = estatura.replace(',', '.')
            peso = peso.replace(',', '.')

            try:
                estatura = float(estatura)
                peso = float(peso)

                if estatura <= 0 or peso <= 0:
                    mensaje_error = 'Por favor, ingresa valores numéricos válidos.'
                elif estatura < 0.5 or estatura > 2.5:
                    mensaje_error = 'Por favor, ingresa una estatura válida entre 0.5 y 2.5 metros.'
                else:
                    imc = peso / (estatura * estatura)
                    if imc < 18.5:
                        resultado = 'Bajo peso'
                        dietas = Dieta.objects.filter(categoria='Dieta para subir de peso')
                    elif imc >= 18.5 and imc <= 24.9:
                        resultado = 'Normal'
                        dietas = Dieta.objects.filter(categoria='Dieta Mantener peso')
                    elif imc >= 25 and imc <= 29.9:
                        resultado = 'Sobrepeso'
                        dietas = Dieta.objects.filter(categoria='Dieta para bajar de peso')
                    else:
                        resultado = 'Obesidad'
                        dietas = Dieta.objects.filter(categoria='Dieta para bajar de peso')
            except ValueError:
                mensaje_error = 'Por favor, ingresa valores numéricos válidos.'

    return render(request, "salud_nutricion/calculadora_imc/calculadora.html", {
        "pagina": pagina_actual,
        "imc": imc,
        "resultado": resultado,
        "dietas": dietas,
        "mensaje_error": mensaje_error,
    })

#endregion

#region Consejeros

def optionsConsejeros(request):
    pagina_actual = "options"
    return render(request,'consejeros/option.html',{"pagina": pagina_actual})

def consejeros_disponibles(request):
    consejeros = Consejero.objects.all()
    consejeros_nutricionistas = Consejero.objects.filter(categoria="Nutricionista")
    consejeros_especialistas_en_reposteria = Consejero.objects.filter(categoria="Especialista en Reposteria")
    consejeros_asesor_en_nutricion_deportiva = Consejero.objects.filter(categoria = "Asesor en Nutricion Deportiva")
    consejeros_dietista = Consejero.objects.filter(categoria = "Dietista")

    paginator = Paginator(consejeros, 15) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "consejeros": consejeros,
        "consejeros_nutricionistas": consejeros_nutricionistas,
        "consejeros_especialistas_en_reposteria": consejeros_especialistas_en_reposteria,
        "consejeros_asesor_en_nutricion_deportiva": consejeros_asesor_en_nutricion_deportiva,
        "consejeros_dietista": consejeros_dietista,
        "pagina": "consejeros_disponibles",
        'consejeros': page_obj,
        'paginator': paginator
    }

    return render(request, 'consejeros/consejeros_disponibles.html', context)

def apartado_consejeros_ver(request, consejero_id):
    consejero = get_object_or_404(Consejero, id_consejero=consejero_id)
    return render(request, 'consejeros/ver_consejeros.html', {'consejero': consejero})

#endregion


#region Mensajes Usuarios no funcional
@login_required
def lista_usuarios(request):
    usuarios = MiUsuario.objects.exclude(id=request.user.id)
    return render(request, 'chat/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def chat_view(request, usuario_id):
    receptor = get_object_or_404(MiUsuario, id=usuario_id)
    mensajes = Mensajes.objects.filter(
        (Q(emisor=request.user) & Q(receptor=receptor)) | (Q(emisor=receptor) & Q(receptor=request.user))
    ).order_by('fecha_creacion')

    return render(request, 'chat/chat.html', {'receptor': receptor, 'mensajes': mensajes})


@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        receptor_id = request.POST.get('receptor_id')
        receptor = MiUsuario.objects.get(id=receptor_id)

        mensaje = Mensajes.objects.create(
            emisor=request.user,
            receptor=receptor,
            contenido=contenido
        )

        return JsonResponse({'mensaje': mensaje.contenido, 'fecha': mensaje.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')})
    return JsonResponse({'error': 'Solicitud inválida'}, status=400)



#endregion

#region Licencias

def licencias_usuario(request):
    licencias = Licencias.objects.all()
    return render(request, 'licencias/licencias_disponibles.html', {'licencias':licencias})

#endregion 

#region Notificaciones

def buzon_notificaciones(request):
    # Obtener las notificaciones del usuario actual
    notificaciones = Notificacion.objects.filter(usuario=request.user).order_by('-fecha_creacion')

    # Si el usuario marca una notificación como leída
    if request.method == "POST":
        notificacion_id = request.POST.get("notificacion_id")
        notificacion = Notificacion.objects.get(id=notificacion_id, usuario=request.user)
        notificacion.leida = True
        notificacion.save()
        return redirect('buzon_notificaciones')

    # Renderiza la página con las notificaciones del usuario
    return render(request, 'usuarios/buzon_notificaciones.html', {
        'notificaciones': notificaciones,
        'usuario': request.user  # Pasa el usuario actual para el saludo personalizado
    })

#endregion

#region Crear Dieta Consejero

def crear_dieta_consejero(request):
    if not request.user.is_authenticated:
        return redirect("/usuarios/login")
    pagina_actual = "crear_dieta_consejero"
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        objetivo = request.POST.get('objetivo')
        calorias = request.POST.get('calorias')
        condicion_medica = request.POST.get('condicion_medica')
        valor_nutricional = request.POST.get('valor_nutricional')
        actividad_fisica = request.POST.get('actividad_fisica')
        consejos = request.POST.get('consejos')
        dispositivos = request.POST.get('dispositivos')
        bibliografia = request.POST.get('bibliografia')
        categoria = request.POST.get('categoria')
        imagen = request.FILES.get('imagen')  

        usuario = request.user

        nueva_dieta = Dieta(
            nombre=nombre,
            descripcion=descripcion,
            objetivo=objetivo,
            calorias=calorias,
            condicion_medica=condicion_medica,
            valor_nutricional=valor_nutricional,
            actividad_fisica=actividad_fisica,
            consejos=consejos,
            dispositivos=dispositivos,
            bibliografia=bibliografia,
            categoria=categoria,
            imagen=imagen,
            usuario=usuario  # Asignar el usuario actual
        )

        # Guardar la receta en la base de datos
        nueva_dieta.save()
    
        return redirect('crear_dieta_consejero')
    else:
        # Manejar el caso de solicitud GET si es necesario
        return render(request, 'consejeros/form_dieta_consejero.html', {"pagina": pagina_actual})

#endregion