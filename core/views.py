from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Exemplo, Topico_swebook_1, Topico_swebook_2, Topico_swebook_3
from .filters import ExemploFilter

class IndexView(TemplateView):
    template_name = 'index.html'

class ExemploListView(ListView):
    model = Exemplo
    context_object_name = 'exemplo_list'
    template_name = 'exemploListView.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ExemploFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ExemploDetailView(DetailView):
    model = Exemplo
    context_object_name = 'exemplo'
    template_name = 'exemploDetailView.html'
