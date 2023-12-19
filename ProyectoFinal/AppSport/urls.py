from django.contrib import admin
from django.urls import path
from AppSport.views import inicio_view, inicio_socio_view, inicio_actividad_view, inicio_sede_view, adminstaff_view, actividades_todas_view, sedes_todas_view, socio_crear_view, socio_registro_ok_view, socio_registro_fail_view, actividad_crear_view, actividad_registro_ok_view, actividad_registro_fail_view, sede_crear_view, sede_registro_ok_view, sede_registro_fail_view, socio_buscar_view, socios_todos_view, socio_buscar_resultado_view


app_name = "AppSport"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name='inicio'),
    path('socios/', inicio_socio_view, name='socios'),
    path('actividades/', inicio_actividad_view, name='actividades'),
    path('sedes/', inicio_sede_view, name='sedes'),
    path('adminstaff/', adminstaff_view, name='adminstaff'),
    path('actividades/todas/', actividades_todas_view, name='actividadestodas'),
    path('sedes/todas/', sedes_todas_view, name='sedestodas'),
    path('socios/todos/', socios_todos_view, name='sociostodos'),
    path('socios/registrar/', socio_crear_view, name='socioregistrar'),
    path('socios/registrar/registrook', socio_registro_ok_view, name='socioregistrook'),
    path('socios/registrar/registrofail', socio_registro_fail_view, name='socioregistrofail'),
    path('actividades/registrar/', actividad_crear_view, name='actividadregistrar'),
    path('actividades/registrar/registrook', actividad_registro_ok_view, name='actividadregistrook'),
    path('actividad/registrar/registrofail', actividad_registro_fail_view, name='actividadregistrofail'),
    path('sede/registrar/', sede_crear_view, name='sederegistrar'),
    path('sede/registrar/registrook', sede_registro_ok_view, name='sederegistrook'),
    path('sede/registrar/registrofail', sede_registro_fail_view, name='sederegistrofail'),
    path('socios/buscar/', socio_buscar_view, name='sociobuscar'),
    path('socios/buscar/resultado', socio_buscar_resultado_view, name='sociobuscarresultado'),
]
