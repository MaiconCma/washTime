from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from carro.models import Carro
from .forms import ProdutoForm
from .models import Gasto, Produto

@login_required
def listar_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produto.html', {'produtos': produtos})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.user = request.user  
            produto.save()
            return redirect('listar_produto')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})


@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.user == produto.user or request.user.is_staff:
        if request.method == 'POST':
            form = ProdutoForm(request.POST, instance=produto)
            if form.is_valid():
                form.save()
                return redirect('listar_produto')
        else:
            form = ProdutoForm(instance=produto)
        return render(request, 'editar_produto.html', {'form': form})
    else:
        raise PermissionDenied

@login_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        if request.user == produto.user or request.user.is_staff:
            produto.delete()
            return redirect('listar_produto')
        else:
            raise PermissionDenied
    return render(request, 'excluir_produto.html', {'produto': produto})


@login_required
def somar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.user == produto.user or request.user.is_staff:
        if request.method == 'POST':
            quantidade = int(request.POST.get('quantidade', 0))
            produto.quantidade += quantidade
            produto.save()
            return redirect('listar_produto')
        return render(request, 'somar_produto.html', {'produto': produto})
    else:
        raise PermissionDenied

@login_required
def registrar_gasto_produto(request):
    produtos = Produto.objects.all()
    carros = Carro.objects.all()  
    
    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        carro_id = request.POST.get('carro')
        quantidade_gasta = int(request.POST.get('quantidade', 0))

        produto = get_object_or_404(Produto, id=produto_id)
        carro = get_object_or_404(Carro, id=carro_id)

        if request.user == produto.user or request.user.is_staff:
            if quantidade_gasta > produto.quantidade:
                return render(request, 'gasto_produto.html', {
                    'produtos': produtos,
                    'carros': carros,
                    'error': 'Quantidade gasta excede a quantidade disponível do produto.'
                })
            produto.quantidade -= quantidade_gasta
            produto.save()
            return redirect('listar_produto')

    return render(request, 'gasto_produto.html', {'produtos': produtos, 'carros': carros})
