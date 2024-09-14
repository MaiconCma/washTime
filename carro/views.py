from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Carro
from .forms import CarroForm
from cliente.models import Cliente

# Listar carros
@login_required
def listar_carro(request):
    carros = Carro.objects.all()
    return render(request, 'listar_carro.html', {'carros': carros})

# Adicionar carro
@login_required
def adicionar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            if Cliente.objects.filter(id=cliente.id).exists():
                carro = form.save(commit=False)
                carro.user = request.user
                carro.save()
                return redirect('listar_carro')
            else:
                form.add_error('cliente', 'O cliente selecionado não existe.')
    else:
        form = CarroForm()
    return render(request, 'adicionar_carro.html', {'form': form})

# Editar carro
@login_required
def editar_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carro')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'editar_carro.html', {'form': form})

# Excluir carro
@login_required
def excluir_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    if request.method == 'POST':
        carro
