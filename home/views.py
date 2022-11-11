from ast import Not
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Books
from home.models import Members
from home.models import Rates
from home.models import Issued
from home.models import Late
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from email import message
import random
from datetime import date as date_n

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

def flush(request):
    isbn = request.POST.get('isbn')
    bookname = request.POST.get('bookname')
    cname = request.POST.get('cname')
    fromd = request.POST.get('from')
    tod = request.POST.get('to')
    charge = request.POST.get('charge')
    ref = str(chr(random.randint(97,122))+str(random.randint(1,7))+str(random.randint(5,9))+chr(random.randint(100,118)))
    issued = Issued(ref = ref, isbn = isbn, bookname = bookname, customername = cname, from_date = fromd, to_date = tod, charge = charge, returned = False)
    issued.save()
    messages.success(request, "Book Issued Ref. No : "+ref)

def issue(request):
    if(request.method == "POST"):
        flush(request)
    d1 = list(Rates.objects.values())
    d2 = list(Books.objects.values())
    d3 = list(Members.objects.values())
    for i in d3:
        i['doj']=""
    d=[]
    a=0
    for j in d2:
        d.append(j['bname'])
    for i in d1:
        i['bname'] = d[a]
        a+=1
    context = {
        'data1':d1,
        'data2':d3,
    }
    return render(request, "issue.html",context)

def available(request):
    context = {
        'data':list(Books.objects.values())
    }
    return render(request, "available.html", context)

def done(request):
    ref = request.POST.get('ref')
    pay = request.POST.get('pay')
    d = Issued.objects.get(ref=ref)
    d.charged = pay
    d.returned = True
    d.save()
    messages.success(request, "Book Returning Successful ! Ref ID: "+ref+" Amount Paid : "+pay)

def returns(request):
    if(request.method == "POST"):
        done(request)
    d3 = list(Issued.objects.values())
    d4 = list(Late.objects.values())
    days=[]
    taken=[]
    for i in d3:
        days.append(str((i['to_date']-i['from_date']).days))
        taken.append(str((date_n.today()-i['from_date']).days))
        i['from_date']=str(i['from_date'])
        i['to_date']=str(i['to_date'])
        i['returned']=str(i['returned'])
    context = {
        'data':d3,
        'days':days,
        'taken':taken,
        'late':d4[0]['fine'],
    }
    return render(request, "return.html" ,context)

def members(request):
    context = {
        'data':list(Members.objects.values())
    }
    return render(request, "members.html", context)

def current(request):
    context = {
        'data':list(Issued.objects.values())
    }
    return render(request, "current.html", context)

def charges(request):
    d1 = list(Rates.objects.values())
    d2 = list(Books.objects.values())
    d3 = list(Late.objects.values())
    d=[]
    a=0
    for j in d2:
        d.append(j['bname'])
    for i in d1:
        i['bname'] = d[a]
        a+=1
    context = {
        'data1':d1,
        'late': d3[0]['fine'],
    }
    return render(request, "charges.html", context)

def defaulters(request):
    return render(request, "defaulters.html")