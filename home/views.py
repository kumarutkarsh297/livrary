from ast import Not
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login

def index(request):
    if(request.user.is_anonymous): 
        return redirect('/signin')
    return render(request, "index.html")

def signin(request):
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

def profile(request):
    all_users = User.objects.values()
    data=[]
    concern=-2
    for i in all_users:
        data.append(i)
    for i in range(len(data)):
        if(str(data[i]['username']) == str(request.user)):
            concern=i
    context = {
        'hello':data[concern]
    }
    return render(request, "profile.html", context)
