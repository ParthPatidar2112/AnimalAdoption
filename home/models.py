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

class AdoptionApplication(models.Model):
    application_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    pet_name=models.ForeignKey(Pet,on_delete=models.CASCADE,related_name='Pet_name')
    data=models.TextField(blank =True,null=True)
    status=models.CharField(choices=(('A',("Accepted")),('P',("Pending")),('D',("Decline"))),default="P",max_length=1)

class contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
