from django.shortcuts import render, redirect
from .models import MiUsuario, Receta
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse





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
    if request.method == "POST":
        email = request.POST.get("email")
        User = get_user_model()

        if email:
            try:
                # Buscar el usuario por correo electrónico
                user = User.objects.get(email=email)

                # Generar la URL para actualizar la contraseña con el ID del usuario
                password_update_url = request.build_absolute_uri(
                    reverse('passwordUpdate', kwargs={'idusuario': user.id})
                )

                # Mensaje en texto plano (opcional)
                plain_message = (
                    f"De: Grupo ReceFy\n"
                    f"Correo para: {email}\n\n"
                    "Hola, Recupera tu contraseña en el siguiente link: "
                    f"{password_update_url}"
                )

                # Mensaje en HTML con la URL personalizada
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

                # Enviar correo con HTML
                send_mail(
                    "Recuperación de Contraseña",
                    plain_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                    html_message=html_message, 
                )

                return redirect('/')  # Redirige al usuario después de enviar el correo
            except User.DoesNotExist:
                return render(request, 'configuracion/recuperacion_contraseña.html', {'error': 'El correo electrónico no está registrado.'})
            except Exception as e:
                # En caso de error al enviar el correo, mostrar el mensaje de error
                return render(request, 'configuracion/recuperacion_contraseña.html', {'error': str(e)})
        else:
            # Si el email no fue proporcionado, mostrar el formulario nuevamente
            return render(request, 'configuracion/recuperacion_contraseña.html', {'error': 'Por favor, proporciona un correo electrónico válido.'})
    
    # Si la solicitud no es POST, renderiza el formulario de recuperación de contraseña
    return render(request, 'configuracion/recuperacion_contraseña.html')
         
def passwordUpdate(request,idusuario):
    if request.method == "POST":
        if request.POST.get('password'):
            up = MiUsuario.objects.get(id=idusuario)
            up.set_password(request.POST.get('password'))
            up.save()
            return redirect('/usuarios/login')
    else:   
        return render(request, 'soporte/passwordUpdate.html')


#endregion


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
            return redirect("soporte_send")
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
    pagina_actual = "lista_recetas"
    
    # Obtener todas las recetas
    recetas_list = Receta.objects.all()
    
    # Renderizar la plantilla con el contexto
    return render(request, "recetas_disponibles/lista_recetas.html", {
        "recetas": recetas_list,
        "pagina": pagina_actual
    })

def detalle_receta(request, id_receta):
    pagina_actual = "detalle_receta"
    receta = Receta.objects.get(pk=id_receta)
    return render(request, "recetas_disponibles/detalle_receta.html", {"receta": receta, "pagina": pagina_actual})


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
#endregion

