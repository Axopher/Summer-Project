from django.db import models
from django.contrib.auth.models import User

# from adminpanel.models import Course

from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=200,blank=True,null=True)
    fullname = models.CharField(max_length=200,blank=True,null=True)
    # ppsize = models.ImageField(null=True,blank=True,upload_to='profiles/',default)
    phone = models.IntegerField()
    email = models.EmailField(max_length=500,blank=True,null=True)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.username
        
# def userCreated(sender,instance,created,**kwargs):
#     print('User created')        





