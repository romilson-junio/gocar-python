# Generated by Django 4.0.5 on 2022-06-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0002_remove_carro_pathimagem_carro_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='carros'),
        ),
    ]
