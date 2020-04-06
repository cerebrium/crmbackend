from djmoney.models.fields import MoneyField
import locale
from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField
from datetime import datetime



# Create your models here.
class Employee(models.Model):
    # all fields needed for the daily feeling sheet report 
    name = models.CharField(max_length = 30)
    inOff = models.IntegerField(default=0,editable=True)
    location = models.CharField(max_length = 10,editable=True)
    route = models.CharField(max_length = 10,editable=True)
    logIn = models.DateTimeField(null=True, blank=True, editable=True)
    logOut = models.DateTimeField(null=True, blank=True, editable=True)
    mileage = models.IntegerField(default=0,editable=True)
    parcel = models.IntegerField(default=0,editable=True)

    
    LWP = models.IntegerField(default=0)
    LVP = models.IntegerField(default=0)
    CRT = models.IntegerField(default=0)
    RL = models.IntegerField(default=0)
    SUP = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')

    #the following fields are money deducion fields
    fuel = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')
    vans = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')
    supportDeductions = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP')

    #arrayList for storing the the driver has been on the road ()
    datesList =  ArrayField(models.CharField(max_length=10), default=list)

    def __str__(self):
        return self.name
    
    
    #deductions
    # TORH = models.DateTimeField()

    
    # @property
    # def TORH(myVar, yourVar):
    #     return myVar, yourVar



    # @property
    # def SUP_display(self):
    #     return "$%s" % self.SUP