from django.contrib import admin
from .models import *

# Registrar outros modelos
admin.site.register(Profile)
admin.site.register(Contato)
admin.site.register(Cliente)
admin.site.register(RepositorioMiniOS)
admin.site.register(MiniOS)
admin.site.register(Repositorio)
admin.site.register(Servico)
admin.site.register(OrdemServico)

# Configuração de Inline para Serviços
class ServicoInline(admin.TabularInline):
    model = Servico
    extra = 1

class TarefaInline(admin.TabularInline):
    model = Tarefa
    extra = 1

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('servico', 'profile', 'descricao', 'data_inicio', 'data_termino')
    search_fields = ('descricao', 'profile__nome')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Defina a ordem de serviço como None inicialmente
        ordem_servico_id = None

        # Se estiver editando uma tarefa existente, pegue a ordem de serviço associada ao serviço da tarefa
        if obj and obj.servico:
            ordem_servico_id = obj.servico.ordem_servico.id
        elif request.GET.get('ordem_servico'):
            # Se estiver criando uma nova tarefa com uma ordem de serviço especificada na URL
            ordem_servico_id = request.GET.get('ordem_servico')

        if ordem_servico_id:
            # Filtrar os serviços pela ordem de serviço correspondente
            form.base_fields['servico'].queryset = Servico.objects.filter(ordem_servico_id=ordem_servico_id)
        else:
            # Não mostrar serviços, caso não tenha a ordem de serviço definida
            form.base_fields['servico'].queryset = Servico.objects.none()

        return form