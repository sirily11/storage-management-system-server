from django.contrib import admin
from storage_management.models import *


@admin.register(Author, ItemImage, Item, Location, DetailPosition, Category, Series)
class GlacierAdmin(admin.ModelAdmin):
    pass
