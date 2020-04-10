from django.urls import include, path
from rest_framework import routers
from pythonicbackend.api import views
# from pythonicbackend.api.views import login

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'schedule', views.ScheduleViewSet)

# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
