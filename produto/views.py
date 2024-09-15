from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import ProdutoForm
from .models import Produto

# Listar produtos
@login_required
def listar_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produto.html', {'produtos': produtos})

# Adicionar produto
@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.user = request.user  # Relaciona o produto com o usuário
            produto.save()
            return redirect('listar_produto')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

# Editar produto
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

# Excluir produto
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
