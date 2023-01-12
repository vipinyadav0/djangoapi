
from django.urls import path, include
from .views import Students, TeacherViewSets, StudentViewSets, StudentsList, StudentDetail, MediaListView, MediaViewSets
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSets, basename='teacher')
router.register(r'students', StudentViewSets, basename='students')
router.register(r'media', MediaViewSets, basename='media')

# router.register(r'files', FileViewSets, basename='files')



urlpatterns = [
    path('', include(router.urls)),
    path('all-students/', Students.as_view()),
    path('list-students/', StudentsList.as_view()),
    path('list-students/<int:pk>/', StudentDetail.as_view()),
    path('media/', MediaListView.as_view())
]

