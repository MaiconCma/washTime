from django import forms
from .models import Carro
from cliente.models import Cliente


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['nome', 'marca', 'modelo', 'ano', 'cor', 'placa', 'cliente']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['cliente'].queryset = Cliente.objects.filter(user=user)