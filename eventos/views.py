from django.shortcuts import render

from articulos.models import articulos
from eventos.models import evento
from proyectos.models import proyectos

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    return render(
        request,
        'index.html'
    )


from django.views import generic

class ArticulosListView(generic.ListView):
    model = articulos
    paginate_by = 10
    template_name = 'articulos.html'
    def get_context_data(self, **kwargs):
        context = super(ArticulosListView, self).get_context_data(**kwargs)
        lista_articulos= articulos.objects.values()
        print(str(lista_articulos))
        context['lista_articulos'] = lista_articulos
        return context

class EventosListView(generic.ListView):
    model = evento
    paginate_by = 10
    template_name = 'eventos.html'

    def get_context_data(self, **kwargs):
        context = super(EventosListView, self).get_context_data(**kwargs)
        lista_eventos= evento.objects.values()
        print(str(lista_eventos))
        context['lista_evento'] = lista_eventos
        return context

class ProyectosListView(generic.ListView):
    
    model = proyectos
    paginate_by = 10
    template_name = 'proyectos.html'  

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        lista_proyectos= proyectos.objects.values()
        print(str(lista_proyectos))
        context['lista_proyectos'] = lista_proyectos
        return context

