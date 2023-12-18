from django.contrib import admin
from django.urls import path
from AppSport.views import inicio_view, inicio_socio_view, inicio_actividad_view, inicio_sede_view


app_name = "AppSport"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
    path('socios/', inicio_socio_view, name='socios'),
    path('actividades/', inicio_actividad_view, name='actividades'),
    path('sedes/', inicio_sede_view, name='sedes'),
]
