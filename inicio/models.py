from django.db import models

class Celu(models.Model):
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    anio=models.IntegerField()
    