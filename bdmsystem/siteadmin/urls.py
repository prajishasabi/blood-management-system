from django.urls import path
from . import views
app_name='siteadmin'
urlpatterns=[
    path("",views.home,name='index'),
    path("donors",views.donors,name='donors'),
    path("patients",views.patients,name='patients'),
    path("donations",views.donations,name='donations'),

    path("requests",views.requests,name='requests'),
    
    path("blood_stock",views.blood_stock,name='blood_stock'),
    path("approve_donor",views.approve_donor,name='approve_donor'),
    path('donations/approve/<int:d_id>',views.approve_donations,name='approve_donations'),


    



]