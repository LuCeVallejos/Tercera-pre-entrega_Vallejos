1) Creo la app AppSport y la registro en settings.py.
2) Corro el servidor Django
3) Defino la url de Inicio y a la view que la atiende ("inicio_view). Repito para "socios", "actividades" y "sedes" (para los cuales luego voy a definir modelos.)
4) Descargo plantilla de Bootstrap dentro de AppSport/static/AppSport
5) Primero pruebo con index y defino que las urls conduzcan cada una donde deben (Socios, Actividades, Sedes)
6) Una vez que las rutas están definidas correctamente me ocupo de la parte estética.
7) Defino los modelos
8) Creo superusuario para Django Administration: admin:123
9) Defino las urls para las vistas que van a exhibir listas y redacto sus respectivos html.
10) Creo forms y en views defino las funciones para crear registros en Socios, Actividades y Sedes.
11) Creo forms, urls y views para el formulario de búsqueda que se puede usar en la sección Socios


FUNCIONALIDADES DE LA APP

- Página de Inicio: Se puede acceder a través de botones a la Sección Admin/Staff, Socios, Actividades y Sedes.
- En la Sección Admin/Staff se puede registrar una actividad nueva mediante formulario así como también se puede registrar ua Sede nueva.
- En la Sección Socios se puede registrar un nuevo usuario mediante un formulario de registro y también se puede buscar datos de socios a través del campo requerido que es DNI (NOTA: Para chequear un dato existente se puede ver antes en el Administrator de Django un dato ingresado, si no se puede 1ro registrar un socio nuevo y luego buscar ese DNI).
- En la Sección Actividades se puede acceder a una lista de Actividades registradas en la BD así como también a sus respectivas Sedes.
- En la Sección Sedes se puede acceder a las sedes ingresadas en la base de datos.



