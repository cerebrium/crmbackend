from django.contrib.auth.models import User
from .models import Driver, ScheduledDate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, DriverSerializer, ScheduledDatesSerializer
#### import the function from the fil here... can add a comma then the next function if you want
from .functions import timeDifference


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class DriverViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,) 

    queryset = Driver.objects.all().order_by('name')
    serializer_class = DriverSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows drivers to be viewed or edited
    """
    queryset = ScheduledDate.objects.all().order_by('driver_id')
    serializer_class = ScheduledDatesSerializer

class DataViewSet(APIView):
    # permission_classes = (IsAuthenticated,)    

    def get(self, request):
        ############# examples of writing functions here #############
        # First returned array
        # grab all of the objects stored in the drivers class
        drivers = Driver.objects.all().order_by('name')

        # make data type to store stuff in -- array in this case
        myDriverArray = []

        # loop through each object in the data class (drivers) and grab the data i want... push it into the array for display
        for name in drivers:
            myDriverArray.append(name.name)

        #######################################################################################################################################    
        # Second returned array

        # grab all of the objects stored in the schedule class
        schedule = ScheduledDate.objects.all().order_by('driver_id')
        
        # make another array to store the dates data i want
        myScheduleArray = []

        # Loop through each object in this array and do some math on it, push the value to the array for display
        for dateObject in schedule:
            myScheduleArray.append(dateObject.LWP + dateObject.LVP)


        ############### example of importing functions from functions file .... much cleaner and the 'proper' way to do this ....
        # step 1: at the top import the name of the function from the file where the function lives
        ## call the function... but dont forget to pass into the function whatever data you want it to act on
        ## store the contents of the function in the object below
        
        content = {
            'drivers_names': myDriverArray,
            'LWP_and_LVP': myScheduleArray,
            ### so this is all we need to actually do to call the function here and store it.... much cleaner!
            'dates_differences_list': timeDifference(schedule)
        }
        return Response(content)

