from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    

class Car(models.Model):
    car_name=models.CharField(max_length=50)
    speed=models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.car_name 

class Department(models.Model):
    department=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']

class StudentId(models.Model):
    studentId=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.studentId
    
    

class Students(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.SET_NULL, null=True, blank=True)
    studentId=models.OneToOneField(StudentId, related_name='Id', on_delete=models.SET_NULL, null=True, blank=True )
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField(unique=True)
    studentAge = models.IntegerField(default=18)
    studentAddress = models.TextField()
    
    def __str__(self):
        return self.studentName
    
    class Meta:
        ordering = ['studentName']


