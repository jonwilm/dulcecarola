from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from applications.sorteo.forms import SorteoForm


class SorteoView(FormView):

    template_name = 'sorteo.html'
    form_class = SorteoForm
    success_url = reverse_lazy('sorteo_app:sorteo')

    def form_valid(self, form):
        form.save()
        return super(SorteoView, self).form_valid(form)
