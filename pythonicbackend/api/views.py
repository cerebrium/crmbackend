from django.contrib.auth.models import User, Group
from .models import Employee
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, EmployeeSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# class EmployeeView(mixins.Create):    
#     """
#     API endpoint that allows employees to be edited
#     """
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()
