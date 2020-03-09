from django.shortcuts import render
from .models import Pregunta,Conversacion,Mensaje
from django.contrib.admin.models import LogEntry
from django.http import JsonResponse
from .Bot import Bot

def CrearConversacion(request):
        
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')

        chat = Conversacion(nombre=nombre, correo=correo)
        chat.save()
        if chat.token is not None:
           token = chat.token
           nombre = chat.nombre
           estado = "creado"
        else:
        	estado = "No se creo que el chat"

        if nombre is None:
            return JsonResponse({'error':'pagina no autorizada'})

        return JsonResponse(
            {
                'content': {
                    'estado': estado,
                    'token': token,
                    'nombre': nombre,
                }
            }
        )


def ObtenerConversacion(request):
        token = request.POST.get('token')

        # Busca la conversacion a la cual pertenece
        try:
           con = Conversacion.objects.get(token=token)
        except Conversacion.DoesNotExist:
           con = None

        if con is None:
            return JsonResponse(            
            {
                'content': {
                    'estado': 'no existe la conversacion',
                    'error':'token no valido',
                    'token':token,
                }
            }
        )

        #obtener los mensajes
        mensajes = Mensaje.objects.filter(conversacion=con)

        #construir lista de mensajes
        lista = [{'mensaje': mensaje.mensaje, 'fecha': mensaje.fecha, 'tipo' : mensaje.tipo} for mensaje in mensajes]
        return JsonResponse(            
            {
                'content': {
                    'estado': 'recibido',
                    'mensajes':lista,
                }
            }
        )


def Chat(request):
        # Borrando registros de las acciones recientes del admin
        LogEntry.objects.all().delete()
        # Recibiendo los parametros
        mensaje = request.POST.get('mensaje')
        token = request.POST.get('token')
        bot = Bot()
        print ("..................Mensajee.........."+str(mensaje).format(request))
        if mensaje is None:
            return JsonResponse({'error':'pagina no autorizada'})

        # Busca la conversacion a la cual pertenece
        try:
           con = Conversacion.objects.get(token=token)
        except Conversacion.DoesNotExist:
           con = None

        if con is None:
            return JsonResponse(            
            {
                'content': {
                    'estado': 'no enviado',
                    'error':'token no valido',
                }
            }
        )

        # guardar mensaje enviado por el cliente
        mensajec = Mensaje(conversacion=con,mensaje=mensaje,tipo='c')
        mensajec.save();

        prueba = bot.responser(mensaje)
        if  prueba != "":
           respuesta = str(prueba)
        else:
            respuesta = "Lo siento no he comprendido, podrias preguntar nuevamente para poder ayudarte?"

        # guardar respuesta enviada al cliente
        mensajes = Mensaje(conversacion=con,mensaje=respuesta,tipo='s')
        mensajes.save();

        return JsonResponse(
            {
                'content': {
                    'estado': 'enviado',
                    'mensaje': respuesta,
                }
            }
        )