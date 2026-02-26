from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=70)
    email = models.EmailField()
    mensaje = models.TextField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField()