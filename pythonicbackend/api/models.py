from djmoney.models.fields import MoneyField
import locale
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField
from django.db import models



# Create your models here.
class Employee(models.Model):
    # all fields needed for the daily feeling sheet report 
    inOff = models.IntegerField(default=0)
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
    datesList = ArrayField(models.CharField(max_length=50), default=list)
    
    #deductions
    # TORH = models.DateTimeField()

    
    # @property
    # def TORH(self):
    #     self.TORH = self.logOut - self.logIn
    #     return self.TORH


    # @property
    # def SUP_display(self):
    #     return "$%s" % self.SUP