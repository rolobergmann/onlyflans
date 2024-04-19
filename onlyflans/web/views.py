from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from web.models import Flan

import os
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)

    context = {'flanes': flanes_publicos}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {'flanes': flanes_privados}
    return render(request, "welcome.html", context)
# Create your views here.
