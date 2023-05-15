from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente, Certificado

admin.site.register(Cliente)
admin.site.register(Certificado)
