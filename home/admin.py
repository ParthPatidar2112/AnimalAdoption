from django.contrib import admin
from home.models import *
from home.models import  user_database

# Register your models here.
# class UserProfile(admin.ModelAdmin):
#     list_display=['user']

# class PetAdmin(admin.ModelAdmin):
#     list_display=['name','species','health','DOB',]

# class AdoptionApplicationAdmin(admin.ModelAdmin):
#     list_display=['application_id','applicant','pet_name','status']

admin.site.register(UserProfile)
admin.site.register(Pet)
admin.site.register(pet_appllication)
admin.site.register(user_database)
admin.site.register(Contact)
