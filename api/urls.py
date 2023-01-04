
from django.urls import path
from .views import Students

urlpatterns = [
    path('v1/srudents/', Students.as_view())
]
