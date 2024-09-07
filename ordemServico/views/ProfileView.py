from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def list_profile_view(request, id=None):
    
    if id is None and request.user.is_authenticated:
        id = request.user.id

    elif not request.user.is_authenticated:
        id = 0
    
    return HttpResponse(
        '<h1>Salve Maria</h1>'
        f'Usuário de id {id}'
    )