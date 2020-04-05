from djmoney.models.fields import MoneyField
import locale
from django.db import models
from datetime import datetime
# from djmoney.money import Money
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField







# Create your models here.
class Employee(models.Model):
    # all fields needed for the daily feeling sheet report 
    inOff = models.IntegerField(default=0)
    name = models.CharField(default='', max_length = 30)
    location = models.CharField(max_length = 10)
    route = models.CharField(max_length = 10)
    logIn = models.DateTimeField(null=True, blank=True)
    logOut = models.DateTimeField(null=True, blank=True)
    mileage = models.IntegerField(default=0)
    parcel = models.IntegerField(default=0)
    LWP = models.IntegerField(default=0)
    LVP = models.IntegerField(default=0)
    CRT = models.IntegerField(default=0)
    RL = models.IntegerField(default=0)
    SUP = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')
    fuel = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')
    vans = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')
    supportDeductions = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')
    
    #create list to store dates 
    datesList = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)


    

    #TORH = models.DateField(default = hr_diff(logIn,logOut))