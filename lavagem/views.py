from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from cliente.models import Carro, Cliente
from lavagem.forms import LavagemForm
from lavagem.models import Lavagem

# Create your views here.
@login_required
def listar_lavagem(request):
    lavagens = Lavagem.objects.all()
    return render(request, 'listar_lavagem.html', {'lavagens': lavagens})

# Adicionar lavagem
@login_required
def adicionar_lavagem(request):
    if request.method == 'POST':
        form = LavagemForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            carro = form.cleaned_data['carro']
            
            if request.user == cliente.user or request.user.is_staff:
                form.save()
                return redirect('listar_lavagem')
            else:
                raise PermissionDenied
            
    else:
        form = LavagemForm()
    return render(request, 'adicionar_lavagem.html', {'form': form})

# Editar lavagem
@login_required
def editar_lavagem(request, lavagem_id):
    lavagem = get_object_or_404(Lavagem, id=lavagem_id)
    if request.user == lavagem.user or request.user.is_staff:
        if request.method == 'POST':
            form = LavagemForm(request.POST, instance=lavagem)
            if form.is_valid():
                form.save()
                return redirect('listar_lavagem')
        else:
            form = LavagemForm(instance=lavagem)
        return render(request, 'editar_lavagem.html', {'form': form})
    else:
        raise PermissionDenied

# Excluir lavagem
@login_required
def excluir_lavagem(request, lavagem_id):
    lavagem = get_object_or_404(Lavagem, id=lavagem_id)
    if request.user == lavagem.user or request.user.is_staff:
        if request.method == 'POST':
            lavagem.delete()
            return redirect('listar_lavagem')
    else:
        raise PermissionDenied
    return render(request, 'excluir_lavagem.html', {'lavagem': lavagem})