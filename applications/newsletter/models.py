from django.db import models


class Newsletter(models.Model):

    email = models.CharField('Email', max_length=80)
    created_at = models.DateTimeField(
        'Fecha de suscripción', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Suscrito'
        verbose_name_plural = 'Suscritos'

    def __str__(self):
        return self.email
