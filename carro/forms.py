from django import forms
from .models import Carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'ano', 'cor', 'placa', 'cliente']