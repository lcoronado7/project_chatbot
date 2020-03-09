from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^articulos/$', views.ArticulosListView.as_view(), name='articulos'),
	url(r'^eventos/$', views.EventosListView.as_view(), name='eventos'),
	url(r'^proyectos/$', views.ProyectosListView.as_view(), name='proyectos'),
]