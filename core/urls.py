from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ExemploListView, ExemploDetailView, ExemploCreateView, PadraoCatalogacaoView, ExemploUpdateView, MeusExemplosListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('exemploListView/', ExemploListView.as_view(), name='exemploListView'),
    path('exemploDetailView/<int:pk>/', ExemploDetailView.as_view(), name='exemploDetailView'),
    path('exemploCreateView/', ExemploCreateView.as_view(), name='exemploCreateView'),
    path('exemploUpdateView/<int:pk>/', ExemploUpdateView.as_view(), name='exemploUpdateView'),
    path('padraoCatalogacao/', PadraoCatalogacaoView.as_view(), name='padraoCatalogacao'),
    path('meusExemplosListView/', MeusExemplosListView.as_view(), name='meusExemplosListView'),

]