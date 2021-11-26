from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Exemplo
from .filters import ExemploFilter
from django.urls import reverse_lazy
from .forms import ExemploForm

class IndexView(TemplateView):
    template_name = 'index.html'

class PadraoCatalogacaoView(TemplateView):
    template_name = 'PadraoCatalogacao.html'

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

class ExemploUpdateView(LoginRequiredMixin, UpdateView):
    model = Exemplo
    template_name = 'exemploCreateView.html'
    success_url = reverse_lazy('meusExemplosListView')
    form_class = ExemploForm

    # coloca automaticamente o usuário logado como autor do exemplo
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ExemploDeleteView(LoginRequiredMixin, DeleteView):
    model = Exemplo
    template_name = 'exemploDeleteView.html'
    success_url = reverse_lazy('meusExemplosListView')

class MeusExemplosListView(LoginRequiredMixin, ListView):
    model = Exemplo
    context_object_name = 'exemplo_list'
    template_name = 'meusExemplosListView.html'

    # alterando retorno padrão para somente exemplos do usuário
    def get_queryset(self):
        user = self.request.user
        return Exemplo.objects.filter(autor=user)

