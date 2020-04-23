from django.contrib.auth.models import User
from .models import Driver, ScheduledDate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, DriverSerializer, ScheduledDatesSerializer
#### import the function from the fil here... can add a comma then the next function if you want
from .functions import timeDifference, returnOrderdData


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 

    queryset = Driver.objects.all().order_by('name')
    serializer_class = DriverSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows drivers to be viewed or edited
    """

    queryset = ScheduledDate.objects.all().order_by('driver_id')

    serializer_class = ScheduledDatesSerializer

class DataViewSet(APIView):
    # permission_classes = (IsAuthenticated,)    

    def get(self, request):
        ## defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()

        #####################################################
        # to Ginishke: check line 71 and 72 of the functions file --> I added your stuff to the overall object so I can just hit one route and get everything

        content = {
            'data': returnOrderdData(drivers, schedule)
        }
        return Response(content)

