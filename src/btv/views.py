from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request,"home.html", {})

def quem_somos(request,*args, **kwargs):
    return render(request,"quem_somos.html", {})

def transparencia(request,*args, **kwargs):
    return render(request,"transparencia.html", {})

def doar(request,*args, **kwargs):
    return render(request,"doar.html", {})

def administrativa(request,*args, **kwargs):
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
    return render (request , 'areaadm/restrito.html')

def logoff(request):
    logout(request)
    return render (request , 'administrativa.html')