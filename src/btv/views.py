from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,"home.html", {})

def quem_somos(request,*args, **kwargs):
    return render(request,"quem_somos.html", {})

def localizacao(request,*args, **kwargs):
    return render(request,"localizacao.html", {})

def transparencia(request,*args, **kwargs):
    return render(request,"transparencia.html", {})

def doar(request,*args, **kwargs):
    return render(request,"doar.html", {})

def administrativa(request,*args, **kwargs):
    return render(request,"administrativa.html", {})