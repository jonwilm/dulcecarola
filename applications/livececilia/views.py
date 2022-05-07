from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from applications.livececilia.forms import LiveCeciliaForm


class LiveCeciliaView(SuccessMessageMixin, FormView):

    template_name = 'livececilia.html'
    form_class = LiveCeciliaForm
    success_url = reverse_lazy('livececilia_app:livececilia')
    success_message = 'Anotado satisfactoriamente'

    def form_valid(self, form):
        form.save()
        return super(LiveCeciliaView, self).form_valid(form)
