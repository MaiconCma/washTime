from django import forms
from .models import Lavagem


class LavagemForm(forms.ModelForm):
    class Meta:
        model = Lavagem
        fields = ['cliente','carro' ,'descricao', 'preco']