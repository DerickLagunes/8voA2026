from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    isbn = models.CharField(unique=True, max_length=20)
    paginas = models.IntegerField()
    editorial = models.CharField(max_length=150)
    disponible = models.BooleanField(default=True)