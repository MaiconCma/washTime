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

        return redirect(login)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login_django(request, user)
            
            
            return redirect('plataforma')
        else:
            return redirect('login')

def plataforma(request):
    if request.user.is_authenticated:
        return render(request, 'inicial.html')
    
    return HttpResponse('Voce não está autenticado')