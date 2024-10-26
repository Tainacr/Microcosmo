from django.db import models

class Ocupacao(models.Model):
    ocupacao = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return self.ocupacao

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do usuário")
    cpf = models.CharField(max_length=100, verbose_name="CPF do usuário")
    email = models.CharField(max_length=100, verbose_name="E-mail do usuário")
    senha = models.CharField(max_length=100, verbose_name="Senha do usuário")
    ocupacao_do_usuario = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}, {self.email}'

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Questionario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do questionário")
    data_criacao = models.DateField(verbose_name="Data de criação do questionário")
    nivel = models.CharField(max_length=100, verbose_name="Nível do questionário")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Questionário"
        verbose_name_plural = "Questionários"


class Pergunta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.CharField(max_length=255, verbose_name="Texto da Pergunta")

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"


class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='alternativas')
    texto = models.CharField(max_length=255, verbose_name="Texto da Alternativa")
    is_correta = models.BooleanField(default=False, verbose_name="É a alternativa correta?")

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"


class Material(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, verbose_name="id do material")
    nome = models.CharField(max_length=100, verbose_name="Nome do material")
    conteudo = models.TextField(verbose_name="Conteúdo do material")
    administrador = models.CharField(max_length=100, verbose_name="Administrador do material")
    questionario_do_material = models.ForeignKey(Questionario, on_delete=models.CASCADE, verbose_name="Questionário relacionado")

    def __str__(self):
        return f'{self.nome}, {self.conteudo}, {self.questionario_do_material}'

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

class Contato(models.Model):
    texto = models.CharField(max_length=1000, verbose_name="Texto do e-mail")

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
