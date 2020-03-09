from django.db import models
from django.utils.timezone import now

# Create your models here.
class proyectos(models.Model):
    
    titulo=models.CharField(max_length=50)
    proposito=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    urlFoto=models.CharField(max_length=50)
	

    def __str__(self):
    
    		return  '%s %s' % (self.nombre,self.proposito)

