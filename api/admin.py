from django.contrib import admin
from .models import Student, Teacher, Media, User
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Media)
admin.site.register(User)


