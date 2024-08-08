from django.shortcuts import render

def index(request):
    return render(request,'index.html')

#region APARTADO NOVEDADES

def apartado_novedades(request):
    pagina_actual = "informacion" 
    return render(request, "apartado_novedades.html", {"pagina": pagina_actual})

#endregion 