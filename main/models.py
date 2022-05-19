from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    language = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
