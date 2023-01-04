
from django.urls import path, include
from .views import Students
from rest_framework import routers

router = routers.SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('v1/students/', Students.as_view())
]
