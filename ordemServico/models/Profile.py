from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):

    TIPO_USUARIO = (
        (1, 'Diretor'),
        (2, 'Administrativo'),
        (3, 'Líder Técnico'),
        (4, 'Sub-Líder Técnico'),
        (5, 'Técnico')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=TIPO_USUARIO, default=5)
    cpf = models.CharField(max_length=14)
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.user.username

    
# @receiver(post_save, sender=User)
# def created_user_profile(sender, instance, created, **kwargs):

#     '''
#     Cria um perfil de usuário automaticamente sempre que um novo usuário é criado.
#     Verifica se o perfil já existe antes de criá-lo.
#     '''
#     if created:
#         Profile.objects.get_or_create(user=instance)

    
   
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):

#     ''' 
#         Salva qualquer alteração no perfil automaticamente quando entramos no painel de perfil e alteramos qualquer dado.
#     '''
#     instance.profile.save()
