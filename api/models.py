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

class Media(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    file = models.FileField(upload_to='upload/', blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Medias'

class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=20, null=False, blank=False)
    familyName = models.CharField(max_length=20, null=False, blank=False)
    givenName = models.CharField(max_length=20, null=False, blank=False)
    googleId = models.IntegerField(null=True, blank=True)
    imageUrl = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    