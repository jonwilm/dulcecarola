from django import forms
from applications.newsletter.models import Newsletter


class NewsletterForm(forms.Form):

    email = forms.EmailField(
        label='Ingrese su email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder': 'Ingrese su email',
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
        Newsletter.objects.get_or_create(
            email=data['email'],
            defaults={}
        )
