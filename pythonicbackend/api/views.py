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
    permission_classes = (IsAuthenticated,)    

    def get(self, request):
        ## defining overall data objects
        drivers = Driver.objects.all().order_by('name')
        schedule = ScheduledDate.objects.all()

            # Ginishka ----
            # so cool!! LVP and LWP are different thought, we won't add them
            #LWP means late wave payment and if there is "1" that menas we pay the driver 10 extra pounds

            # LVP means large van payment  "1" that means we pay the driver i think 16 extra pounds
            #for the invoice we will need to sum all the extra reposrt stuff and substract deductions, we have
            #time for that though :*

            # --- end

            # here we want to return the sum of the dedcution fields in shceduleDates
            #     #  that sum will be deducted from the driver payment

        deductionArray = []
        for ele in schedule:
            myLocalVar = str(ele.SUP + ele.fuel + ele.supportDeductions + ele.vans)
            deductionArray.append(myLocalVar)

        #  Here we want to check the number of day a driver has been on training
            #  CRT and RL needs to be 4 for every driver
            # Every driver needs to comlete the trainings before starting to work
            # CRT (classroom) and RL (on the road) training needs to be 4  (2 of each)
            # if the driver has been on RL the managers rights '1' that means he has completed one ride along training for the day
            # same for CRT
            # maybe we can usethis someweher else later, to keep track of the drivers info
        trainingArray = []
        
        for element2 in schedule:
            trainingArray.append(element2.CRT + element2.RL)

        content = {
            'training': trainingArray,
            'deduction_report': deductionArray,

            ### so this is the final object and function in the functions file... this is where its at! :D
            'dates_differences_list': timeDifference(schedule),
            'data': returnOrderdData(drivers, schedule)

        }
        return Response(content)

