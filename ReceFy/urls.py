"""
URL configuration for ReceFy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ReceFy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ,name="index"),
    path('novedades/', views.apartado_novedades, name="apartado_novedades"),
    
    
    #region Salud Nutricion
    path('salud-nutricion/', views.salud_nutricion, name="salud_nutricion"),
    #endregion



    #region Recetas Disponibles
    path('recetas/', views.lista_recetas, name="lista_recetas"),
    path('detalle_receta/<int:id_receta>', views.detalle_receta, name="detalle_receta"),
    path('recetas/crear', views.receta_crear, name="crear_receta"),
    path("recetas/apartado",views.crear_ver,name="crear_ver"),
    path('recetas/<int:usuario_id>/tus_recetas/', views.recetas_usuarios, name='recetas_usuarios'),


    #endregion
    
    #region Usuarios
    path('usuarios/registro', views.registro_usuario, name="registro_usuario"),
    path('usuarios/login', views.loginusuarios, name="login"),
    path('usuarios/logout', views.logoutusuarios, name='logout'),
    path('usuarios/mi_perfil', views.mi_perfil,name="mi_perfil"),
    path('usuarios/completar', views.completar_info, name="completar_info"),
    path('configuracion/actualizar_info/<int:idusuario>', views.actualizar_info, name="actualizar_perfil"),
    #endregion
 
    #pruebas
    path('imagen', views.imagen2, name="imagen2"),
    
    #region Soporte y Configuracion
    path('configuracion/soporte_tecnico', views.soporte_tecnico, name="soporte"),
    path('configuracion/recuperar_contraseña', views.rest_email, name="recuperar_contraseña"),
    path('configuracion/passwordUpdate/<int:idusuario>', views.passwordUpdate, name="passwordUpdate"),
    path('configuracion/updateUser/<int:idusuario>', views.updateUser, name="updateUser"),

    #region Plan Nutricional (calendario)
    path('salud-nutricion/plan-nutricional/', views.crear_plan, name="crear_plan"),
    path('ver_calendarios/', views.ver_calendarios, name='ver_calendarios'),
    path('calendario/<int:id>/', views.ver_calendario, name='ver_calendario'),
    #endregion
         
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)