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
class DriverManager(models.Manager):
    def create_driver(self, name):
        driver = self.create(name=name)

        return driver
    

#----rename it to Driver(models.model)
class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, null = True)
    location = models.CharField(max_length = 15, default = 'DBS2', null = True)
    datesList = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    status = models.CharField(max_length = 30, null = True)
    onboarding = models.IntegerField("Onboarding", default=0, null=True)
    phone = models.CharField(max_length = 20, null=True)
    email = models.CharField(max_length = 50, null=True)
    DandATest = models.BooleanField(default=False)
    DriverUniqueId = models.CharField(max_length = 30, null=True)
    Badge = models.BooleanField(default=False)
    BadgeNumber = models.CharField(max_length=15, null=True)
    Active = models.BooleanField(default=False)
    VanEConfirmed = models.BooleanField(default=False)
    NINNumber = models.CharField(max_length=15, null=True)
    UTRNumber = models.CharField(max_length=20, null=True)
    VatNumber = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)

    objects = DriverManager() # allows us to call method above
    #week = models.DateField("week", default = datetime.date.today.isocalendar()[1])
    
    def __str__(self):
        return self.name 

class Vehicles(models.Model):
    Vehicle_id = models.AutoField(primary_key=True)
    VehiclesRegistration = models.CharField(max_length=20, null=True)
    VehiclesDVLANumber = models.CharField(max_length=40, null=True)
    VehicleOwned = models.BooleanField(default=False)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    ImagesLink = models.CharField(max_length=150, null=True)
    Verified = models.BooleanField(default=False)
    ManagerSigned = models.BooleanField(default=False)
    DriverSigned = models.BooleanField(default=False)
    ExpiryDate = models.CharField(max_length = 50, null = True, default= datetime.datetime.now())
    SignitureToken = models.CharField(max_length = 1000, null = True)
    SignitureManagerEmail = models.CharField(max_length = 100, null = True)
    ImageName = models.CharField(max_length=20, null=True)
    Points = models.IntegerField(default = 0, null = True)
    NextDVLAScreenshot = models.CharField(max_length = 50, null = True, default= datetime.datetime.now())
    LicenseOrigin = models.CharField(max_length = 15, null=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name 

class ScheduledDatesManager(models.Manager):
    
    def create_date(self, name, inOff, route, logIn_time, logOut_time, TORH, mileage, parcel, LWP, LVP, CRT, RL, SUP, fuel, support, vans, deductions, PHR, CALL, POD, CONS, driver_id):
        date = self.create(
            name=name,
            inOff=inOff,
            route=route,
            logIn_time=logIn_time,
            logOut_time=logOut_time,
            TORH=TORH,
            mileage=mileage,
            parcel=parcel,
            LWP=LWP,
            LVP=LVP,
            CRT=CRT,
            RL=RL,
            SUP=SUP,
            fuel=fuel,
            support=support,
            vans=vans,
            deductions=deductions, 
            PHR=PHR,
            CALL=CALL,
            POD=POD,
            CONS=CONS,
            driver_id=Driver(driver_id),
            location='DBS2'
        )

        return date
  

class ScheduledDate(models.Model):
    # have to add this
    objects = ScheduledDatesManager()

    # all fields needed for the daily feeling sheet report 
    date_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, null = True)
    inOff = models.IntegerField("IN", default=1, editable=True, null = True)
    route = models.CharField("Route", max_length = 10, default = "0", null = True)
    logOut_time = models.TimeField("LOG OUT", null = True)
    logIn_time = models.TimeField("LOG IN", null = True)

     #here we don't need the manager to enter the station every time, but if he choose a driver from anotehr station
     # the location should be either auto filled, or manually
    location = models.CharField(max_length = 15, default='DBS2', null=True)
    date = models.CharField(max_length = 50, null = True, default= datetime.datetime.now())
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    parcel = models.IntegerField("PARCEL", default=0, editable=True, null = True)

    #the following fields are Extra's report fields 
    TORH = models.TimeField("TORH", null = True)
    LWP = models.IntegerField("LWP", default=0, null = True)
    LVP = models.IntegerField("LVP", default=0,  null = True)
    CRT = models.IntegerField("CRT", default=0, null = True)
    RL = models.IntegerField("RL", default=0, null = True)
    FDDS = models.FloatField("FDDS", default=0, null = True)
    PHR = models.FloatField("PHR", default=0, null = True)
    CALL = models.FloatField("CALL", default=0, null = True)
    POD = models.FloatField("POD", default=0, null = True)
    CONS = models.FloatField("FDDS", default=0, null = True)
    DPMO = models.FloatField("DPMO", default=0, null = True)
    SUP = MoneyField("SUP", default=0, max_digits=10, decimal_places=2, default_currency='GBP', null = True)

    
    #the following fields are money DEDUCTION fields 
    fuel = MoneyField("FUEL", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    support = MoneyField("SUPPORT", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    vans = MoneyField("VANS", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

    deductions = MoneyField("Deductions", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

    objects = ScheduledDatesManager()

    def __str__(self):
        return self.name

    #set default = 1, becasue if the manager has already chose to complete the daily filling sheet
    # that person with default = 1, will work and have data for that day



    #here i want to create a class that will get just the training if there are any
    #then I plan to use it in fucntions to check if there are trainings
class TrainingDate(models.Model):

    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, null = True)
    support = MoneyField("SUPPORT", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    location = models.CharField(max_length = 15, default='DBS2', null=True)
    CRT = models.IntegerField("CRT", default=0, null = True)
    RL = models.IntegerField("RL", default=0, null = True)
    deductions = MoneyField("Deductions", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    date = models.CharField(max_length = 50, null = True, default= datetime.datetime.now())

    objects = ScheduledDatesManager()

    def __str__(self):
        return self.name

