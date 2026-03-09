from django import forms
from .models import Lavagem
from cliente.models import Cliente
from carro.models import Carro


class LavagemForm(forms.ModelForm):
    class Meta:
        model = Lavagem
        fields = ['cliente', 'carro', 'descricao', 'preco']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['cliente'].queryset = Cliente.objects.filter(user=user)
            self.fields['carro'].queryset = Carro.objects.filter(user=user)