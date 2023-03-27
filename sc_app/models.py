from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Student_Register(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_no = models.IntegerField()
    college_name= models.CharField(max_length=100)
    mobile = models.CharField(max_length=10,unique=True)

class Complaint(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    complaint= models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True,blank=True)

class Notification(models.Model):
    notifications= models.TextField()
    date = models.DateField(auto_now=True)


