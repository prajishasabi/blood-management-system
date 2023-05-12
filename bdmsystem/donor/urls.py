from django.urls import path
from . import views
app_name='donor'
urlpatterns=[
    path('',views.home,name='index'),
    path('donate_blood',views.donate_blood,name='donate_blood'),
    path('request_blood',views.request_blood,name='request_blood'),
    path('donation_history',views.donation_history,name='donation_history'),
    path('request_history',views.request_history,name='request_history'),
    path('logout',views.logout,name='logout')

]