from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class AlmacenCarro(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    precio = models.PositiveIntegerField(default=0)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.marca.nombre + " " + self.modelo.nombre
