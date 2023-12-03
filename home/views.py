from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

from home.models import UserProfile

from datetime import datetime
from home.models import *

# Create your views here.
def index(request):
    context = {
        "variable1":"this is sent through views.url",
        "variable2":"thisrl"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")    

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")

#application

def application(request):
    if request.method == "POST":
        applicant_name=request.POST.get("name")
        email=request.POST.get("email")
        phonenumber=request.POST.get("phonenumber")
        address=request.POST.get("address")
        desc=request.POST.get("desc")
        status = request.POST.get("status", default="1")
        data=pet_appllication(applicant_name=applicant_name, email=email, phonenumber=phonenumber,address=address,desc=desc,status=status)
        data.save( )

        return redirect('home')
    
    return render(request, 'application.html')

#login

def login_view(request):
    # if request.method=='GET':
    #   return render(request,'login.html')
    # if request.method=='POST':
    #     data=request.POST
    #     password = data.get('password')
    #     username = data.get('username')
    #     x = User.objects.filter(username=username).first()
    #     print(x)
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request,user)
    #         return redirect('/user-profile') 
    #     else:
    b = user_database.objects.all().values()
    global usertype
    global num
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        i = 0
        j = 0
        for i in range(len(b)):

            if (b[i]['username'] == username and b[i]['password'] == password):
                #   user=login(email=email, password=password)
                #   user.save()
                num = 1

                i = i+1
                return redirect("home")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        # data=request.POST
        # request_data = dict(first_name = data.get('first_name'),
        # last_name = data.get('last_name'),
        # email = data.get('email'),
        # password = make_password(data.get('password')),
        # username = data.get('username'))

        # user = User.objects.create(**request_data)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        data = user_database(firstname = first_name, lastname = last_name, email = email, password = password, username = username)
        data.save()
        
        return redirect('home')
   
# User Profile is not working
    
def user_profile(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if profile:
        profile = profile.__dict__
        if profile.get('image'):
            profile['image'] = settings.MEDIA_URL+profile['image']
    # else:
    #     profile={}
    # friends = list(Friends.objects.filter(follow=request.user).values_list('following',flat=True))
    # friends.append(request.user.id)
    # user_posts= UserPost.objects.filter(user__id__in=friends).order_by('-created_at')
    # return render(request,'user-timeline.html',context={"profile":profile,'posts':user_posts})
  

