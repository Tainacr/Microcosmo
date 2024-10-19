from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import CadastroForm, LoginForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class ViewUsuario(View):
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuario':usuario})

class ViewQuestionario(View):
    def get(self, request, *args, **kwargs):
        questionario = Questionario.objects.all()
        return render(request, 'questionario.html', {'questionario':questionario})

class ViewQuestionario2(View):
    def get(self, request, *args, **kwargs):
        questionario2 = Questionario.objects.all()
        return render(request, 'questionario2.html', {'questionario2':questionario2})

def ViewMaterial(request):
    tipo = request.GET.get('tipo')
    material = None

    if tipo:
        material = Material.objects.filter(tipo=tipo).first() 

    return render(request, 'material.html', {'material': material})

def ViewMaterial2(request):
    tipo = request.GET.get('tipo') 
    material2 = None

    if tipo:
        material2 = Material.objects.filter(tipo=tipo).first() 

    return render(request, 'material2.html', {'material2': material2})

class ViewContato(View):
    def get(self, request, *args, **kwargs):
        contato = Contato.objects.all()
        return render(request, 'contato.html', {'contato':contato})

class ViewMaterialAdicionado(View):
    def get(self, request, *args, **kwargs):
        materialadicionado = MaterialAdicionado.objects.all()
        return render(request, 'material.html', {'materialadicionado': materialadicionado})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')  
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['user']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(cpf=cpf, senha=password)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('index')  
            except Usuario.DoesNotExist:
                messages.error(request, "CPF ou senha inválidos.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

