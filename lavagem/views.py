from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import LavagemForm
from .models import Lavagem


@login_required
def listar_lavagem(request):
    lavagens = Lavagem.objects.filter(user=request.user)
    return render(request, 'listar_lavagem.html', {'lavagens': lavagens})


@login_required
def adicionar_lavagem(request):
    if request.method == 'POST':
        form = LavagemForm(request.POST, user=request.user)
        if form.is_valid():
            lavagem = form.save(commit=False)
            lavagem.user = request.user
            lavagem.save()
            return redirect('listar_lavagem')
    else:
        form = LavagemForm(user=request.user)

    return render(request, 'adicionar_lavagem.html', {'form': form})


@login_required
def editar_lavagem(request, lavagem_id):
    lavagem = get_object_or_404(Lavagem, id=lavagem_id, user=request.user)

    if request.method == 'POST':
        form = LavagemForm(request.POST, instance=lavagem, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('listar_lavagem')
    else:
        form = LavagemForm(instance=lavagem, user=request.user)

    return render(request, 'editar_lavagem.html', {'form': form})


@login_required
def excluir_lavagem(request, lavagem_id):
    lavagem = get_object_or_404(Lavagem, id=lavagem_id, user=request.user)

    if request.method == 'POST':
        lavagem.delete()
        return redirect('listar_lavagem')

    return render(request, 'excluir_lavagem.html', {'lavagem': lavagem})