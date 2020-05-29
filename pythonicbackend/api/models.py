from djmoney.models.fields import MoneyField
import locale
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from django import forms
from django.utils import timezone
import pytz

class managers(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    email = models.CharField(max_length = 100, unique=True)
    name = models.CharField(max_length = 100, null = True)
    station = models.CharField(max_length = 20, null = True)
    creationDate = models.CharField(max_length = 50, default = datetime.date.today())

# Create your models here.
class DriverManager(models.Manager):
    def create_driver(self, name):
        driver = self.create(name=name)

        return driver
        
#----rename it to Driver(models.model)
class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True, unique=True) #need to connect to DA Compliance Check
    vehicle_name = models.CharField(max_length=50, null = True)

    #the following fields will be displayed when a manager clicks on "Add Driver"
    name = models.CharField(max_length = 100, null = True)
    location = models.CharField(max_length = 15, default = 'DBS2', null = True) #want to change to depot
    email = models.CharField(max_length = 50, null=True)
    phone = models.CharField(max_length = 20, null=True)
    address = models.CharField(max_length=100, null=True)
    datesList = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    status = models.CharField(max_length = 30, null = True)
    DriverUniqueId = models.CharField(max_length = 30, null=True)
    SigningUrlNumber = models.CharField(max_length = 100, null=True)
    Signed = models.BooleanField(default=False)

    objects = DriverManager() # allows us to call method above
    #week = models.DateField("week", default = datetime.date.today.isocalendar()[1])
    
    def __str__(self):
        return self.name 

# Create your models here.
class InvoiceManager(models.Manager):
    def create_Invoice(self, driver_id, day, routeType, LWP, LVP, SUP, deductions, fuel):
        invoice = self.create(
            driver_id = driver_id,
            day = day,
            routeType =routeType, 
            LWP = LWP,
            LVP = LVP,
            SUP = SUP, 
            deductions = deductions,
            fuel = fuel
            )

        return invoice

class Invoice(models.Model):
    name = models.CharField(max_length = 100, null = True)
    invoice_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length = 50, null = True, default = datetime.date.today())
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    day = models.CharField(max_length = 50, null = True)
    routeType = models.CharField(max_length = 10, null = True)
    LWP = models.IntegerField("LWP", default=0, null = True)
    LVP = models.IntegerField("LVP", default=0,  null = True)
    SUP = MoneyField("SUP", default=0, max_digits=10, decimal_places=2, default_currency='GBP', null = True)
    deductions = MoneyField("Deductions", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    fuel = MoneyField("FUEL", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

    def __str__(self):
        return self.name

class Vehicles(models.Model):
    driver_id = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    vehicle_id = models.AutoField(primary_key=True)
    registration = models.CharField(max_length=20, null=True)
    make = models.CharField(max_length=30, null=True)
    model = models.CharField(max_length=30, null=True)
    year = models.CharField(max_length=10, null=True)
    companyOwned = models.BooleanField(default=False)
    vtype = models.CharField(max_length=20, default='standard')
    quotePrice = MoneyField("RENTAL QUOTE", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    invoice = MoneyField("INVOICE", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)

class VehicleDamages(models.Model):
    VehicleDamages_id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    statmentOfDamage = models.CharField(max_length = 500, null=True)
    dateOfIncident = models.CharField(max_length = 100, null=True)

# DA compliance check
class Images(models.Model):
    driver_id = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicles, blank=True, null=True, on_delete=models.CASCADE)
    image_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, null = True)
    countryOfIssue = models.CharField(max_length = 30, null=True)
    expiryDate = models.CharField(max_length = 100, null = True)
    dueDate = models.CharField(max_length = 50, null = True)
    datePassed = models.CharField(max_length=30, null=True)
    photo = models.CharField(max_length=15, null=True)
    managerApprovedName = models.CharField(max_length = 30, null=True)
    managerApprovedDate = models.CharField(max_length = 90, null=True)
    imagesLink = models.CharField(max_length=150, null=True)
    verified = models.BooleanField(default=False)
    driverSigned = models.BooleanField(default=False)
    points = models.IntegerField(default = 0, null = True)
    nextDVLAScreenshot = models.CharField(max_length = 50, null = True)
 
    def __str__(self):
        return self.name 

class ScheduledDatesManager(models.Manager):
    
    def create_date(self, NAME, IN, ROUTE, LOGIN, LOGOUT, TORH, MILEAGE, PARCEL, LWP, LVP, CRT, RL, SUP, FUEL, deductions, date, driver_id):
        date = self.create(
            name=NAME,
            inOff=IN,
            route=ROUTE,
            logIn_time=LOGIN,
            logOut_time=LOGOUT,
            TORH=TORH,
            mileage=MILEAGE,
            parcel=PARCEL,
            LateWavePayment=LWP,
            LVP=LVP,
            CRT=CRT,
            RL=RL,
            support=SUP,
            fuel=FUEL,
            deductions=deductions,
            date=date,
            driver_id=Driver(driver_id),
        )

        return date
  

class ScheduledDate(models.Model):
    # have to add this
    objects = ScheduledDatesManager()

    # all fields needed for the daily feeling sheet report 
    date_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length = 50, null = True)
    inOff = models.IntegerField("IN", default=1, editable=True, null = True)
    route = models.CharField("Route", max_length = 30, default = "0", null = True)
    routeNumber = models.CharField("Route", max_length = 30, default = "0", null = True)
    logOut_time = models.TimeField("LOG OUT", null = True)
    logIn_time = models.TimeField("LOG IN", null = True)

     #here we don't need the manager to enter the station every time, but if he choose a driver from anotehr station
     # the location should be either auto filled, or manually
    location = models.CharField(max_length = 15, default='DBS2', null=True)
    date = models.CharField(max_length = 50, null = True, default = datetime.date.today())
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    start_mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    finish_mileage = models.IntegerField("MILEAGE", default=0, editable=True, null = True)
    parcel = models.IntegerField("PARCEL", default=0, editable=True, null = True)
    parcelNotDelivered = models.IntegerField("PARCEL NOT DELIVERED", default=0, editable=True, null = True)

    #the following fields are Extra's report fields 
    TORH = models.TimeField("TORH", null = True)
    LateWavePayment = models.IntegerField("LWP", default=0, null = True)
    LVP = models.IntegerField("LVP", default=0,  null = True)
    CRT = models.IntegerField("CRT", default=0, null = True)
    RL = models.IntegerField("RL", default=0, null = True)
    FDDS = models.FloatField("FDDS", default=0, null = True)
    PHR = models.FloatField("PHR", default=0, null = True)
    CALL = models.FloatField("CALL", default=0, null = True)
    POD = models.FloatField("POD", default=0, null = True)
    CONS = models.FloatField("FDDS", default=0, null = True)
    DPMO = models.FloatField("DPMO", default=0, null = True)

    #the following fields are money DEDUCTION fields 
    fuel = MoneyField("FUEL", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    support = MoneyField("SUPPORT", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    vans = MoneyField("VANS", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    deductions = MoneyField("Deductions", default=0, max_digits=19, decimal_places=2, default_currency='GBP', null = True)
    objects = ScheduledDatesManager()

    def __str__(self):
        return self.name
        