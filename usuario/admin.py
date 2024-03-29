from django.contrib import admin
from .models import Profile

class DetProfile(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_picture', 'biography', )
    list_display_links = ('user', )
    search_fields = ('user', )

admin.site.register(Profile)
# Register your models here.
