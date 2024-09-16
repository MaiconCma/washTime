from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=username).exists():
            return HttpResponse('Usuário já existe')

        user = User.objects.create_user(username=username, email=  email, password=senha)

        user.save()

        return HttpResponse('Usuario cadastrado com sucesso ' + username)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login_django(request, user)
            
            
            return redirect('listar_cliente')
        else:
            return redirect('cadastro')

def plataforma(request):
    if request.user.is_authenticated:
        return render(request, 'listar_cliente')
    
    return HttpResponse('Voce não está autenticado')