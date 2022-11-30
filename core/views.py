from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Funcionario
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView, CreateView


def lista_funcionarios(request):
    funcionarios = Funcionario.objetos.all()

    return render(request, 'core/funcionarios.html', {'funcionarios': funcionarios})


class ListaFuncionarios(ListView):
    template_name = 'core/funcionarios.html'
    model = Funcionario
    # nome padrão = object
    context_object_name = 'funcionarios'


def cria_funcionario(request):
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            return redirect('core:lista-funcionarios')
    else:
        return render(request, 'core/form.html', {'form': form})


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        funcionario = None

        id = self.kwargs.get(self.pk_url_kwargs)
        slug = self.kwargs.get(self.slug_url_kwargs)

        if id is not None:
            funcionario = Funcionario.objects.filter(id=id).first()
        
        elif slug is not None:
            campo_slug = self.get_slug_field()

            funcionario = Funcionario.objects.filter(**{campo_slug: slug}).first()

        return funcionario


class FuncionarioDeleteView(DeleteView):
    template_name = 'core/exclui.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy('core:lista-funcionarios')


class FuncionarioCreateView(CreateView):
    template_name = 'core/cria.html'
    model = Funcionario
    form_class = InseFuncionarioForm
    success_url = reverse_lazy('core:lista-funcionarios')

