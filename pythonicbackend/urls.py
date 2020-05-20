from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from pythonicbackend.api import views

router = routers.DefaultRouter()
router.register(r'managers', views.managersViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'schedule', views.ScheduleViewSet)
router.register(r'images', views.ImagesViewSet)
router.register(r'vehicles', views.VehiclesViewSet)
router.register(r'trainingdate', views.TrainingViewSet)
router.register(r'invoices', views.InvoicesViewSet)


# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls), name='rest routes'),
    path('asdjflkasj24dflasd43fhapsdjnfkqjwne2r2oqwiefkasjd43nfkjl4nwe31ofiqwefkjan51dmfnqoweifqk123wjenfaskjdnfasdf/', obtain_auth_token),
    path('data/', views.DataViewSet.as_view(), name='data'),
    path('invoice/', views.InvoiceViewSet.as_view(), name='invoice'),
    path('statistics/', views.StatisticsViewSet.as_view(), name='stats'),
    path('csv/', views.MapViewSet.as_view(), name='csv')
]
