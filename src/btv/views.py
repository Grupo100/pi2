from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UploadForm
from .models import Doador, Documento

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,"home.html", {})

def quem_somos(request,*args, **kwargs):
    return render(request,"quem_somos.html", {})

def transparencia(request,*args, **kwargs):
    doadores = Doador.objects.all()
    documentos = Documento.objects.all()
    return render(request,"transparencia.html", {'doadores': doadores, 'documentos': documentos})

def doar(request,*args, **kwargs):
    return render(request,"doar.html", {})

def administrativa(request,*args, **kwargs):
    if request.user.is_authenticated:
        form = UploadForm()
        doadores = Doador.objects.all()
        documentos = Documento.objects.all()
        return render (request , 'areaadm/restrito.html', {"form": form, "doadores":doadores, "documentos":documentos})
    else:
        return render(request,"administrativa.html", {})

def create(request):
    return render (request , 'areaadm/create.html')

def store(request):
    data = {}
    if (request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação diferentes! Digite novamente!'
        data['class'] = 'alertaer'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuario cadastrado! '
        data['class'] = 'alerta'
    return render (request , 'areaadm/create.html', data)
    
def loginview(request):
        data = {}
        user = authenticate(username=request.POST['user'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/areaadm/')
        else:
            data['msg'] = 'Senha ou usuario invalidos!'
            data['class'] = 'alertaer'
            return render (request , 'administrativa.html', data)

def areaadm(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/transparencia/')
    else:
        form = UploadForm()
        doadores = Doador.objects.all()
        documentos = Documento.objects.all()
        return render (request , 'areaadm/restrito.html', {'form':form, "doadores":doadores, "documentos":documentos})

def delete_doc(request, pk):
    if request.method == 'POST':
        documento = Documento.objects.get(pk=pk)
        documento.delete()
    return redirect('/transparencia/')

def logoff(request):
    logout(request)
    return render (request , 'administrativa.html')