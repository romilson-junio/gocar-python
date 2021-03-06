# Generated by Django 4.0.5 on 2022-06-12 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localRetirada', models.CharField(max_length=100)),
                ('dataRetirada', models.DateField()),
                ('dataDevolucao', models.DateField()),
                ('horaRetirada', models.TimeField()),
                ('horaDevolucao', models.TimeField()),
                ('idCliente', models.IntegerField()),
                ('idCarro', models.IntegerField()),
                ('valor', models.FloatField()),
            ],
        ),
    ]
