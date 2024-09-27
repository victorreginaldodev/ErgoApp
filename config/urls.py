from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ordemServico.urls.OrdemServicoUrls')),
    path('', include('ordemServico.urls.FinanceiroUrls')),
    path('', include('ordemServico.urls.LiderTecnicoUrls')),
    path('', include('ordemServico.urls.TecnicoUrls')),
    path('', include('ordemServico.urls.OsRapidaUrls')),
    path('', include('ordemServico.urls.LoginUrls')),
    path('', include('ordemServico.urls.RegistroUrls')),
    path('', include('ordemServico.urls.ClientesUrls')),
    path('', include('ordemServico.urls.RepositorioUrls')),
    path('', include('ordemServico.urls.UsuarioUrls')),
    path('', include('ordemServico.urls.PainelControleUrls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)