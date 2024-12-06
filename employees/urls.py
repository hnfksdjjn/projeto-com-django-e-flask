# employees/urls.py

from django.urls import path
from .views import (
    list_employees,
    employee_registration,
    dashboard,
    backup_data,
    restore_data,
    index,  # Página inicial
)

urlpatterns = [
    path('',  index, name='index'),  # Página inicial
    path('register/', employee_registration, name='employee_registration'),
    path('employees/', list_employees, name='list_employees'),
    path('dashboard/', dashboard, name='dashboard'),
    path('backup/', backup_data, name='backup_data'),
    path('restore/', restore_data, name='restore_data'),
]
