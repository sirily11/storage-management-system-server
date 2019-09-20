from django.db import models
from django.utils.translation import gettext as _
import uuid


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, default="Book", unique=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=128, default="No content here", unique=True)
    description = models.TextField(max_length=1024, blank=True, null=True, default="")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=128, default="", unique=True)
    description = models.TextField(max_length=1024, default="No content here", null=True, blank=True)

    def __str__(self):
        return self.name


# Address
class Location(models.Model):
    country = models.CharField(max_length=128, default="China")
    city = models.CharField(max_length=128, default="Shenzhen")
    street = models.CharField(max_length=128, default="Qian Hai Lu", null=True, blank=True)
    building = models.CharField(max_length=128, default="Tian Lang Feng Qing", null=True, blank=True)
    unit = models.CharField(max_length=128, default="Tian Qi Yuan", null=True, blank=True)
    room_number = models.CharField(max_length=128, default="605")

    def __str__(self):
        return f"{self.country}{self.city}{self.building}"


class DetailPosition(models.Model):
    position = models.CharField(max_length=1024, default="Book Shelf 1")
    description = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.position


class Item(models.Model):
    unit_choices = [("USD", "美元"), ("HDK", "港币"), ("CNY", "人民币")]

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True, blank=True)
    name = models.CharField(max_length=1024, default="", verbose_name=_("Item Name"),
                            help_text="Please Enter your item name")
    description = models.TextField(max_length=1024, blank=True, null=True,
                                   help_text="Please enter your item description")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(default=0.0)
    qr_code = models.CharField(max_length=10008, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    detail_position = models.ForeignKey(DetailPosition, on_delete=models.SET_NULL, blank=True, null=True
                                        )
    column = models.IntegerField(default=1)
    row = models.IntegerField(default=1)
    unit = models.CharField(max_length=10, default="USD", choices=unit_choices)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    title = models.CharField(max_length=128, default="Face", null=True, blank=True)
    image = models.ImageField(verbose_name=_("Item Image"), upload_to="item-image")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Image-{self.item.name.title()}"


class ItemFile(models.Model):
    file = models.CharField(default="", max_length=1024)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"File-{self.item.name.title()}"
