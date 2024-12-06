# employees/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count, Avg
import logging
import json
import pandas as pd
from xhtml2pdf import pisa
import plotly.express as px
import requests
from .models import Employee
import requests
from io import BytesIO
from reportlab.pdfgen import canvas

# URL da API Flask
FLASK_API_URL = "http://127.0.0.1:5000/users"

# Criar logger
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'employees/index.html')  # Verifique o caminho do template

# Função de envio de e-mail
def send_employee_email(employee_email, subject, message):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [employee_email],
            fail_silently=False,
        )
        return "E-mail enviado com sucesso!"
    except Exception as e:
        return f"Erro ao enviar o e-mail: {str(e)}"

# Função de log de ações
def log_employee_action(action, employee_name, employee_id=None):
    if action == "create":
        logger.info(f"Funcionário {employee_name} (ID: {employee_id}) foi criado.")
    elif action == "update":
        logger.info(f"Funcionário {employee_name} (ID: {employee_id}) foi atualizado.")
    elif action == "delete":
        logger.info(f"Funcionário {employee_name} (ID: {employee_id}) foi excluído.")

# Função de cadastro de funcionários
def employee_registration(request):
    if request.method == "POST":
        # Dados do funcionário
        name = request.POST.get('name')
        age = request.POST.get('age')
        position = request.POST.get('position')
        salary = request.POST.get('salary')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Criar o funcionário
        new_employee = Employee.objects.create(name=name, age=age, position=position, salary=salary, phone=phone, email=email)
        log_employee_action("create", name, new_employee.id)

        # Enviar e-mail
        subject = "Bem-vindo à nossa empresa!"
        message = f"Olá {name}, você foi registrado com sucesso!"
        send_employee_email(email, subject, message)

        return redirect('list_employees')
    
    return render(request, 'employees/employee_form.html')

# Função de listagem de funcionários
def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})

# Função de dashboard de estatísticas
def dashboard(request):
    # Pega todos os funcionários registrados no banco
    employees = Employee.objects.all()

    # Gráfico de distribuição de cargos
    position_counts = employees.values('position').annotate(count=Count('position'))  # Usando Count
    position_fig = px.bar(position_counts, x='position', y='count', title="Distribuição de Cargos")

    # Gráfico de média salarial
    avg_salary = employees.aggregate(Avg('salary'))  # Usando Avg

    return render(request, "employees/dashboard.html", {
        "position_fig": position_fig.to_html(full_html=False),
        "avg_salary": avg_salary['salary__avg']
    })

# Funções para gerar relatórios em PDF e Excel



# Funções de backup e restauração de dados
def backup_data(request):
    employees = Employee.objects.all().values()
    data = list(employees)

    with open("backup_funcionarios.json", "w") as f:
        json.dump(data, f, indent=4)

    return HttpResponse("Backup gerado com sucesso!", content_type="text/plain")

def restore_data(request):
    with open("backup_funcionarios.json", "r") as f:
        data = json.load(f)
        
    for emp in data:
        Employee.objects.update_or_create(
            id=emp['id'],
            defaults={
                'name': emp['name'],
                'age': emp['age'],
                'position': emp['position'],
                'salary': emp['salary'],
                'phone': emp['phone'],
                'email': emp['email'],
            }
        )

    return HttpResponse("Dados restaurados com sucesso!", content_type="text/plain")

