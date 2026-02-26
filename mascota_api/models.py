from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    especie = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_de_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascota_api_mascota'
