from django.db import models

class Book(models.Model):
    name = models.CharField(
        max_length=200
        )
    journal = models.CharField(
        max_length=200
        )
    author = models.CharField(
        max_length=200
        )
    published_date = models.DateField()

    description = models.TextField()

    publisher = models.CharField(
        max_length=200
        )

    def __str__(self):
        return self.name
