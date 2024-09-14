from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nome de Usuário',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput
    )

@login_required
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.user.is_staff or request.user == cliente.user:
        if request.method == 'POST':
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('listar_clientes')
        else:
            form = ClienteForm(instance=cliente)
        return render(request, 'editar_cliente.html', {'form': form})
    else:
        raise PermissionDenied

@login_required
def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    # Verifica se o usuário tem permissão para excluir
    if request.user.is_staff or request.user == cliente.user:
        if request.method == 'POST':
            cliente.delete()
            return redirect('listar_clientes')
        return render(request, 'excluir_cliente.html', {'cliente': cliente})
    else:
        raise PermissionDenied

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.filter(user=request.user)
    return render(request, 'listar_clientes.html', {'clientes': clientes})

@login_required
def adicionar_cliente(request):
    # Aqui não verificamos se o cliente já existe, pois agora um usuário pode ter múltiplos clientes
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user  # Associar o cliente ao usuário logado
            cliente.save()
            return redirect('listar_clientes')  # Redireciona para o perfil do cliente após salvar
    else:
        form = ClienteForm()

    return render(request, 'adicionar_cliente.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Verifica se o usuário é administrador ou cliente
            if user.is_staff:
                return redirect('admin_dashboard')  # Redireciona ao painel admin
            else:
                return redirect('listar_clientes')  # Redireciona ao perfil do cliente
    else:
        form = UserLoginForm()
    return render(request, 'login/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def adicionar_usuario(request):
    if not request.user.is_staff:
        raise PermissionDenied

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()

            login(request, user)
            return redirect('listar_clientes')  # Ajuste conforme necessário

    else:
        user_form = UserRegisterForm()
        cliente_form = ClienteForm()

    return render(request, 'adicionar_usuario.html', {
        'user_form': user_form,
        'cliente_form': cliente_form
    })