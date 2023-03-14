from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect 
from hashlib import sha256

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status' : status})

def login(request):
    return render(request, 'login.html')    

def validacao(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    usuario = Usuario.objects.filter(email=email)
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/cadastro/?status=0')
    
    if len(senha) < 6:
        return redirect('/cadastro/?status=1')
    
    if len(usuario) > 0:
        return redirect('/cadastro/?status=2')
    try: 
        senha = sha256(senha.encode()).hexdigest()                  
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        
        return redirect('/cadastro/?status=3')
    except:
        return redirect('/cadastro/?status=4')

    