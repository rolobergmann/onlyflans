from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context, loader
from web.models import Flan, ContactForm
from web.forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required

import os
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)

    context = {'flanes': flanes_publicos}
    return render(request, "index.html", context)

def contacto(request) :
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactFormModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form. cleaned_data as required
            # ...
            # redirect to a new URL:
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactFormModelForm()

    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, "exito.html")
def about(request):
    return render(request, "about.html")

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {'flanes': flanes_privados}
    return render(request, "welcome.html", context)
# Create your views here.
