from django.urls import path
from . import views
app_name='blood'
urlpatterns=[
    path('',views.home,name='index'),
    path('patient_login',views.patient_login,name='patient_login'),
    path('patient_registration',views.patient_registration,name='patient_registration'),
    path('donor_login',views.donor_login,name='donor_login'),
    path('donor_registration',views.donor_registration,name='donor_registration')

]