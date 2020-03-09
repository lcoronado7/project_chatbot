from django.db import models
from django.utils.timezone import now

# Create your models here.
class articulos(models.Model):
    
	nombre=models.CharField(max_length=50)
	tipo=models.CharField(max_length=50)
	costo=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=50,default="")
	fecha_lanzamiento=models.DateTimeField(default=now)
	descuento=models.BooleanField()
	procentaje_descuento=models.BigIntegerField()
	urlFoto=models.CharField(max_length=50)


	def __str__(self):
    		return  '%s %s' % (self.nombre,self.tipo)

    
