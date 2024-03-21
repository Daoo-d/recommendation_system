from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class HomeTemplate(TemplateView):
    template_name = "User/home.html"
