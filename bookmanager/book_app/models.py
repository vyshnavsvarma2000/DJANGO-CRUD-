from django.db import models


class Book(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    author = models.CharField(max_length=50)


