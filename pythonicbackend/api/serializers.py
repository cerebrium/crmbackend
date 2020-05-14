from django.contrib.auth.models import User
from .models import Driver, ScheduledDate, Images, TrainingDate, Vehicles
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 
            'username', 
            'email', 
            'groups',
            'is_superuser'
        ]
  
class DriverSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Driver
        fields =[
            'driver_id',
            'name',
            'location',
            'email',
            'phone',
            'address',
            'datesList',
            'status',
            'DriverUniqueId',
            'SigningUrlNumber',
            'Signed'
        ]

class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = [
            'Vehicle_id',
            'VehiclesRegistration',
            'VehiclesDVLANumber',
            'VehicleOwned',
            'driver_id'
        ]


       

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = [
            'image_id',
            'ImagesLink',
            'Verified',
            'ImageName',
            'driver_id',
            'ManagerSigned',
            'DriverSigned',
            'ExpiryDate', 
            'SignitureToken',
            'SignitureManagerEmail',
            'Points',
            'NextDVLAScreenshot',
            'LicenseOrigin'
        ]

class ScheduledDatesSerializer(serializers.HyperlinkedModelSerializer):  
    logIn_time = serializers.TimeField(input_formats= ['%H:%M'])
    logOut_time = serializers.TimeField(input_formats= ['%H:%M'])  
    date =  serializers.TimeField(input_formats= ['%Y:%M:%D'])  
    class Meta:
        model = ScheduledDate
        fields = [
            'date_id',
            'name',
            'inOff',
            'route',
            'logIn_time',
            'logOut_time',   
            'location',
            'date',
            'driver_id',
            'mileage',
            'parcel',
            'LWP',
            'LVP',
            'CRT',
            'RL',
            'SUP',
            'fuel',
            'support',
            'vans',
            'deductions'
        ]




class TrainingDateSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = TrainingDate
        fields = [
            'date_id',
            'name',
            'location',
            'date',
            'driver_id',
            'CRT',
            'RL',
            'deductions',
            'support'
        ]


