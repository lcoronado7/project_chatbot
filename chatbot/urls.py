from django.conf.urls import url

from . import views



urlpatterns = [
	url(r'^chat/$', views.Chat, name='chat'),
	url(r'^chat/create', views.CrearConversacion, name='create-chat'),
	url(r'^chat/get$', views.ObtenerConversacion, name='get-chat'),
]