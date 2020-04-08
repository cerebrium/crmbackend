from djmoney.models.fields import MoneyField
import locale
from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from django import forms
from django.utils import timezone
import pytz



#import pytz
#from django.utils.timesince import timesince
# Create your models here.
class Employee(models.Model):
    # all fields needed for the daily feeling sheet report 
    name = models.CharField(max_length = 30, null = True)
    inOff = models.IntegerField(default=1, editable=True, null = True)
    location = models.CharField(max_length = 10, default='DBS2', null = True)
    route = models.CharField(max_length = 10, default = "0", null = True)
    logIn_time = models.TimeField(null = True)
    logOut_time = models.TimeField(null = True)
    mileage = models.IntegerField(default=0, editable=True, null = True)
    parcel = models.IntegerField(default=0, editable=True, null = True)
    LWP = models.IntegerField(default=0, null = True)
    LVP = models.IntegerField(default=0, null = True)
    CRT = models.IntegerField(default=0, null = True)
    RL = models.IntegerField(default=0, null = True)
    SUP = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    #the following fields are money deducion fields
    fuel = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    vans = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    supportDeductions = MoneyField(default=0, max_digits=19, decimal_places=4, default_currency='GBP', null = True)
    #arrayList for storing the the driver has been on the road ()
    datesList =  ArrayField(models.CharField(max_length=10), default=list, null = True)

    def __str__(self):
        return self.name



    #set default = 1, becasue if the manager has already chose to complete the daily filling sheet
    # that person with default = 1, will work and have data for that day

   # models.DateTimeField()
    

    #dateTime 
    #dt_now = datetime.now()
    #dt_0 = timedelta.fields.TimedeltaField()
    #logIn = forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    #logOut = forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    #logOut = models.DateTimeField()
    
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
