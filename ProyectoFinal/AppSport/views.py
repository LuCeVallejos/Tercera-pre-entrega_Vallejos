from django.shortcuts import render


def inicio_view(request):
    return render(request, "AppSport/inicio.html")


def inicio_socio_view(request):
    return render(request, "AppSport/index_socios.html")


def inicio_actividad_view(request):
    return render(request, "AppSport/index_actividades.html")


def inicio_sede_view(request):
    return render(request, "AppSport/index_sedes.html")