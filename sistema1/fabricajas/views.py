from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Certificado
from django.http import FileResponse
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
    return render(request, 'paginas/index.html')


def nosotros(request):
    return render(request, 'paginas/about.html')


def precio(request):
    return render(request, 'cajas/price.html')


def exhibition(request):
    return render(request, 'cajas/project.html')


def service(request):
    return render(request, 'cajas/service.html')


def segunda(request):
    return render(request, 'cajas/segunda.html')


def certificado(request):
    if request.method == 'POST':
        nit = request.POST['nit']
        anio = request.POST['anio']
        try:
            cliente = Cliente.objects.get(nit=nit)
            certificado = Certificado.objects.get(anio=anio, cliente=cliente)
            return FileResponse(certificado.archivo_pdf, as_attachment=True)
        except (Cliente.DoesNotExist, Certificado.DoesNotExist):
            pass
    return render(request, 'cajas/certificados.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('certificado/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def perfil(request):
    return render(request, 'perfil.html')
