from django import forms
from applications.sorteo.models import Sorteo


class SorteoForm(forms.Form):

    name = forms.CharField(
        label='Nombre y Apellido',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre y apellido',
                'autocomplete': 'off',
            }
        ))
    date_nac = forms.CharField(
        label='Fecha de nacimiento',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su fecha de nacimiento',
                'autocomplete': 'off',
            }
        ))
    genere = forms.CharField(
        label='Genero',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su genero',
                'autocomplete': 'off',
            }
        ))
    code_zip = forms.CharField(
        label='Código postal',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su codigo postal',
                'autocomplete': 'off',
            }
        ))
    city = forms.CharField(
        label='Ciudad',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su ciudad',
                'autocomplete': 'off',
            }
        ))
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su email',
                'autocomplete': 'off',
            }
        ))
    phone = forms.CharField(
        label='Teléfono',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su telefono',
                'autocomplete': 'off',
            }
        ))

    # def clean(self):
        # password = self.cleaned_data['password']

        # if not authenticate(username='Asistente', password=password):
        #     raise forms.ValidationError(
        #         'Contraseña Incorrecta'
        #     )

        # return self.cleaned_data

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        Sorteo.objects.get_or_create(
            name=data['name'],
            date_nac=data['date_nac'],
            genere=data['genere'],
            code_zip=data['code_zip'],
            city=data['city'],
            email=data['email'],
            phone=data['phone'],
            defaults={}
        )
