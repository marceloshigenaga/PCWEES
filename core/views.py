from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Exemplo, Topico_swebook_1, Topico_swebook_2, Topico_swebook_3
from .filters import ExemploFilter
from django_filters.views import FilterView

class IndexView(TemplateView):
    template_name = 'index.html'

# class ExemploListView(ListView):
#     model = Exemplo
#     template_name = 'exemploListView.html'
#     context_object_name = 'exemplos'
#
#     filter = ExemploFilter()

class ExemploListView(FilterView):
    model = Exemplo
    context_object_name = 'exemplo_list'
    template_name = 'exemploListView.html'
    filterset_class = ExemploFilter


