from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prac.urls')),

]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#  	url(r'^$', views.Main, name='mainpage'),
#  	url(r'^prac/newlist_url$', views.New, name='newlist'),
#     url(r'^prac/(\d+)/$', views.View, name='viewlist'),
#     url(r'^prac/subsidy', views.Subsidy, name='Subsidy'),
#     url(r'^prac/status', views.Status, name='Status'),
#     url(r'^prac/applicant', views.Applicant, name='Applicant'),
#     url(r'^prac/aboutus', views.Aboutus, name='Aboutus'),
#     url(r'^prac/inquiries', views.Inquiries, name='Inquiries'),
#     url(r'^prac/assistance', views.Assistance, name='Assistance'),
#     url(r'^prac/home', views.Main, name='main'),
 
#  	]


"""anneproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""
