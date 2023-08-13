from django.contrib import admin

# Register your models here.
from .models import Coche,Accidente

admin.site.register(Coche)
admin.site.register(Accidente)
