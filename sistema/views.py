from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindo ao sistema veterinário")

def cadastro(request):
    return HttpResponse("Página de cadastro")

def login(request):
    return HttpResponse("Página de login")    
