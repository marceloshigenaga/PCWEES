from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Exemplo, Avaliacao
from .filters import ExemploFilter
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ExemploForm, AvaliacaoForm, UsuarioForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avaliacoes'] = Avaliacao.objects.filter(exemplo=self.kwargs['pk'])
        return context

class ExemploCreateView(LoginRequiredMixin, SuccessMessageMixin,  CreateView):
    model = Exemplo
    template_name = 'exemploCreateView.html'
    success_url = reverse_lazy('meusExemplosListView')
    form_class = ExemploForm
    success_message = "Exemplo criado com sucesso!"

    # coloca automaticamente o usuário logado como autor do exemplo
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ExemploUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Exemplo
    template_name = 'exemploCreateView.html'
    success_url = reverse_lazy('meusExemplosListView')
    form_class = ExemploForm
    success_message = "Exemplo alterado com sucesso!"

    # coloca automaticamente o usuário logado como autor do exemplo
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    # verifica se é o autor que está fazendo a alteração
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Exemplo, pk=self.kwargs['pk'], autor=self.request.user)
        return self.object

class ExemploDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Exemplo
    template_name = 'exemploDeleteView.html'
    success_url = reverse_lazy('meusExemplosListView')
    success_message = "Exemplo excluído com sucesso!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ExemploDeleteView, self).delete(request, *args, **kwargs)

    # verifica se é o autor que está fazendo a exclusão
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Exemplo, pk=self.kwargs['pk'], autor=self.request.user)
        return self.object

class MeusExemplosListView(LoginRequiredMixin, ListView):
    model = Exemplo
    context_object_name = 'exemplo_list'
    template_name = 'meusExemplosListView.html'

    # alterando retorno padrão para somente exemplos do usuário
    def get_queryset(self):
        user = self.request.user
        return Exemplo.objects.filter(autor=user)

class AvaliacaoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Avaliacao
    template_name = 'avaliacaoCreateView.html'
    success_url = reverse_lazy('exemploListView')
    form_class = AvaliacaoForm
    success_message = "Avaliação realizada com sucesso!"

    # coloca automaticamente o usuário logado como avaliador
    def form_valid(self, form):
        form.instance.avaliador = self.request.user
        form.instance.exemplo = Exemplo.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    # pega o exemplo passado como parâmetro
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exemplo'] = Exemplo.objects.get(pk=self.kwargs['pk'])
        return context

class AvaliacaoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Avaliacao
    template_name = 'avaliacaoCreateView.html'
    success_url = reverse_lazy('minhasAvaliacoesListView')
    form_class = AvaliacaoForm
    success_message = "Avaliação alterada com sucesso!"

    # verifica se é o autor que está fazendo a alteração
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Avaliacao, pk=self.kwargs['pk'], avaliador=self.request.user)
        return self.object

class AvaliacaoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Avaliacao
    template_name = 'avaliacaoDeleteView.html'
    success_url = reverse_lazy('minhasAvaliacoesListView')
    success_message = "Avaliação excluída com sucesso!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AvaliacaoDeleteView, self).delete(request, *args, **kwargs)

    # verifica se é o autor que está fazendo a exclusão
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Avaliacao, pk=self.kwargs['pk'], avaliador=self.request.user)
        return self.object

class MinhasAvaliacoesListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    context_object_name = 'avaliacao_list'
    template_name = 'minhasAvaliacoesListView.html'

    # alterando retorno padrão para somente exemplos do usuário
    def get_queryset(self):
        user = self.request.user
        return Avaliacao.objects.filter(avaliador=user)

class UsuarioCreateView(SuccessMessageMixin, CreateView):
    template_name = 'usuarioCreateView.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    success_message = "Cadastro realizado com sucesso!"

