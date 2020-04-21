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

#----rename it to Driver(models.model)
class Driver(models.Model):
    name = models.CharField(max_length = 50, null = True)
    driver_id = models.AutoField(primary_key=True)
    documents = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    datesList = ArrayField(models.CharField(max_length=20), default=list, blank=True)

    

#------- The following fields are moved in the ScheduleDate class

    # route = models.CharField(max_length = 10, default = "0", null = True)
    # mileage = models.IntegerField(default=0, editable=True, null = True)
    # parcel = models.IntegerField(default=0, editable=True, null = True)
    # LWP = models.IntegerField(default=0, null = True)
    # LVP = models.DecimalField(default=0, decimal_places=10, max_digits=15,  null = True)
    # CRT = models.DecimalField(default=0, decimal_places=10, max_digits=15, null = True)
    # RL = models.IntegerField(default=0, null = True)
    # SUP = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    # #the following fields are money deducion fields
    # fuel = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    # vans = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    # supportDeductions = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    # documents = ArrayField(models.CharField(max_length=100), default=list, blank=True)
    # datesList = ArrayField(models.CharField(max_length=20), default=list, blank=True)

    def __str__(self):
        return self.name


class ScheduledDate(models.Model):
    # all fields needed for the daily feeling sheet report 
    date_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, null = True)
    inOff = models.IntegerField("IN", default=1, editable=True, null = True)

    # ---????? ----route type should be a drop down menu? 
    route = models.CharField("Route", max_length = 10, default = "0", null = True)
    logIn_time = models.TimeField("LOG IN", null = True)
    logOut_time = models.TimeField("LOG OUT", null = True)
    #location = models.CharField(max_length = 10, default='DBS2', null = True)

     #here we don't need the manager to enter the station every time, but if he choose a driver from anotehr station
     # the location should be either auto filled, or manually
    location = models.CharField(max_length = 100, null=True)
    date = models.DateField(max_length = 50, null = True, default = datetime.date.today)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)

    
    mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    parcel = models.IntegerField("PARCEL", default=0, editable=True, null = True)

    #the following fields are Extra's report fields 
    LWP = models.IntegerField("LWP", default=0, null = True)
    LVP = models.IntegerField("LVP", default=0,  null = True)
    CRT = models.IntegerField("CRT", default=0, null = True)
    RL = models.IntegerField("RL", default=0, null = True)
    SUP = MoneyField("SUP", default=0, max_digits=10, decimal_places=2, default_currency='GBP', null = True)
    
    #the following fields are money DEDUCTION fields 
    fuel = MoneyField("FUEL", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    supportDeductions = MoneyField("SUPPORT", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    vans = MoneyField("VANS", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    


    def __str__(self):
        return self.name



    #set default = 1, becasue if the manager has already chose to complete the daily filling sheet
    # that person with default = 1, will work and have data for that day

 
    

    # TORH = (logOut - logIn)

#-%%% ------------------
    #  def hours(self):
    #      c = self.logOut - self.logIn
    #      print(c.seconds)    
    
    
    #deductions
    # TORH = models.DateTimeField()

    
    # @property
    # def TORH(myVar, yourVar):
    #     return myVar, yourVar



    # @property
    # def SUP_display(self):
    #     return "$%s" % self.SUP






#     a = '2200'
# b = '1800'
# time1 = datetime.strptime(a,"%H%M") # convert string to time
# time2 = datetime.strptime(b,"%H%M") 
# diff = time1 -time2
# diff.total_seconds()/3600 
