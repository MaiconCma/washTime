from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from produto.forms import UserRegisterForm

from .forms import ClienteForm
from .models import Cliente


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
                messages.success(request, 'Cliente atualizado com sucesso!')
                return redirect('listar_cliente')
        else:
            form = ClienteForm(instance=cliente)
        return render(request, 'editar_cliente.html', {'form': form})
    else:
        raise PermissionDenied


@login_required
def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.user.is_staff or request.user == cliente.user:
        if request.method == 'POST':
            cliente.delete()
            messages.success(request, 'Cliente excluído com sucesso!')
            return redirect('listar_cliente')
        return render(request, 'excluir_cliente.html', {'cliente': cliente})
    else:
        raise PermissionDenied


@login_required
def listar_cliente(request):
    clientes = Cliente.objects.filter(user=request.user)
    return render(request, 'listar_cliente.html', {'clientes': clientes})  # Corrigi o nome da variável


@login_required
def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
            cliente.save()
            messages.success(request, 'Cliente adicionado com sucesso!')
            return redirect('listar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'adicionar_cliente.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('listar_cliente')
    else:
        form = UserLoginForm()
    return render(request, 'login/login.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
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
            messages.success(request, 'Usuário e cliente adicionados com sucesso!')
            return redirect('listar_cliente')

    else:
        user_form = UserRegisterForm()
        cliente_form = ClienteForm()

    return render(request, 'adicionar_usuario.html', {
        'user_form': user_form,
        'cliente_form': cliente_form
    })
