from django.contrib.auth.models import User
from .models import Driver, ScheduledDate, DriverManager,ScheduledDatesManager
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, DriverSerializer, ScheduledDatesSerializer
#### import the function from the fil here... can add a comma then the next function if you want
from .functions import timeDifference, returnOrderdData
from .test_data import importData
import csv,io 


class UserViewSet(viewsets.ModelViewSet):
    # Authentication
    # permission_classes = (IsAuthenticated,)

    # Users
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class DriverViewSet(viewsets.ModelViewSet):
    # Authentication
    # permission_classes = (IsAuthenticated,) 

    # drivers
    queryset = Driver.objects.all().order_by('name')
    serializer_class = DriverSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    # Authentication
    # permission_classes = (IsAuthenticated,)

    # schedule
    queryset = ScheduledDate.objects.all().order_by('driver_id')
    serializer_class = ScheduledDatesSerializer

class DataViewSet(APIView):
    # Authentication
    # permission_classes = (IsAuthenticated,)    

    # function for all data
    def get(self, request):
        ## defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()

        content = {
            'data': returnOrderdData(drivers, schedule)
        }
        return Response(content)

class MapViewSet(APIView):
    # Authentication
    # permission_classes = (IsAuthenticated,)  
    # This route is just a route that allows us to call the function in the test_data.py file with the correct environment  

    # function for all data
    def get(self, request):
        content = {
            'data': importData(ScheduledDate, Driver, DriverManager, ScheduledDatesManager) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

