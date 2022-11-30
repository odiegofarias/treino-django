from django.urls import path
from . import views


app_name='core'

urlpatterns = [
    path('', views.ListaFuncionarios.as_view(), name='lista-funcionarios'),
    path('index/', views.IndexTemplateView.as_view(), name='index'),
    path('funcionario/<id>', views.FuncionarioUpdateView.as_view(), name='atualiza-funcionario'),
    path('funcionario/exclui/<pk>', views.FuncionarioDeleteView.as_view(), name='exclui-funcionario'),
    path('funcionario/cadastrar', views.FuncionarioCreateView.as_view(), name='cria-funcionario'),
]
