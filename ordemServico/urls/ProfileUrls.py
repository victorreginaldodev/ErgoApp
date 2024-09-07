from django.urls import path
from ordemServico.views.ProfileView import list_profile_view

urlpatterns  = [
    path('', list_profile_view, name='profile'),
    path('<int:id>', list_profile_view, name='profile'),
]