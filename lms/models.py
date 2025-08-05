from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', null=True)
    desc = models.CharField(verbose_name='Desc', null=True)
    image = models.ImageField(upload_to='course/', verbose_name='Course picture', null=True)



class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', null=True)
    desc = models.CharField(verbose_name='Desc', null=True)
    url = models.CharField(verbose_name='Video url', null=True)
    image = models.ImageField(upload_to='course/', verbose_name='Lesson picture', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course', null=True)
