from django.urls import path
from . import views


app_name='core'

urlpatterns = [
    path('', views.ListaFuncionarios.as_view(), name='lista-funcionarios')
]
