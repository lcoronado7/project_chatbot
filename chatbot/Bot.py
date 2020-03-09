import string
from django import db
from django.core import serializers
import re
from .models import Pregunta,Conversacion,Mensaje, palabrasClave
#from cursos.models import Categoria, Curso



class Bot:
  def __init__(self):
      pass

  # responser: recibe el mensaje enviado por el usuario y lo compara con las preguntas
  #para luego concatenar las respuestas relacionas con las preguntas 

  def responser(self,msj):
        
        msj=msj.lower()
        msj=msj.split()
        lista=[]
        for palabra in msj:
            try:
                response=palabrasClave.objects.get(palabra=palabra)
                lista.append(response)
            except:
                continue
        
        if lista != None:
            respuestas=""
            for claves in lista:
                try:
                    response1=Pregunta.objects.get(pregunta=claves.idpregunta)
                    respuestas+=str(response1.idrespuesta)+" <br>"
                    print(respuestas)
                except:
                    response=None
            print("LISTA ", str(respuestas))
            
            response=respuestas
            if not response :
                response =""
        else:
            response = ""

        return response

