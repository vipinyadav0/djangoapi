
from django.urls import path
from .views import DataTest

urlpatterns = [
    path('v1/data/', DataTest)
]
