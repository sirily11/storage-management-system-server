from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Glacier, Vault, File)
class GlacierAdmin(admin.ModelAdmin):
    pass
