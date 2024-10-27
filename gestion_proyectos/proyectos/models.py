from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    responsable = models.ForeignKey(User, related_name='responsable_tareas', on_delete=models.SET_NULL, null=True)
    ejecutor = models.ForeignKey(User, related_name='ejecutor_tareas', on_delete=models.SET_NULL, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre