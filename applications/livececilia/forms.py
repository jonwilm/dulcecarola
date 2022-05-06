from django import forms
from applications.livececilia.models import LiveCecilia


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
    date_nac = forms.CharField(
        label='Fecha de nacimiento',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '',
                'autocomplete': 'off',
            }
        ))
    genere = forms.CharField(
        label='Genero',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
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
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
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

    # def clean(self):
    # password = self.cleaned_data['password']

    # if not authenticate(username='Asistente', password=password):
    #     raise forms.ValidationError(
    #         'Contraseña Incorrecta'
    #     )

    # return self.cleaned_data

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
