from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=64)

class Breadcrumb(models.Model):
    product = models.ForeignKey(Product)
    datetime = models.DateTimeField()
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)
    elevation = models.CharField(max_length=32)
