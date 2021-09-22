from django.views.generic import ListView, DetailView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'models'


class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/model.html'
    context_object_name = 'model'
