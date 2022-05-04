from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from applications.newsletter.forms import NewsletterForm


# def newsletter(self, request):
#     if request.method == 'POST':
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username='root',
#                 password='dulcecarola321-'
#             )
#             login(self.request, user)
#             form.save()


class HomeView(TemplateView):

    template_name = 'home.html'


class EstadisticasView(TemplateView):

    template_name = 'estadisticas.html'
