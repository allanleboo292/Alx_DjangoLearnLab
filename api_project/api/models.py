from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)