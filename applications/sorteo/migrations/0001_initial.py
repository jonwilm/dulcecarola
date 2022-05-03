# Generated by Django 3.2.13 on 2022-05-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sorteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre y Apellido')),
                ('date_nac', models.DateField(verbose_name='Fecha de Naciemiento')),
                ('genero', models.CharField(max_length=2, verbose_name='Género')),
                ('code_zip', models.CharField(max_length=10, verbose_name='Código Postal')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('email', models.CharField(max_length=80, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de suscripción')),
            ],
            options={
                'verbose_name': 'Sorteo',
                'verbose_name_plural': 'Sorteo',
            },
        ),
    ]
