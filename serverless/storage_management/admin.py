from django.contrib import admin
from .models import *


@admin.register(Author, ItemImage, Item, Location, DetailPosition, Category, Series, ItemFile)
class GlacierAdmin(admin.ModelAdmin):
    pass
