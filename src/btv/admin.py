from django.contrib import admin
from .models import Doador, Documento

# Register your models here.

@admin.register(Doador)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Doador._meta.get_fields()]

@admin.register(Documento)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Documento._meta.get_fields()]