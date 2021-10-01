from django.contrib import admin
from .models import Produtora, Games


class DetGames(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'lancamento', )
    list_display_links = ('title', )
    search_fields = ('title', )


admin.site.register(Produtora)
admin.site.register(Games, DetGames)
