from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ExemploListView, ExemploDetailView, \
    ExemploCreateView, PadraoCatalogacaoView, ExemploUpdateView, MeusExemplosListView, \
    ExemploDeleteView, AvaliacaoCreateView, MinhasAvaliacoesListView, AvaliacaoUpdateView, AvaliacaoDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('exemploListView/', ExemploListView.as_view(), name='exemploListView'),
    path('exemploDetailView/<int:pk>/', ExemploDetailView.as_view(), name='exemploDetailView'),
    path('exemploCreateView/', ExemploCreateView.as_view(), name='exemploCreateView'),
    path('exemploUpdateView/<int:pk>/', ExemploUpdateView.as_view(), name='exemploUpdateView'),
    path('exemploDeleteView/<int:pk>/', ExemploDeleteView.as_view(), name='exemploDeleteView'),
    path('padraoCatalogacao/', PadraoCatalogacaoView.as_view(), name='padraoCatalogacao'),
    path('meusExemplosListView/', MeusExemplosListView.as_view(), name='meusExemplosListView'),
    path('avaliacaoCreateView/<int:pk>/', AvaliacaoCreateView.as_view(), name='avaliacaoCreateView'),
    path('minhasAvaliacoesListView/', MinhasAvaliacoesListView.as_view(), name='minhasAvaliacoesListView'),
    path('avaliacaoUpdateView/<int:pk>/', AvaliacaoUpdateView.as_view(), name='avaliacaoUpdateView'),
    path('avaliacaoDeleteView/<int:pk>/', AvaliacaoDeleteView.as_view(), name='avaliacaoDeleteView'),

]