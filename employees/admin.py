from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position','age', 'salary', 'phone','email')  # Exibe as colunas na lista
    search_fields = ('name', 'position')  # Permite pesquisa por nome e cargo
    list_filter = ('position',)  # Filtro de cargos
    
    # Permissões personalizadas
    def has_add_permission(self, request):
        # Condição para permitir adicionar
        return request.user.has_perm('employees.add_employee')

    def has_delete_permission(self, request, obj=None):
        # Condição para permitir excluir
        return request.user.has_perm('employees.delete_employee')
# Registra o modelo Employee com as configurações personalizadas
admin.site.register(Employee, EmployeeAdmin)