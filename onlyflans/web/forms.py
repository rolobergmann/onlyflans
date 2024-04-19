from django import forms

# Create the form class.

class ContactFormForm(forms.Form) :
    # contact form uuid No necesita ser declarado en nuestro form
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')