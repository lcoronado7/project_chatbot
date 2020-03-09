from django.db import models
from django.utils.timezone import now

# Create your models here.
class evento(models.Model):
    
    titulo=models.CharField(max_length=50)
    proposito=models.CharField(max_length=50)
    fecha_realizacion=models.DateTimeField(default=now)
    descripcion=models.CharField(max_length=50)
    urlFoto=models.CharField(max_length=50)
	
    def __str__(self):
    
    		return  '%s %s' % (self.titulo,self.fecha_realizacion)
    


	
    