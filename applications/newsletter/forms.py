from django import forms
from applications.newsletter.models import Newsletter


class NewsletterForm(forms.Form):

    email = forms.EmailField(
        label='Ingrese su email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'autocomplete': 'off',
            }
        ))
