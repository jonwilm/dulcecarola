from django.db import models


class Sorteo(models.Model):

    PRODUCT_GENERE = [
        ('', 'Seleccione...'),
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro'),
        ('NC', 'No contesta'),
    ]

    PRODUCT_CITY = [
        ('', 'Seleccione...'),
        ('1', 'Buenos Aires'),
        ('2', 'Ciudad Autónoma de Buenos Aires'),
        ('3', 'Catamarca'),
        ('4', 'Chaco'),
        ('5', 'Chubut'),
        ('6', 'Córdoba'),
        ('7', 'Corrientes'),
        ('8', 'Entre Ríos'),
        ('9', 'Formosa'),
        ('10', 'Jujuy'),
        ('11', 'La Pampa'),
        ('12', 'La Rioja'),
        ('13', 'Mendoza'),
        ('14', 'Misiones'),
        ('15', 'Neuquén'),
        ('16', 'Río Negro'),
        ('17', 'Salta'),
        ('18', 'San Juan'),
        ('19', 'San Luis'),
        ('20', 'Santa Cruz'),
        ('21', 'Santa Fe'),
        ('22', 'Santiago del Estero'),
        ('23', 'Tierra del Fuego'),
        ('24', 'Tucumán'),
    ]
    firstname = models.CharField('Nombre', max_length=200, null=False)
    lastname = models.CharField('Apellido', max_length=200, null=False)
    date_nac = models.DateField('Fecha de Nacimiento', null=False)
    genere = models.CharField('Género', max_length=2, null=False, choices=PRODUCT_GENERE)
    code_zip = models.CharField('Código Postal', max_length=10, blank=True, null=True)
    city = models.CharField('Ciudad', max_length=3, null=False, choices=PRODUCT_CITY)
    email = models.CharField('Email', max_length=80, unique=True, null=False)
    phone = models.CharField('Teléfono', max_length=15, null=False)
    created_at = models.DateTimeField('Fecha de suscripción', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'

    def __str__(self):
        return self.email
