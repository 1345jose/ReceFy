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
    path('salud-nutricion/calculadora_imc', views.calculadora_imc, name="calculadora_imc"),
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
    path('usuario/mis-comentarios/', views.comentUser, name='mis_comentarios'),
    
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
    path('plan/eliminar/<int:id_plan>', views.Eliminar_Plan, name="Eliminar_Plan"),
    path('calendario/<int:calendario_id>/pdf/', views.generar_pdf, name='generar_pdf'),
    #endregion

    #region Dietas Disponibles
    path('dietas/', views.lista_dietas, name='lista_dietas'),
    path('dietas/dieta=<int:id>/', views.detalle_dietas, name='detalle_dietas'),

    #endregion

    #region Administracion
    path("administracion/", views.dashboard, name="home_administracion"),

    #CRUD CONSEJEROS
    path("administracion/consejeros/listado/", views.listar_consejeros, name="listar_consejeros"),
    path("administracion/consejeros/insertar/", views.insertar_consejero, name="insertar_consejero"),
    path("administracion/consejeros/borrar/<int:pk>/", views.borrar_consejero, name="borrar_consejero"),
    path("administracion/consejeros/actualizar/<int:pk>/", views.actualizar_consejero, name="actualizar_consejero"),
    path("administracion/consejeros/ver/<int:consejero_id>/", views.ver_consejero, name="ver_consejero"),
    #FIN CRUD CONSEJEROS

    #CRUD RECETAS
    path("administracion/recetas/listado/", views.listar_recetas, name="listar_recetas"),
    path("administracion/recetas/insertar/", views.insertar_receta, name="insertar_receta"),
    path("administracion/recetas/borrar/<int:pk>/", views.borrar_receta, name="borrar_receta"),
    path("administracion/recetas/actualizar/<int:pk>/", views.actualizar_receta, name="actualizar_receta"),
    path("administracion/recetas/ver/<int:receta_id>/", views.ver_receta, name="ver_receta"),
    #FIN CRUD RECETAS

    #CRUD DIETAS
    path("administracion/dietas/listado/", views.listar_dietas, name="listar_dietas"),
    path("administracion/dietas/insertar/", views.insertar_dieta, name="insertar_dieta"),
    path("administracion/dietas/borrar/<int:pk>/", views.borrar_dieta, name="borrar_dieta"),
    path("administracion/dietas/actualizar/<int:pk>/", views.actualizar_dieta, name="actualizar_dieta"),
    path("administracion/dietas/ver/<int:dieta_id>/", views.ver_dieta, name="ver_dieta"),
    # FIN CRUD DIETAS

    #CRUD INGREDIENTES
    path("administracion/ingredientes/listado", views.listado_ingredientes, name="listado_ingredientes"),
    path("administracion/ingredientes/insertar/", views.insertar_ingrediente, name="insertar_ingrediente"),
    path("administracion/ingredientes/actualizar/<int:pk>/", views.actualizar_ingrediente, name="actualizar_ingrediente"),
    path("administracion/ingredientes/borrar/<int:pk>/", views.borrar_ingrediente, name="borrar_ingrediente"),
    path("administracion/ingredientes/ver/<int:ingrediente_id>/", views.ver_ingrediente, name="ver_ingrediente"),
    #FIN CRUD INGREDIENTES

    #CRUD ROLES
    path("administracion/roles/listado/", views.listado_roles, name="listado_roles"),
    path("administracion/roles/insertar/", views.insertar_roles, name="insertar_roles"),
    path("administracion/roles/borrar/<int:idroles>/", views.borrar_rol, name="borrar_rol"),
    path("administracion/roles/actualizar/<int:idroles>/" , views.actualizar_rol, name="actualizar_rol"),
    path("administracion/roles/editar/<int:idinter>/", views.editarRolu, name="editarRolu"),
    #FIN CRUD ROLES 
    
    #CRUD USUARIOS
    path("administracion/usuarios/listado/", views.listadoUsuarios, name="listado_usuarios"),
    path("administracion/usuarios/borrrar/<int:idusuario>/", views.borrarUsuario , name="borrar_usuario"),
    path("administracion/usuarios/actualizar/<int:idusuario>/", views.actualizarUsuario, name="actualizarUsuario"),
    #FIN CRUD USUARIOS

    #CRUD COMENTARIOS
    path("administracion/comentarios/listado/", views.listadoComentarios, name="listado_comentarios"),
    path("administracion/comentarios/borrar/<int:idcomentario>/", views.borrarComentario, name="borrar_comentario"),

    #FIN CRUD COMENTARIOS

    #ESTADISTICAS GENERALES

    path("administracion/estadisticas/generales/", views.Estadisticas_generales, name="estadisticas"),
    #FIN ESTADISTICAS

    #endregion

    #region Mensajes Usuarios (por terminar)

    path('usuarios/lista', views.lista_usuarios, name='lista_usuarios'),
    path('chat/<int:usuario_id>/', views.chat_view, name='chat'),
    path('chat/enviar/', views.enviar_mensaje, name='enviar_mensaje'),


    #endregion
        
    #region Consejeros

    path("consejeros/opcion/", views.optionsConsejeros, name="optionsConsejeros"),

    #endregion
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)