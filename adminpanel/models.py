from operator import truediv
from tokenize import blank_re
from users.models import Profile
from django.db import models
import uuid
from django.contrib.auth.models import User
from PIL import Image
# from django.contrib.auth.models import User

# Create your models here.




class Teacher(models.Model):
    TNum = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    TName = models.CharField(max_length=100)
    TAddress = models.CharField(max_length=100)
    TEmail = models.EmailField()
    TDob = models.DateField()
    TPhone = models.PositiveIntegerField()
    graduation_type = (
        ('Under Graduate','Under Graduate'),
        ('Post Graduate','Post Graduate'),
        ('PhD','PhD')
    )
    TQualification = models.CharField(max_length=16,choices=graduation_type,default='Under Graduate')
    gender_type = (
        ('male','male'),
        ('female','female'),
        ('others','others')
    )
    TGender = models.CharField(max_length=6,choices=gender_type,default='male') 
    created = models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.TName

class Course(models.Model):
    CNum = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    CName = models.CharField(max_length=100)
    CTName = models.ManyToManyField(Teacher)
    CPrice=models.PositiveIntegerField()
    CDuration=models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.CName     


class Student(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    StNum = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    StName = models.CharField(max_length=100)
    StImage = models.ImageField(null=True,blank=True,default="avatar.jpg")
    StPhone = models.PositiveIntegerField()
    StEmail = models.EmailField()
    StAddress = models.CharField(max_length=100)
    StDob = models.DateField()
    StCName = models.ManyToManyField(Course)
    gender_type = (
        ('male','male'),
        ('female','female'),
        ('others','others')
    )
    StGender = models.CharField(max_length=6,choices=gender_type,default='male') 
    StRemarks = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    
    def __str__(self):
        return self.StName


 
class Fee(models.Model):
    FNum = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    FStudName = models.OneToOneField(Student,on_delete=models.PROTECT,null=True)
    FCourseName = models.ManyToManyField(Course)
    FDate=models.DateTimeField(auto_now_add=True)
    FAmount=models.PositiveIntegerField()
    Admission=models.PositiveIntegerField(default=2000)
    Refundable_Deposit=models.PositiveIntegerField(default=3000)

    class Meta:
        db_table = 'fee'
        ordering = ['-FDate']

    def __str__(self):
        return str(self.FStudName)


