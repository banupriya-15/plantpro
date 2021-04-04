from django.urls import path
from .views import home, scan, remedy, status

urlpatterns = [
    path('', home, name="home"),
    path('scan', scan, name="scan"),
    path('remedy', remedy, name="remedy"),
    path('status', status, name="status")
]
