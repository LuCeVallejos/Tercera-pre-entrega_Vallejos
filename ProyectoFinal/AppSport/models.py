from django.db import models


class Socio(models.Model):
    dni = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellido} - {self.mail}"
    

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.sede}"


class Sede(models.Model):
    sede = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sede}"
