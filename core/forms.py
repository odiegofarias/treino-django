from django import forms
from .models import Funcionario


class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'