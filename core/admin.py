from django.contrib import admin

from .models import Exemplo, Topico_swebook_1, Topico_swebook_2, Topico_swebook_3, Avaliacao

@admin.register(Exemplo)
class ExemploAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor')
    search_fields = ('titulo', 'autor', 'projeto_nome', 'projeto_descricao')
    list_filter = ('autor','projeto_linguagem_programacao', 'topico_swebook_1')

@admin.register(Topico_swebook_1)
class Topico_swebook_1Admin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)

@admin.register(Topico_swebook_2)
class Topico_swebook_2Admin(admin.ModelAdmin):
    list_display = ('nome', 'associacao')
    list_filter = ('associacao',)
    ordering = ('nome',)

@admin.register(Topico_swebook_3)
class Topico_swebook_3Admin(admin.ModelAdmin):
    list_display = ('nome', 'associacao')
    list_filter = ('associacao',)
    ordering = ('nome',)

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('exemplo', 'avaliacao', 'avaliador', 'comentario')
    list_filter = ('avaliador', )

