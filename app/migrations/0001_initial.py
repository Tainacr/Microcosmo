# Generated by Django 5.1.2 on 2024-10-21 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=1000, verbose_name='E-mail do usuário')),
                ('texto', models.CharField(max_length=1000, verbose_name='Texto do e-mail')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacao', models.CharField(max_length=100, verbose_name='Ocupação')),
            ],
            options={
                'verbose_name': 'Ocupação',
                'verbose_name_plural': 'Ocupações',
            },
        ),
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100, verbose_name='Enunciado da pergunta')),
                ('alternativa_a', models.CharField(max_length=100, verbose_name='Alternativa A')),
                ('alternativa_b', models.CharField(max_length=100, verbose_name='Alternativa B')),
                ('alternativa_c', models.CharField(max_length=100, verbose_name='Alternativa C')),
                ('alternativa_d', models.CharField(max_length=100, verbose_name='Alternativa D')),
                ('alternativa_correta', models.CharField(max_length=100, verbose_name='Alternativa correta')),
            ],
            options={
                'verbose_name': 'Pergunta',
                'verbose_name_plural': 'Perguntas',
            },
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do questionário')),
                ('data_criacao', models.DateField(verbose_name='Data de criação do questionário')),
                ('nivel', models.CharField(max_length=100, verbose_name='Nível do questionário')),
                ('perguntas', models.ManyToManyField(to='app.perguntas', verbose_name='Perguntas do questionário')),
            ],
            options={
                'verbose_name': 'Questionário',
                'verbose_name_plural': 'Questionários',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do material')),
                ('conteudo', models.TextField(verbose_name='Conteúdo do material')),
                ('administrador', models.CharField(max_length=100, verbose_name='Administrador do material')),
                ('questionario_do_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.questionario')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do usuário')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF do usuário')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail do usuário')),
                ('senha', models.CharField(max_length=100, verbose_name='Senha do usuário')),
                ('ocupacao_do_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='MaterialAdicionado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.material')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
            options={
                'verbose_name': 'Material Adicionado',
                'verbose_name_plural': 'Materiais Adicionados',
            },
        ),
    ]
