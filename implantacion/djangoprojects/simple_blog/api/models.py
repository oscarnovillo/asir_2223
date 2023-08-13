from django.db import models

# Create your models here.


class Coche(models.Model):
        
    matricula = models.CharField(max_length=7, primary_key=True)
    fecha_matriculacion = models.DateField()
    color = models.CharField(max_length=20)
    accidentes = models.ManyToManyField('Accidente', blank=True)
    
    
class Accidente(models.Model):
    descripcion = models.CharField(max_length=200)
    lugar = models.CharField(max_length=200)
    coches = models.ManyToManyField('Accidente', blank=True)
    
    def __str__ (self):
        return self.descripcion
    