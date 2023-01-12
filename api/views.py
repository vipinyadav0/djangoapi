from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets, mixins, decorators
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Teacher, Media
from .serializers import StudentSerializer, TeachersSerializer, MediaSerializer

# Create your views here.

class Students(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentsList(APIView):
    def get(self, request):
        students =  Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    """Retrieve, Update, Delete a student instance

    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentViewSets(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple viewsets for listing or retrieving teachers.
    """

    # def list(self, request):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     queryset = Student.objects.all()
    #     teacher = get_object_or_404(queryset, pk=pk)
    #     serializer = StudentSerializer(teacher)
    #     return Response(serializer.data)

class TeacherViewSets(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.DestroyModelMixin):
    """
    A simple viewsets for listing or retrieving teachers.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer

# class FileViewSets(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.DestroyModelMixin):
#     queryset = Media.objects.all()
#     serializer_class = FileSerializer

class MediaListView(ListAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    
class MediaViewSets(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.DestroyModelMixin):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()

    
