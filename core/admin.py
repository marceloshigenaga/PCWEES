from django.contrib import admin

from .models import Exemplo, Topico_swebook_1, Topico_swebook_2, Topico_swebook_3

@admin.register(Exemplo)
class ExemploAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Topico_swebook_1)
class Topico_swebook_1(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Topico_swebook_2)
class Topico_swebook_2(admin.ModelAdmin):
    list_display = ('nome', 'associacao')

@admin.register(Topico_swebook_3)
class Topico_swebook_3(admin.ModelAdmin):
    list_display = ('nome', 'associacao')