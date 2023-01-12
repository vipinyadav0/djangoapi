from rest_framework import serializers
from .models import Student, Teacher, Media, User
import base64
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    
class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

# class FileSerializer(serializers.ModelSerializer):
#     file_obj = serializers.SerializerMethodField()
#     file_url = serializers.SerializerMethodField()
#     file_base64 = serializers.SerializerMethodField()
#     class Meta:
#         model = Media
#         fields = ('id', 'file_obj', 'file_url', 'file_base64')

#     def get_file_obj(self, obj):
#         return obj.file

#     def get_file_url(self, obj):
#         request = self.context.get('request')
#         file_url = obj.file.url
#         return request.build_absolute_uri(file_url)
#     def get_file_base64(self, obj):
#         with open(obj.file.path, 'rb') as f:
#             file_base64 = base64.b64encode(f.read()).decode()
#         return file_base64

class MediaSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    class Meta:
        model = Media
        fields = ('id','user','file_url')

    def get_file_url(self, obj):
        request = self.context.get('request')
        file_url = obj.file.url
        return request.build_absolute_uri(file_url)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"