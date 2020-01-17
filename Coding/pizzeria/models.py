from __future__ import unicode_literals
from django.db import models
from django.db.models import Model
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Order(Model):
    pizza_name = models.CharField(max_length=30)
    size = models.CharField(max_length=30, default="Medium")
    customer_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    phone_number = models.IntegerField(default = '')
    
class Pizza(Model):
    pizza_name = models.CharField(max_length=30)
    size = ArrayField(
            models.CharField(max_length=10)
        )



