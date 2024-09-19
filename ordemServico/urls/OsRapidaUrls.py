from django.urls import path
from ordemServico.views.OsRapidaView import criar_os_rapida, editar_os_rapida, os_rapida

urlpatterns = [
    path('criar/osrapida/', criar_os_rapida, name='criar_os_rapida'),
    path('osrapida/', os_rapida, name='os_rapida'),
    path('editar_os_rapida/<int:os_rapida_id>/', editar_os_rapida, name='editar_os_rapida'),

]