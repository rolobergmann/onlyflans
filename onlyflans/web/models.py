from django.db import models
from django.contrib import admin
import uuid

class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)

# Clase para administrar el modelo 'Flan'
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'flan_uuid', 'slug', 'is_private')  # Campos a mostrar en la lista
    #readonly_fields = ('flan_uuid',)  # Campos de solo lectura en la edición
    prepopulated_fields = {'slug': ('name',)}  # Genera el slug automáticamente a partir del 'name' 

class ContactForm(models.Model) :
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


# Registro del modelo en el panel de administración
admin.site.register(Flan, FlanAdmin)