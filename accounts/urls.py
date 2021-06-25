from django.contrib import admin
from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include

urlpatterns = [
    path('usersignup', views.devotee_signup_view,name='usersignup'),
    path('devotee-dashboard', views.devotee_dashboard_view,name='devotee-dashboard'),
    ]