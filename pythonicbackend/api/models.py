from django.db import models

# Create your models here.
class Employee(models.Model):
    #text
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    inOff = models.CharField(max_length=50)
    milesDriven = models.IntegerField()