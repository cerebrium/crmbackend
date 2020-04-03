from djmoney.models.fields import MoneyField
import locale
from django.db import models
#from djmoney.money import Money
from django.contrib.auth.models import User, Group



# Create your models here.
class Employee(models.Model):
    # all fields needed for the daily feeling sheet report 
    name = models.CharField(max_length=100)
    inOff = models.IntegerField(default=0)
    location = models.CharField(max_length = 10)
    route = models.CharField(max_length = 10)
    logIn = models.DateTimeField(null=True, blank=True)
    logOut = models.DateTimeField(null=True, blank=True)
    #TORH = models.DateTimeField()
    milage = models.IntegerField(default=0)
    parcel = models.IntegerField(default=0)
    LWP = models.IntegerField(default=0)
    LVP = models.IntegerField(default=0)
    CRT = models.IntegerField(default=0)
    RL = models.IntegerField(default=0)
    SUP = MoneyField(max_digits=19, decimal_places=4, default_currency='GBP')
    #deductions
    fuel = MoneyField(max_digits=19, decimal_places=4, default_currency='GBP')
    support_deducitons = MoneyField(max_digits=19, decimal_places=4, default_currency='GBP')
    vans = MoneyField(max_digits=19, decimal_places=4, default_currency='GBP')

    
    # @property
    # def TORH(self):
    #     self.TORH = self.logOut - self.logIn
    #     return self.TORH


    # @property
    # def SUP_display(self):
    #     return "$%s" % self.SUP