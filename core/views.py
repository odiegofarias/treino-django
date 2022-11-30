from django.shortcuts import redirect, render
from .models import Funcionario
from django.views.generic import ListView


def lista_funcionarios(request):
    funcionarios = Funcionario.objetos.all()

    return render(request, 'core/funcionarios.html', {'funcionarios': funcionarios})


class ListaFuncionarios(ListView):
    template_name = 'core/funcionarios.html'
    model = Funcionario
    context_object_name = 'funcionarios'


def cria_funcionario(request):
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            return redirect('core:lista-funcionarios')
    else:
        return render(request, 'core/form.html', {'form': form})
