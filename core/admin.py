from django.contrib import admin

from .models import Exemplo, Topico_swebook_1, Topico_swebook_2, Topico_swebook_3, Avaliacao

@admin.register(Exemplo)
class ExemploAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Topico_swebook_1)
class Topico_swebook_1Admin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Topico_swebook_2)
class Topico_swebook_2Admin(admin.ModelAdmin):
    list_display = ('nome', 'associacao')

@admin.register(Topico_swebook_3)
class Topico_swebook_3Admin(admin.ModelAdmin):
    list_display = ('nome', 'associacao')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('exemplo', 'avaliacao', 'avaliador', 'comentario')

