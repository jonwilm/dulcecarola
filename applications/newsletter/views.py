# django
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# apps
from applications.newsletter.models import Newsletter

# other
import json


@csrf_exempt
def newsletter(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        n, t = Newsletter.objects.get_or_create(
            email=data['newsletter'],
            defaults={}
        )
    return JsonResponse({ 'guardado': t })


class HomeView(TemplateView):

    template_name = 'home.html'
