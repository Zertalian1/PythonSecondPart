from django.db import models


class University(models.Model):
    full_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    date_of_creation = models.DateField()
