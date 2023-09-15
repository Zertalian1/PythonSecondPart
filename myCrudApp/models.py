from django.db import models


class University(models.Model):
    full_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    date_of_creation = models.DateField()


class Student(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    FCs = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    year_of_admission = models.DateField()
