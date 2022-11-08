from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("signin", views.signin, name='signin'),
    path("signout",views.signout, name="signout"),
    path("profile",views.profile, name="profile"),
    path("available",views.available, name="available"),
    path("issue",views.issue, name="issue"),
    path("return",views.returns, name="return"),
    path("members",views.members, name="members"),
    path("current",views.current, name="current"),
    path("charges",views.charges, name="charges"),
    path("defaulters",views.defaulters, name="defaulters"),
]
