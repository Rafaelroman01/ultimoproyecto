from django.http import HttpResponse 
from django.shortcuts import render
from Appcoder.models import Excursion, Participantes, Recreadores, Documentacion 
from Appcoder.forms import RecreadorFormulario, ExcursionFormulario


# Dependencias para resolver apertura de archivos usando rutas relativas
from viajeescolar.settings import BASE_DIR
import os


# Create your views here.
def inicio(request):
    return render(request, "Appcoder/index.html")


def excursiones(request):
    errores = ""
    # validamos tipo de peticion
    if request.method =="POST":
        # cargamos los datos en el formulario
        formulario = ExcursionFormulario(request.POST)
        
        # validamos los datos
        if formulario.is_valid():
            # Recuperamos los datos sanitizados
            data = formulario.cleaned_data
            # creamos la excursion
            pruebaexcursion = Excursion(nombre=data["nombre"],  email=data["email"])
            # Guardamos la excursion
            pruebaexcursion.save()
                
        else:
            errores = formulario.errors
                    
    # Recuperar todos los cursos de la base de datos
    excursiones = Excursion.objects.all()
    # Creamos el formulario vacio
    formulario = ExcursionFormulario()
    # Creamos el contexto
    contexto = {"listado_excursiones": excursiones, "formulario": formulario, "errores": errores}
    # Retornamos la respuesta
    return render(request, "Appcoder/excursiones.html", contexto)

def participantes(request):
    return render(request, "Appcoder/participantes.html") 

def recreadores(request):
    return render(request, "Appcoder/recreadores.html")

def creacion_recreadores(request):
    if request.method == "POST":
        formulario = RecreadorFormulario(request.POST)
        
        # Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            # Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            recreadores = Recreadores(nombre=data["nombre"], edad=data["edad"], nacimiento=data["nacimiento"])
            
            recreadores.save()
            
    
    formulario = RecreadorFormulario()
    contexto = {"formulario": formulario}
    return render(request, "Appcoder/recreadores_formularios.html", contexto)

def buscar_excursion(request):
    return render(request, "Appcoder/busqueda_excursion.html")

def resultados_busqueda_excursion(request):
    nombre_excursion= request.GET["nombre_excursion"]
    excursiones = Excursion.objects.filter(nombre__icontains=nombre_excursion)
    return render(request, "Appcoder/resultados_busqueda_excursion.html", {"excursiones": excursiones})
    

def documentacion(request):
    return render(request, "Appcoder/documentacion.html")

# Res   .


