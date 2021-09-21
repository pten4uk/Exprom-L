from django.views.generic import ListView, DetailView
from .models import Pouf


class PoufList(ListView):
    model = Pouf
    template_name = 'catalog/catalog.html'
    context_object_name = 'models'


class PoufDetail(DetailView):
    model = Pouf
    template_name = 'catalog/model.html'
    context_object_name = 'model'
