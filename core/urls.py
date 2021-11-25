from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ExemploListView, ExemploDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('exemploListView/', ExemploListView.as_view(), name='exemploListView'),
    path('exemploDetailView/<int:pk>/', ExemploDetailView.as_view(), name='exemploDetailView'),

]