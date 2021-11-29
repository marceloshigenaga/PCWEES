import django_filters
from .models import *
from django.db.models import Q

class ExemploFilter(django_filters.FilterSet):
    swebook = django_filters.ModelChoiceFilter(queryset=Topico_swebook_1.objects.all(),
                                               field_name='topico_swebook_1',
                                               label="Tópico SWEBOOK")
    tags = django_filters.CharFilter(method='tags_filter',
                                     label="Tags")
    titulo = django_filters.CharFilter(field_name='titulo',
                                       label="Título",
                                       lookup_expr='icontains')
    linguagem = django_filters.CharFilter(field_name='projeto_linguagem_programacao',
                                          label="Linguagem de programação",
                                          lookup_expr='icontains')


    class Meta:
        model = Exemplo
        fields = ('titulo', 'swebook', 'tags', 'linguagem')

    def tags_filter(self, queryset, name, value):
        return Exemplo.objects.filter(
            Q(tag_1__icontains=value) | Q(tag_2__icontains=value) | Q(tag_3__icontains=value))

