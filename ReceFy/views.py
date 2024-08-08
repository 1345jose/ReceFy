from django.shortcuts import render, redirect
from .models import MiUsuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
    return render(request, "salud_nutricion.html", {"pagina": pagina_actual})

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
        if request.POST.get('biografia') and request.POST.get('telefono') and request.POST.get('fecha_nacimiento') and request.POST.get('edad') and request.POST.get('pais') and request.POST.get('idioma'):
            act = MiUsuario.objects.get(id=idusuario)
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
        usuario = request.user  # Obtenemos el usuario actual
        
        # Actualizamos la imagen 'imagen2' si está presente en el formulario
        if request.FILES.get('imagen2'):
            usuario.imagen2 = request.FILES.get('imagen2')

        # Guardamos los cambios en la base de datos
        usuario.save()

    return render(request, 'configuracion/imagenes_usuario.html')

#endregion
