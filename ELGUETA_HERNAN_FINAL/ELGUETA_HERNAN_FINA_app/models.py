from django.db import models

# Create your models here.

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    asignatura = models.CharField(max_length=20)
    seccion = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    tipoInstitucion = models.CharField(max_length=80)


