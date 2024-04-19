from django import forms
import uuid
# Create the form class.

class ContactForm(forms.Form):
    contact_form_uuid = forms.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = forms.EmailField(help_text="Ej:a@b.com", label="Email")
    customername = forms.CharField(max_length=64, label= "Nombre")
    message = forms.CharField(widget=forms.Textarea({"size":100}), label="Comentario")