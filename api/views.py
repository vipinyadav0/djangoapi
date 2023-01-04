from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.views import APIView
from .models import Student
# Create your views here.

class Students(APIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()