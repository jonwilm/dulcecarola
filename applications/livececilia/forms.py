from django import forms
from django.core.exceptions import ValidationError

from applications.livececilia.models import LiveCecilia


product_genere = [
    ('', 'Seleccione...'),
    ('F', 'Femenino'),
    ('M', 'Masculino'),
    ('O', 'Otro'),
    ('NC', 'No contesta'),
]

product_city = [
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

class LiveCeciliaForm(forms.Form):

    firstname = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    lastname = forms.CharField(
        label='Apellido',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    date_nac = forms.DateField(
        label='Fecha de nacimiento',
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    genere = forms.CharField(
        label='Género',
        required=False,
        widget=forms.Select(
            choices=product_genere,
            attrs={
                'class': 'form-select',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    code_zip = forms.CharField(
        label='Código postal',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    city = forms.CharField(
        label='Provincia',
        required=False,
        widget=forms.Select(
            choices=product_city,
            attrs={
                'class': 'form-select',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    phone = forms.CharField(
        label='Teléfono',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))

    def clean_email(self):
        email = self.cleaned_data['email']
        if LiveCecilia.objects.filter(email=email).exists():
            raise ValidationError(
                "Email ya se encuentra resgistrado")
        return email


    def save(self, *args, **kwargs):
        data = self.cleaned_data
        LiveCecilia.objects.get_or_create(
            firstname=data['firstname'],
            lastname=data['lastname'],
            date_nac=data['date_nac'],
            genere=data['genere'],
            code_zip=data['code_zip'],
            city=data['city'],
            email=data['email'],
            phone=data['phone'],
            defaults={}
        )
