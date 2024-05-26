from django.contrib import admin
from .models import PasswordModle

# Register your models here.
@admin.register(PasswordModle)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ("website", "username", "password","remarks")