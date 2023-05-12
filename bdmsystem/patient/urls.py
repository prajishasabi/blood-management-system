from django.urls import path
from . import views
app_name='patient'
urlpatterns=[
    path('',views.home,name='index'),
    path('blood_request',views.blood_request,name='blood_request'),
    path('request_history',views.request_history,name='request_history'),
    path('show_donors' ,views.show_donors,name='show_donors')


]