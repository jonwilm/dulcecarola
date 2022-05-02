from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from applications.newsletter.forms import NewsletterForm


def newsletter(request):

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()


class HomeView(TemplateView):

    template_name = 'home.html'
