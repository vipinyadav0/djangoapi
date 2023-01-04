from django.shortcuts import render, get_object_or_404
from .serializers import StudentSerializer, TeachersSerializer
from rest_framework.generics import GenericAPIView, ListAPIView
from .models import Student, Teacher
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class Students(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentViewSets(viewsets.ViewSet):
    """
    A simple viewsets for listing or retrieving teachers.
    """

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        teacher = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(teacher)
        return Response(serializer.data)

class TeacherViewSets(viewsets.ViewSet):
    """
    A simple viewsets for listing or retrieving teachers.
    """

    def list(self, request):
        queryset = Teacher.objects.all()
        serializer = TeachersSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Teacher.objects.all()
        teacher = get_object_or_404(queryset, pk=pk)
        serializer = TeachersSerializer(teacher)
        return Response(serializer.data)
