from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={"class": "form-control"}),
            'cpf': forms.TextInput(attrs={"class": "form-control"}),
            'telefone': forms.TextInput(attrs={"class": "form-control"}),
            'endereco': forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) != 11 or not cpf.isdigit():
            raise forms.ValidationError("O CPF deve ter 11 dígitos numéricos.")
        return cpf
