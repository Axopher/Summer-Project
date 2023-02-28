from itertools import product
from operator import truediv
from tkinter.tix import Tree
from django.db import models
import uuid
from adminpanel.models import Course

# Create your models here.

class Product(models.Model):
    course = models.OneToOneField(Course,null=True,blank=True,on_delete=models.DO_NOTHING)
    productName = models.CharField(max_length=200,null=True,blank=True)
    teacherName = models.CharField(max_length=200,null=True,blank=True)
    productPrice = models.PositiveIntegerField(null=True,blank=True)
    duration= models.PositiveIntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    featured_image = models.ImageField(null=True,blank=True,upload_to="products/",default="products/default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.course)

class Order(models.Model):
    product = models.ForeignKey(Product,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)
    sname = models.CharField(max_length=200,null=True,blank=True)
    sphone = models.PositiveIntegerField(null=True,blank=True)
    semail = models.EmailField(null=True,blank=True)
    saddress = models.CharField(max_length=200,null=True,blank=True)
    sgender = models.CharField(max_length=10,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.product.productName

    class Meta:
        ordering = ['-created']    


