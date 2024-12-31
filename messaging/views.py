from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Mensaje
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MensajeListView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'messaging/mensaje_list.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user)
