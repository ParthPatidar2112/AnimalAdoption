from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import *
from dateutil.relativedelta import relativedelta

# Create your models here.

class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    bio=models.TextField(blank =True,null=True)
    country=models.CharField(max_length=25,blank=True,null =True)
    address=models.TextField(blank=True,null =True)


class Pet(models.Model):
    name=models.TextField(blank =True,null=True)
    photo=models.ImageField(blank=True,null =True)
    location=models.CharField(max_length=25,blank=True,null =True)
    avilability=models.BooleanField(blank=True,null =True,default=False)
    breed=models.TextField(blank =True,null=True)
    DOB=models.DateField(blank =True,null=True)
    health=models.CharField(choices=(('H',("Healthy")),('I',("injure")),('U',("Unhealthy"))),default=1,max_length=1)
    special_needs=models.TextField(blank =True,null=True)
    species=models.TextField(blank =True,null=True)


    def __str__(self):
        return self.name


    
class pet_appllication(models.Model):
    applicant_name=models.TextField(blank =True,null=True)
    email =models.CharField(max_length=122, blank=True,null =True)
    phonenumber =models.IntegerField(blank=True,null =True)
    address=models.TextField(blank=True,null =True)
    desc =models.TextField(max_length=122, blank=True,null =True)
    status=models.CharField(max_length=50,default="1")  # 1(pendding) 2(reject) 0(approve)
 
    def __str__(self):
        return self.applicant_name

class Contact(models.Model):
    

    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    #date = models.DateField()
    def __str__(self):
        return self.name

class user_database(models.Model):

    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    def __str__(self):
        return self.firstname
    