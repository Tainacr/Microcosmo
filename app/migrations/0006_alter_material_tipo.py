# Generated by Django 5.1.1 on 2024-09-26 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_tipomaterial_alter_material_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tipomaterial'),
        ),
    ]