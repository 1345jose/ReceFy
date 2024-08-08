from django.shortcuts import render

def index(request):
    return render(request,'index.html')

#region Novedades

def apartado_novedades(request):
    pagina_actual = "informacion" 
    return render(request, "apartado_novedades.html", {"pagina": pagina_actual})

#endregion 

#region Salud nutricion

def salud_nutricion(request):
    pagina_actual = "salud_nutricion"
    return render(request, "salud_nutricion.html", {"pagina": pagina_actual})

#endregion