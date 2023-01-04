from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView, ListAPIView
from .models import Student
# Create your views here.

class Students(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()