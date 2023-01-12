from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    school = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Students'
    

class Teacher(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    subject = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Teachers'

class File(models.Model):
    file = models.FileField(upload_to='upload/')

    class Meta:
        verbose_name_plural = 'Files'
