from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Carro
from .forms import CarroForm
from cliente.models import Cliente


@login_required
def listar_carro(request):
    carros = Carro.objects.filter(user=request.user)
    return render(request, 'listar_carro.html', {'carros': carros})


@login_required
def adicionar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST, user=request.user)
        if form.is_valid():
            carro = form.save(commit=False)
            carro.user = request.user
            carro.save()
            return redirect('listar_carro')
    else:
        form = CarroForm(user=request.user)

    return render(request, 'adicionar_carro.html', {'form': form})


@login_required
def editar_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id, user=request.user)

    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('listar_carro')
    else:
        form = CarroForm(instance=carro, user=request.user)

    return render(request, 'editar_carro.html', {'form': form})


@login_required
def excluir_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id, user=request.user)

    if request.method == 'POST':
        carro.delete()
        return redirect('listar_carro')

    return render(request, 'excluir_carro.html', {'carro': carro})