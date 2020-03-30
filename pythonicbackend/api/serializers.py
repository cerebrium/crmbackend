from django.contrib.auth.models import User, Group
from .models import Employee
from rest_framework import serializers

# a comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 
            'username', 
            'email', 
            'groups'
        ]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
             'name',
             'age'
        ]       
  
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'name',
            'email',
            'location',
            'milesDriven'
        ]
