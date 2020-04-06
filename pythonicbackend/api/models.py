from djmoney.models.fields import MoneyField
import locale
from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
#import pytz
#from django.utils.timesince import timesince




# Create your models here.
class Employee(models.Model):
    # all fields needed for the daily feeling sheet report 
    name = models.CharField(max_length = 30)

    #set default = 1, becasue if the manager has already chose to complete the daily filling sheet
    # that person with default = 1, will work and have data for that day
    inOff = models.IntegerField(default=1, editable=True)
    station = models.CharField(max_length = 30)
    route = models.CharField(max_length = 10)

    #dateTime 
    #dt_now = datetime.now()
    logIn = models.TimeField(default = None)

    #logIn2 = datetime.strptime(logIn,'%H:%M')
    logOut = models.TimeField(default = None)

    # TORH = (logOut - logIn)
    mileage = models.IntegerField(default=0, editable=True)
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
