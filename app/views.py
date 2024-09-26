from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

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

def ViewMaterial(request):
    tipo = request.GET.get('tipo')  # Obtém o parâmetro 'tipo'
    material = None

    if tipo:
        material = Material.objects.filter(tipo=tipo).first()  # Filtra o material

    return render(request, 'material.html', {'material': material})

class ViewContato(View):
    def get(self, request, *args, **kwargs):
        contato = Contato.objects.all()
        return render(request, 'contato.html', {'contato':contato})

class ViewMaterialAdicionado(View):
    def get(self, request, *args, **kwargs):
        materialadicionado = MaterialAdicionado.objects.all()
        return render(request, 'material.html', {'materialadicionado': materialadicionado})
