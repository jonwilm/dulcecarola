from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from applications.sorteo.forms import SorteoForm


class SorteoView(FormView):

    template_name = 'sorteo.html'
    form_class = SorteoForm
    success_url = reverse_lazy('sorteo_app:sorteo')

    def form_valid(self, form):
        user = authenticate(
            username='root',
            password='dulcecarola321-'
        )
        login(self.request, user)
        form.save()
        return super(SorteoView, self).form_valid(form)
