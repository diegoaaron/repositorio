from django.db import models

from datetime import date
from django.utils import timezone


# ----------------------------------------
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

# ----------------------------------------


def default_city():
    return "San Diego"

class Store(models.Model):
    #default_address = "unknow"

    def default_address(self):
        return "Av. central S/N - Calle, si te ries, pierdes XD"

    name = models.CharField(max_length=30, default="invitado")
    address = models.CharField(max_length=30, default=default_address)
    city = models.CharField(max_length=30, default=default_city)
    state = models.CharField(max_length=21)
    
    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})"


#    date = models.DateField(default=date.today)
#    datetime = models.DateTimeField(default=timezone.now)
#    date_lastupdated = models.DateField(auto_now=True)
#    date_added = models.DateField(auto_now_add=True)
#    timestamp_lastupdated = models.DateTimeField(auto_now=True)
#    timestamp_added = models.DateTimeField(auto_now_add=True)


ITEM_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('P', 'Portion'),
)


def calorie_watcher(value):
    if value > 5000:
        raise ValidationError(f"Whoa! calories are {value}s? We try to serve healthy food, try somethin less than 5000!",)


class Menu(models.Model):
    name = models.CharField(max_length=30)

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Item name")
    description = models.CharField(max_length=100, db_index=True)
    size = models.CharField(choices=ITEM_SIZES, max_length=1)












