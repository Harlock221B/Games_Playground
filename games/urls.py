from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='home'),
    path('usuario/', include('usuario.urls')),
    path('<int:idbusca>', views.mostrar, name='games'),
    path('buscar/', views.buscar, name='buscar'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

