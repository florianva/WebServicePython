from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=42)
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titre
