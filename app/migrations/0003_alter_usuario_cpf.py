# Generated by Django 5.1.2 on 2024-10-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_contato_options_alter_material_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=100, verbose_name='CPF do usuário'),
        ),
    ]