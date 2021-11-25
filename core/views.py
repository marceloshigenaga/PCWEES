from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Exemplo
from .filters import ExemploFilter
from django.urls import reverse_lazy
from .forms import ExemploForm

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

class ExemploCreateView(LoginRequiredMixin, CreateView):
    model = Exemplo
    template_name = 'exemploCreateView.html'
    success_url = reverse_lazy('exemploListView')
    form_class = ExemploForm

    # coloca automaticamente o usuário logado como autor do exemplo
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

