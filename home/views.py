from ast import Not
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from email import message

def index(request):
    if(request.user.is_anonymous): 
        return redirect('/signin')
    return render(request, "index.html")

def signin(request):
    if(request.user.is_anonymous == False): 
        return redirect('/')
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if(user is not None):
            login(request, user)
            return redirect('/')
        else: 
            return render(request, 'login.html')
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('/signin')

def update(request):
    id = request.POST.get('id')
    fname = request.POST.get('fname')
    lname =  request.POST.get('lname')
    email = request.POST.get('email')
    u = User.objects.get(id=id)
    u.first_name = fname
    u.last_name = lname
    u.email = email
    u.save()
    messages.success(request, "Profile Updated Successfully")

def profile(request):
    if(request.method == "POST"):
        update(request)
    all_users = User.objects.values()
    data=[]
    concern=-2
    for i in all_users:
        data.append(i)
    for i in range(len(data)):
        if(str(data[i]['username']) == str(request.user)):
            concern=i
    ll=str(data[concern]['last_login'])
    doj=str(data[concern]['date_joined'])
    staff=""
    admin=""
    if(data[concern]['is_staff']==True and data[concern]['is_superuser']==False):
        staff="Yes"
        admin="No"
    elif(data[concern]['is_staff']==True and data[concern]['is_superuser']==True):
        staff="No"
        admin="Yes"
    context = {
        'data':data[concern],
        'fname':data[concern]['first_name'],
        'lname':data[concern]['last_name'],
        'username':data[concern]['username'],
        'email':data[concern]['email'],
        'last_login':ll[0:ll.index(' ')],
        'doj':doj[0:doj.index(' ')],
        'staff':staff,
        'admin':admin,
        'id':data[concern]['id']
        }
    return render(request, "profile.html", context)

def issue(request):
    return render(request, "issue.html")