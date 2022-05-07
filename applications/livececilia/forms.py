from django import forms
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

    name = forms.CharField(
        label='Nombre y Apellido',
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
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    genere = forms.CharField(
        label='Genero',
        required=True,
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
        required=True,
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
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))


    def save(self, *args, **kwargs):
        data = self.cleaned_data
        LiveCecilia.objects.get_or_create(
            name=data['name'],
            date_nac=data['date_nac'],
            genere=data['genere'],
            code_zip=data['code_zip'],
            city=data['city'],
            email=data['email'],
            phone=data['phone'],
            defaults={}
        )
