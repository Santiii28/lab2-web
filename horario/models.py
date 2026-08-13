from django.db import models


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.EmailField()

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="clases")
    cupo = models.PositiveIntegerField()
    inscritos = models.PositiveIntegerField(default=0)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
