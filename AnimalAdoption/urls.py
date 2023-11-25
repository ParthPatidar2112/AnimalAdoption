from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Paws Shelter Admin"
admin.site.site_title = "Paws Shelter Admin Portal"
admin.site.index_title = "Welcome to Paws Shelter"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
    
 ]
