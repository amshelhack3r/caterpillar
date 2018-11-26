from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class hello(TemplateView):
    template_name = 'index.html'
