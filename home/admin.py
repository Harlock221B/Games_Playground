from django.contrib import admin
from .models import Produtora, Games, Genero


class DetGames(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'lancamento', )
    list_display_links = ('title', )
    search_fields = ('title', )

class DetProdutora(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', )
    list_display_links = ('nome', )
    search_fields = ('nome', )

class DetGenero(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', )
    list_display_links = ('nome', )
    search_fields = ('nome', )

admin.site.register(Produtora)
admin.site.register(Games, DetGames)
admin.site.register(Genero, DetGenero)
