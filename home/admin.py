from django.contrib import admin
from home.models import contact

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user']

class PetAdmin(admin.ModelAdmin):
    list_display=['name','species','health','DOB',]

class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display=['application_id','applicant','pet_name','status']

admin.site.register(UserProfileAdmin)
admin.site.register(PetAdmin)
admin.site.register(AdoptionApplicationAdmin)

admin.site.register(contact)