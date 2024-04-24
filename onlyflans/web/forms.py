from django import forms
from django.forms import ModelForm
from .models import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create the form class.

class ContactFormForm(forms.Form) :
    # contact form uuid No necesita ser declarado en nuestro form
    customer_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo'}), label='Correo')
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tu nombre'}), label='Nombre')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(forms.ModelForm) :
    class Meta :
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')