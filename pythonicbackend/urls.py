from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from pythonicbackend.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'schedule', views.ScheduleViewSet)

# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls), name='rest routes'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('hello/', views.CoolViewSet.as_view(), name='hello')
]
