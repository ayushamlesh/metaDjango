from django.db import models
from unicodedata import name
# Create your models here.


class menu(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " : "+self.desc + " Rs. " + self.price
