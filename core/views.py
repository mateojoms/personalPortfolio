from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError

from .models import *

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = super().get_context_data()

        context['about'] = about.objects.first()
        context['services'] = service.objects.all()
        context['works'] = recentWorks.objects.all()

        return context



class testmonial(TemplateView):
    template_name = 'testmonials.html'


    def get_context_data(self):
        context = super().get_context_data()

        context['client'] = client.objects.all()

        return context


