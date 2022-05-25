from django.db import models


class Sorteo(models.Model):

    firstname = models.CharField('Nombre', max_length=200)
    lastname = models.CharField('Apellido', max_length=200)
    date_nac = models.DateField('Fecha de Nacimiento')
    genere = models.CharField('Género', max_length=2)
    code_zip = models.CharField('Código Postal', max_length=10, blank=True)
    city = models.CharField('Ciudad', max_length=3)
    email = models.CharField('Email', max_length=80, unique=True)
    phone = models.CharField('Teléfono', max_length=15)
    created_at = models.DateTimeField('Fecha de suscripción', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'

    def __str__(self):
        return self.email
