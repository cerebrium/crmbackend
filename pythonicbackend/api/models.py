from djmoney.models.fields import MoneyField
import locale
from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField
import datetime
from django import forms
from django.utils import timezone
import pytz


# Create your models here.
# new model .... i followed this websites syntax exactly https://docs.djangoproject.com/en/3.0/ref/models/instances/
class DriverManager(models.Manager):
    def create_driver(self, name):
        driver = self.create(name=name)

        return driver
    

#----rename it to Driver(models.model)
class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30, null = True)
    location = models.CharField(max_length = 15, default = 'DBS2', null = True)
    documents = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    vehicleDocuments = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    datesList = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    objects = DriverManager() # allows us to call method above

    def __str__(self):
        return self.name 

#Field names from the csv file
# added: NAME,
#need to add: IN,ROUTE,LOG_IN,LOG_OUT,TORH,MILEAGE,PARCEL,LWP,LVP,
#CRT,RL,SUP,FUEL,SUPPORT,VANS,
# 
# Not needed: FDDS,PHR,CALL,POD,CONS,DAILY DPMO 
class ScheduledDatesManager(models.Manager):
    
    def create_scheduledDate(self, route):
        scheduledDate = self.create(route=route)
        return scheduledDate
  

class ScheduledDate(models.Model):
    # have to add this
    objects = ScheduledDatesManager()

    # all fields needed for the daily feeling sheet report 
    date_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, null = True)
    inOff = models.IntegerField("IN", default=1, editable=True, null = True)
    route = models.CharField("Route", max_length = 10, default = "0", null = True)
    logIn_time = models.TimeField("LOG IN", null = True)
    logOut_time = models.TimeField("LOG OUT", null = True)

     #here we don't need the manager to enter the station every time, but if he choose a driver from anotehr station
     # the location should be either auto filled, or manually
    location = models.CharField(max_length = 15, null=True)
    date = models.CharField(max_length = 50, null = True, default= datetime.datetime.now())
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    parcel = models.IntegerField("PARCEL", default=0, editable=True, null = True)

    #the following fields are Extra's report fields 
    LWP = models.IntegerField("LWP", default=0, null = True)
    LVP = models.IntegerField("LVP", default=0,  null = True)
    CRT = models.IntegerField("CRT", default=0, null = True)
    RL = models.IntegerField("RL", default=0, null = True)
    
    #the following fields are money DEDUCTION fields 
    SUP = MoneyField("SUP", default=0, max_digits=10, decimal_places=2, default_currency='GBP', null = True)
    fuel = MoneyField("FUEL", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    supportDeductions = MoneyField("SUPPORT", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    vans = MoneyField("VANS", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

    payroll = ScheduledDatesManager()

    def __str__(self):
        return self.name

    #set default = 1, becasue if the manager has already chose to complete the daily filling sheet
    # that person with default = 1, will work and have data for that day
