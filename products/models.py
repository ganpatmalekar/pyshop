from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return f"{self.name}"


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    discount = models.FloatField()

