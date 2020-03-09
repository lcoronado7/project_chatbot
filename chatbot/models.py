from django.db import models
import uuid
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.utils.timezone import now

class Respuesta(models.Model):
    id = models.id = models.AutoField(primary_key=True, default=uuid.uuid4, help_text="id único")
    respuesta = models.CharField(max_length=500, help_text="Respuesta del servidor")
    def __str__(self):
        return self.respuesta

class Pregunta(models.Model):
    id = models.id = models.AutoField(primary_key=True, default=uuid.uuid4, help_text="id único")	
    idrespuesta= models.ForeignKey(Respuesta, default=0, on_delete=models.CASCADE)
    pregunta =models.CharField(max_length=500, help_text="Mensaje del cliente",unique=True)

	

    def __str__(self):
        return self.pregunta
    


class palabrasClave(models.Model):
    id_palabrasClave = models.id = models.AutoField(primary_key=True, default=uuid.uuid4, help_text="id único")
    idpregunta = models.ForeignKey(Pregunta, default=0 ,on_delete=models.CASCADE)
    palabra=models.CharField(max_length=500,default="", help_text="Respuesta del servidor")

    def __str__(self):
        return '%s, %s' % (self.id_palabrasClave, self.palabra)



class Conversacion(models.Model):
	token = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="id único")
	nombre = models.CharField(max_length=200)
	correo = models.CharField(max_length=200)
	fecha = models.DateTimeField(default=now)
	class Meta:
		verbose_name = "conversacion"
		verbose_name_plural = "conversaciones"

	def __str__(self):
		return '%s (%s)' % (self.nombre,self.correo)

class Mensaje(models.Model):
	conversacion = models.ForeignKey('Conversacion', on_delete=models.SET_NULL, null=True)
	mensaje = models.CharField(max_length=500)
	fecha = models.DateTimeField(default=now)
	LOAN_TIPO = (
		('c', 'Cliente'),
		('s', 'Servidor'),
	)
	tipo = models.CharField(max_length=1, choices=LOAN_TIPO, blank=True, default='c', help_text='EMISOR')

	class Meta:
		verbose_name = "mensaje"
		verbose_name_plural = "mensajes"

	def __str__(self):
		return '%i' % (self.id)
