from django.contrib.auth.models import User
from .models import Driver, ScheduledDate, Images
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
            'datesList'
        ]

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = [
            'image_id'
            'ImagesLink',
            'Verified',
            'ImageName',
            'driver_id'       
        ]

class ScheduledDatesSerializer(serializers.HyperlinkedModelSerializer):  
    logIn_time = serializers.TimeField(input_formats= ['%H:%M'])
    logOut_time = serializers.TimeField(input_formats= ['%H:%M'])  
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
            'vans'
        ]


