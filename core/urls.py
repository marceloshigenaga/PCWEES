from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ExemploListView, ExemploDetailView, \
    ExemploCreateView, PadraoCatalogacaoView, ExemploUpdateView, MeusExemplosListView, \
    ExemploDeleteView, AvaliacaoCreateView, MinhasAvaliacoesListView, AvaliacaoUpdateView, \
    AvaliacaoDeleteView, UsuarioCreateView, UsuarioUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('padraoCatalogacao/', PadraoCatalogacaoView.as_view(), name='padraoCatalogacao'),
    #exemplo
    path('exemploListView/', ExemploListView.as_view(), name='exemploListView'),
    path('exemploDetailView/<int:pk>/', ExemploDetailView.as_view(), name='exemploDetailView'),
    path('exemploCreateView/', ExemploCreateView.as_view(), name='exemploCreateView'),
    path('exemploUpdateView/<int:pk>/', ExemploUpdateView.as_view(), name='exemploUpdateView'),
    path('exemploDeleteView/<int:pk>/', ExemploDeleteView.as_view(), name='exemploDeleteView'),
    path('meusExemplosListView/', MeusExemplosListView.as_view(), name='meusExemplosListView'),
    #avaliação
    path('avaliacaoCreateView/<int:pk>/', AvaliacaoCreateView.as_view(), name='avaliacaoCreateView'),
    path('minhasAvaliacoesListView/', MinhasAvaliacoesListView.as_view(), name='minhasAvaliacoesListView'),
    path('avaliacaoUpdateView/<int:pk>/', AvaliacaoUpdateView.as_view(), name='avaliacaoUpdateView'),
    path('avaliacaoDeleteView/<int:pk>/', AvaliacaoDeleteView.as_view(), name='avaliacaoDeleteView'),
    #visitante
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarioCreateView/', UsuarioCreateView.as_view(), name='usuarioCreateView'),
    path('usuarioUpdateView/<int:pk>/', UsuarioUpdateView.as_view(), name='usuarioUpdateView'),


]