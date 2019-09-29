from django.db import models

class Endereco(models.Model):
    referencia_um = models.CharField(max_length=120)
    referencia_dois = models.CharField(max_length=120, null=True, blank=True)
    cidade = models.CharField(max_length=120)
    estado = models.CharField(max_length=120)
    pais =models.CharField(max_length=120)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.referencia_um
