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


    # def save(self, *args, **kwargs):
    #     data = self.cleaned_data
    #     Newsletter.objects.get_or_create(
    #         email=data['email'],
    #         defaults={}
    #     )
