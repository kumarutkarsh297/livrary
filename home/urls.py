from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("signin", views.signin, name='signin'),
    path("signout",views.signout, name="signout"),
    path("profile",views.profile, name="profile"),
    path("issue",views.issue, name="issue"),
]
