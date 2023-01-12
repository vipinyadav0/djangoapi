from rest_framework import serializers
from .models import Student, Teacher, File

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    
class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"