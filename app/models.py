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
    senha = models.CharField(max_length=100, verbose_name= "Senha do usuário")
    ocupacao_do_usuario = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
   
    def __str__(self):
        return f'{self.nome}, {self.email}'
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    
class Perguntas(models.Model):    
    enunciado = models.CharField(max_length=100, verbose_name="Enunciado da pergunta")
    alternativa_a = models.CharField(max_length=100, verbose_name="Alternativa A")
    alternativa_b = models.CharField(max_length=100, verbose_name="Alternativa B")
    alternativa_c = models.CharField(max_length=100, verbose_name="Alternativa C")
    alternativa_d = models.CharField(max_length=100, verbose_name="Alternativa D")
    alternativa_correta = models.CharField(max_length=100, verbose_name="Alternativa correta")

    def __str__(self):
        return self.enunciado
    
    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"
    

class Questionario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do questionário")
    data_criacao = models.DateField(verbose_name="Data de criação do questionário")
    nivel = models.CharField(max_length=100, verbose_name="Nível do questionário")
    perguntas = models.ManyToManyField(Perguntas, verbose_name="Perguntas do questionário")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Questionário"
        verbose_name_plural = "Questionários"

class Material(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do material")
    conteudo = models.TextField(verbose_name="Conteúdo do material")  # Alterado para TextField para suportar conteúdo maior
    administrador = models.CharField(max_length=100, verbose_name="Administrador do material")
    questionario_do_material = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    # tipo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
            return f'{self.nome}, {self.conteudo},{self.questionario_do_material}'
    
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"
    

class MaterialAdicionado(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario}, {self.material}'
    
    class Meta:
        verbose_name = "Material Adicionado"
        verbose_name_plural = "Materiais Adicionados"
    

class Contato(models.Model):
    texto = models.CharField(max_length=1000, verbose_name="Texto do e-mail")

    def __str__(self):
        return self.texto
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"