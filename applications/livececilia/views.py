from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from applications.livececilia.forms import LiveCeciliaForm


class LiveCeciliaView(FormView):

    template_name = 'livececilia.html'
    form_class = LiveCeciliaForm
    success_url = reverse_lazy('livececilia_app:livececilia')

    def form_valid(self, form):
        # user = authenticate(
        #     username='root',
        #     password='dulcecarola321-'
        # )
        # login(self.request, user)
        form.save()
        return super(LiveCeciliaView, self).form_valid(form)
