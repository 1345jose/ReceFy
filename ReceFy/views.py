from django.shortcuts import render, redirect, get_object_or_404
from .models import MiUsuario, Receta , Comentario, MeGusta, PlanNutricional
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash


def index(request):
    return render(request,'index.html')

#region Novedades
    
def apartado_novedades(request):
    pagina_actual = "informacion" 
    return render(request, "apartado_novedades.html", {"pagina": pagina_actual})

#endregion 

#region Salud Nutricion

def salud_nutricion(request):
    pagina_actual = "salud_nutricion"
    return render(request, "salud_nutricion/salud_nutricion.html", {"pagina": pagina_actual})

#endregion

#region Usuarios

def registro_usuario(request):
    pagina_actual = "registro"
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmar_contraseña = request.POST.get("confirmar_contraseña")

        # Validar que todos los campos requeridos estén presentes y las contraseñas coincidan
        if username and email and password and password == confirmar_contraseña:
            # Verificar si el correo electrónico ya está en uso
            if MiUsuario.objects.filter(email=email).exists():
                messages.error(
                    request,
                    "El correo electrónico ya está en uso. Por favor, utiliza otro.",
                )
                return render(
                    request, "usuarios/registro.html", {"pagina": pagina_actual}
                )

            # Verificar si el nombre de usuario ya está en uso
            if MiUsuario.objects.filter(username=username).exists():
                messages.error(
                    request,
                    "El nombre de usuario ya está en uso. Por favor, elige otro.",
                )
                return render(
                    request, "usuarios/registro.html", {"pagina": pagina_actual}
                )

            try:
                # Crear el usuario si el correo electrónico y el nombre de usuario son únicos
                user = MiUsuario.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                messages.success(
                    request, "¡Registro exitoso! Ahora puedes iniciar sesión."
                )
                # Renderizar la plantilla con una variable que indique que el registro fue exitoso
                return render(
                    request,
                    "usuairos/registro.html",
                    {"pagina": pagina_actual, "registro_exitoso": True},
                )
            except Exception as e:
                messages.error(request, f"Error al crear usuario: {e}")
                return render(
                    request, "usuarios/registro.html", {"pagina": pagina_actual}
                )
        else:
            # Si los campos no están completos o las contraseñas no coinciden, mostrar el formulario nuevamente con un mensaje de error
            messages.error(
                request,
                "Por favor, completa todos los campos y asegúrate de que las contraseñas coincidan.",
            )
            return render(request, "usuarios/registro.html", {"pagina": pagina_actual})

    # Si la solicitud no es POST, renderizar el formulario vacío
    return render(request, "usuarios/registro.html", {"pagina": pagina_actual})


def loginusuarios(request):
    pagina_actual = "loginusuarios"
    mensaje = ""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            try:
                # Buscar el usuario por correo electrónico
                user = MiUsuario.objects.get(email=email)
                # Autenticar utilizando el nombre de usuario del usuario encontrado
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    mensaje = "Correo Electronico o Contraseña incorrectos, Intente de nuevo"  
            except MiUsuario.DoesNotExist:
                mensaje = "Este usuario NO Exite, Por favor Registrese o Intente de nuevo"
        else:
            mensaje = "Por favor, ingrese ambos campos"

    return render(request, "usuarios/login.html", {"pagina": pagina_actual, "mensaje": mensaje})

def logoutusuarios(request):
    logout(request)
    return redirect('/')

@login_required
def mi_perfil(request):
    usuario = request.user
    return render(request,'usuarios/mi_perfil.html',{'usuario':usuario})

@login_required
def completar_info(request):
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
        return redirect('/')  
    return render(request,'usuarios/completar_info.html',{'pagina':pagina_actual})

@login_required
def actualizar_info(request, idusuario):
    pagina_actual = "configuracion"
    act = request.user
    if request.method == "POST":
        if  request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('biografia') and request.POST.get('telefono') and request.POST.get('fecha_nacimiento') and request.POST.get('edad') and request.POST.get('pais') and request.POST.get('idioma'):
            act = MiUsuario.objects.get(id=idusuario)
            act.first_name = request.POST.get('fist_name')
            act.last_name = request.POST.get('last_name')
            act.biografia = request.POST.get('biografia')
            act.telefono = request.POST.get('telefono')
            act.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            act.edad = request.POST.get('edad')
            act.pais = request.POST.get('pais')
            act.idioma = request.POST.get('idioma')
            act.save()
            return redirect('/usuarios/mi_perfil')
    else:
        act = MiUsuario.objects.filter(id=idusuario)
        return render(request,'configuracion/actualizar.html', {'act':act, 'pagina':pagina_actual})
    


@login_required
def imagen2(request):
    if request.method == "POST":
        usuario = request.user  
        if request.FILES.get('imagen2'):
            usuario.imagen2 = request.FILES.get('imagen2')
        usuario.save()
    return render(request, 'configuracion/imagenes_usuario.html')

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
                return render(request, 'configuracion/recuperacion_contraseña.html', {'error': 'El correo electrónico no está registrado.'})
            except Exception as e:
                return render(request, 'configuracion/recuperacion_contraseña.html', {'error': str(e)})
        else:
            return render(request, 'configuracion/recuperacion_contraseña.html', {'error': 'Por favor, proporciona un correo electrónico válido.'})
        
    return render(request, 'configuracion/recuperacion_contraseña.html',{'pagina':pagina_actual})

         
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
        return render(request, 'soporte/passwordUpdate.html',{'pagina':pagina_actual})

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
    
    return render(request, 'configuracion/usuario_pass_act.html', {'usuario': usuario, 'pagina': pagina_actual})

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
            return redirect('/')
        else:
            # Mostrar mensaje de error si la descripción o el email están vacíos
            messages.error(
                request, "Por favor proporciona una descripción del problema y tu correo electrónico."
            )

    # Renderizar la plantilla del formulario
    return render(request, "configuracion/soporte_tecnico.html", {"pagina_actual": pagina_actual})
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
            if contenido:
                Comentario.objects.create(
                    receta=receta,
                    usuario=request.user,
                    contenido=contenido
                )
            return redirect('detalle_receta', id_receta=id_receta)
        
        if 'me_gusta' in request.POST:
            comentario_id = request.POST.get('comentario_id')
            if comentario_id:
                comentario = get_object_or_404(Comentario, pk=comentario_id)
                
                me_gusta, created = MeGusta.objects.get_or_create(
                    comentario=comentario,
                    usuario=request.user
                )
                
                if not created:
                    me_gusta.delete()
                return redirect('detalle_receta', id_receta=id_receta)

    # Contar el total de "Me gusta" para cada comentario
    for comentario in comentarios:
        comentario.me_gusta_count = comentario.megustas.count()
    
    return render(request, "recetas_disponibles/detalle_receta.html", {
        "receta": receta, 
        "pagina": pagina_actual,  
        'comentarios': comentarios
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

#endregion

#region Comentarios Usuario
def comentUser(request, usuario_id):
    user = get_object_or_404(MiUsuario, id=usuario_id)
    comentarios = Comentario.objects.filter(usuario=user)
    return render(request, 'usuarios/mi_perfil.html', {'user': user, 'comentarios': comentarios})


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

#endregion

