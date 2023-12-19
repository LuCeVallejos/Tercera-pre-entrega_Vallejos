from django.shortcuts import render, redirect
from .models import Socio, Actividad, Sede
from . import models
from .forms import SocioCrearFormulario, ActividadCrearFormulario, SedeCrearFormulario

def inicio_view(request):
    return render(request, "AppSport/inicio.html")


def inicio_socio_view(request):
    return render(request, "AppSport/index_socios.html")


def inicio_actividad_view(request):
    return render(request, "AppSport/index_actividades.html")


def inicio_sede_view(request):
    return render(request, "AppSport/index_sedes.html")


def adminstaff_view(request):
    return render(request, "AppSport/index_adminstaff.html")    


def actividades_todas_view(request):
    actividades = models.Actividad.objects.all()
    context = {"actividadestodas": actividades}
    return render(request, "AppSport/index_actividades_lista.html", context)


def sedes_todas_view(request):
    sedes = models.Sede.objects.all()
    context = {"sedestodas": sedes}
    return render(request, "AppSport/index_sedes_lista.html", context)


def socio_crear_view(request):
     if request.method == "GET":
         # mostrar formulario
         contexto = {'form':SocioCrearFormulario()}
         return render(
             request,
             "AppSport/index_socio_registrar.html", context = contexto
             )
     else:
         # procesar formulario
         print (request.POST)
         formulario=SocioCrearFormulario(request.POST)
         if formulario.is_valid():
             informacion_limpia=formulario.cleaned_data
             modelo = Socio(
                 dni=informacion_limpia['dni'],
                 nombre=informacion_limpia['nombre'],
                 apellido=informacion_limpia['apellido'],
                 mail=informacion_limpia['mail'],
                 )
             modelo.save()
             return redirect('AppSport:socioregistrook')
         else:
          # Add this return statement for the case when the form is not valid
             contexto = {'form': formulario}
             return redirect(request, 'AppSport:socioregistrofail', context=contexto)
         

def socio_registro_ok_view(request):
    return render(request, "AppSport/index_socio_reg_ok.html")


def socio_registro_fail_view(request):
    return render(request, "AppSport/index_socio_reg_fail.html")


def actividad_crear_view(request):
     if request.method == "GET":
         # mostrar formulario
         contexto = {'form':ActividadCrearFormulario()}
         return render(
             request,
             "AppSport/index_actividad_registrar.html", context = contexto
             )
     else:
         # procesar formulario
         print (request.POST)
         formulario=ActividadCrearFormulario(request.POST)
         if formulario.is_valid():
             informacion_limpia=formulario.cleaned_data
             modelo = Actividad(
                 nombre=informacion_limpia['nombre'],
                 sede=informacion_limpia['sede'],
                 )
             modelo.save()
             return redirect('AppSport:socioregistrook')
         else:
          # Add this return statement for the case when the form is not valid
             contexto = {'form': formulario}
             return redirect(request, 'AppSport:socioregistrofail', context=contexto)
         

def actividad_registro_ok_view(request):
    return render(request, "AppSport/index_socio_reg_ok.html")


def actividad_registro_fail_view(request):
    return render(request, "AppSport/index_socio_reg_fail.html")


def sede_crear_view(request):
     if request.method == "GET":
         # mostrar formulario
         contexto = {'form':SedeCrearFormulario()}
         return render(
             request,
             "AppSport/index_sede_registrar.html", context = contexto
             )
     else:
         # procesar formulario
         print (request.POST)
         formulario=SedeCrearFormulario(request.POST)
         if formulario.is_valid():
             informacion_limpia=formulario.cleaned_data
             modelo = Sede(
                 sede=informacion_limpia['sede'],
                 )
             modelo.save()
             return redirect('AppSport:socioregistrook')
         else:
          # Add this return statement for the case when the form is not valid
             contexto = {'form': formulario}
             return redirect(request, 'AppSport:socioregistrofail', context=contexto)
         

def sede_registro_ok_view(request):
    return render(request, "AppSport/index_socio_reg_ok.html")


def sede_registro_fail_view(request):
    return render(request, "AppSport/index_socio_reg_fail.html")