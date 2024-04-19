from django import forms
from django.forms import ModelForm
from .models import ContactForm

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