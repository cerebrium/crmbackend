from django.contrib.auth.models import User
from .models import Employee, ScheduledDate
from rest_framework import serializers


# a comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 
            'username', 
            'email', 
            'groups',
            'auth_level'
        ]
  
class EmployeeSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Employee
        fields =[
            'employee_id',
            'name',
            'inOff', 
            'location',
            'route',
            'mileage',
            'parcel',
            'LWP',
            'LVP',
            'CRT',
            'RL',
            'SUP',
            'fuel',
            'vans',
            'supportDeductions',
            'documents',
            'datesList',
        ]

class ScheduledDatesSerializer(serializers.HyperlinkedModelSerializer):  
    logIn_time = serializers.TimeField(input_formats= ['%H:%M'])
    logOut_time = serializers.TimeField(input_formats= ['%H:%M'])  
    class Meta:
        model = ScheduledDate
        fields = [
            'date_id',
            'logIn_time',
            'logOut_time',   
            'location',
            'date',
            'employee_id'
        ]


