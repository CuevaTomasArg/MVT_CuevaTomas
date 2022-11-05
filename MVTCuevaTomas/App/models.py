from django.db import models

# Create your models here.
class Familiar(models.Model):
    
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad= models.IntegerField()
    hijos= models.IntegerField()
    nietos= models.IntegerField()
    fecha_de_nacimiento = models.DateTimeField()
    