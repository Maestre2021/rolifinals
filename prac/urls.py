from django.urls import path 
from django.conf.urls import url 

from . import views

urlpatterns = [
	path('', views.Main, name="mainpage"),
	path('Mainget', views.Mainget, name='Mainget'),

	path('Subsidy', views.Subsidy, name='Subsidy'),
	path('Subsidyget', views.Subsidyget, name='Subsidyget'),

	path('Inquiries', views.Inquiries, name="Inquiries"),
	path('Inquiriesandco', views.Inquiriesandco, name="Inquiriesandco"),
	path('Inquire', views.Inquire, name="Inquire"),

	path('Status', views.Status, name="Status"),
	path('Applicant', views.Applicant, name="Applicant"),
	path('Aboutus', views.Aboutus, name="Aboutus"),
	
	url(r'^EditPlace/(?P<id>\d+)$', views.EditPlace, name="EditPlace"),
	url(r'^EditPlace/UpdatePlace/(?P<id>\d+)$', views.UpdatePlace, name="UpdatePlace"),
	url(r'^DeletePlace/(?P<id>\d+)$', views.DeletePlace, name="DeletePlace"),

	url(r'^EditBank/(?P<id>\d+)$', views.EditBank, name="EditBank"),
	url(r'^EditBank/UpdateBank/(?P<id>\d+)$', views.UpdateBank, name="UpdateBank"),
	url(r'^DeleteBank/(?P<id>\d+)$', views.DeleteBank, name="DeleteBank"),

	url(r'^EditInq/(?P<id>\d+)$', views.EditInq, name="EditInq"),
	url(r'^EditInq/UpdateInq/$', views.UpdateInq, name="UpdateInq"),
	url(r'^DeleteInq/(?P<id>\d+)$', views.DeleteInq, name="DeleteInq"),


	
]

# path('Assistance', views.Assistance, name="Assistance"),
# 	path('Assistanceget', views.Assistanceget, name="Assistanceget"),
# 	path('Assisting', views.Assisting, name="Assisting"),
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