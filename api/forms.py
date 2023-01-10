from django import forms
from .models import Student, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fielsd = "__all__"
    
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fielsd = "__all__"