from django.shortcuts import render, redirect, get_object_or_404 
from .models import *
from django.views import View
from django.contrib import messages
from .forms import CadastroForm, LoginForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ViewQuestionario(View):
    def get(self, request, questionario_id):
        questionario = get_object_or_404(Questionario, id=questionario_id)
        perguntas = questionario.perguntas.all()  # Obter todas as perguntas do questionário
        return render(request, 'questionario.html', {'questionario': questionario, 'perguntas': perguntas})

    def post(self, request, questionario_id):
        questionario = get_object_or_404(Questionario, id=questionario_id)
        perguntas = questionario.perguntas.all()

        pontuacao = 0
        for pergunta in perguntas:
            resposta = request.POST.get(str(pergunta.id))
            if resposta:  # Verifica se uma resposta foi fornecida
                try:
                    alternativa = Alternativa.objects.get(id=resposta)
                    if alternativa.is_correta:  # Verifica se a alternativa é a correta
                        pontuacao += 1
                except Alternativa.DoesNotExist:
                    continue  # Ignora caso a alternativa não exista

        # Renderiza a página de resultado com a pontuação
        return render(request, 'resultado.html', {'pontuacao': pontuacao, 'total': len(perguntas)})


class ViewListaQuestionarios(View):
    def get(self, request):
        questionarios = Questionario.objects.all()
        return render(request, 'lista_questionarios.html', {'questionarios': questionarios})


class ViewUsuario(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})


def ViewMaterial(request):
    material = Material.objects.first()
    return render(request, 'material.html', {'material': material})


def ViewMaterial2(request):
    material2 = Material.objects.filter(id=2).first()
    return render(request, 'material2.html', {'material2': material2})


def contato(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        texto = request.POST.get('texto')

        Contato.objects.create(texto=f"Email: {email}\nMensagem: {texto}")

        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato') 

    return render(request, 'contato.html')


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
