from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

from home.models import UserProfile

from datetime import datetime
from home.models import contact

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
        contact = contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")

#login

def login_view(request):
    if request.method=='GET':
      return render(request,'login.html')
    if request.method=='POST':
        data=request.POST
        password = data.get('password')
        username = data.get('username')
        x = User.objects.filter(username=username).first()
        print(x)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/user-profile') 
        else:
            return redirect('login') 

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        data=request.POST
        request_data = dict(first_name = data.get('first_name'),
        last_name = data.get('last_name'),
        email = data.get('email'),
        password = make_password(data.get('password')),
        username = data.get('username'))

        user = User.objects.create(**request_data)
        return redirect('home')
   
# User Profile is not working
    
def user_profile(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if profile:
        profile = profile.__dict__
        if profile.get('image'):
            profile['image'] = settings.MEDIA_URL+profile['image']
    else:
        profile={}
    friends = list(Friends.objects.filter(follow=request.user).values_list('following',flat=True))
    friends.append(request.user.id)
    user_posts= UserPost.objects.filter(user__id__in=friends).order_by('-created_at')
    return render(request,'user-timeline.html',context={"profile":profile,'posts':user_posts})
  

