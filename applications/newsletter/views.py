from crypt import methods
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from applications.newsletter.models import Newsletter

import json

@csrf_exempt
def newsletter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        n, t = Newsletter.objects.get_or_create(
            email=data['mailNewsletter'],
            defaults={}
        )
    return JsonResponse({'newsletterStatus': t})


class HomeView(TemplateView):

    template_name = 'home.html'


class EstadisticasView(TemplateView):

    template_name = 'estadisticas.html'


class TestimoniosView(TemplateView):

    template_name = 'testimonios.html'
