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
    #todos_campos = django_filters.CharFilter(method='todos_campos_filter', label="Todos os campos")


    class Meta:
        model = Exemplo
        fields = ('titulo', 'swebook', 'tags', 'linguagem')


        # fields = ('titulo', 'projeto_linguagem_programacao', 'topico_swebook_1', 'tags', 'todos_campos')

    def todos_campos_filter(self, queryset, name, value):
        return Exemplo.objects.filter(
            Q(titulo__icontains=value) | Q(outros_topicos__icontains=value) | Q(projeto_nome__icontains=value))

    def tags_filter(self, queryset, name, value):
        return Exemplo.objects.filter(
            Q(tag_1__icontains=value) | Q(tag_2__icontains=value) | Q(tag_3__icontains=value))


# fields = {
#             'titulo': ['icontains'],
#             'projeto_linguagem_programacao': ['icontains'],
#             'topico_swebook_1': [],
#             }