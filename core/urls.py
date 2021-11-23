from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ExemploListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('exemplosListView/', ExemploListView.as_view(), name='exemploListView'),

]