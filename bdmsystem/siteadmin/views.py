from django.shortcuts import redirect, render
from blood.models import Donor,BloodRequest, Patient
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from donor.models import BloodDonate
from siteadmin.models import Stock
from django.db.models import Sum


# Create your views here.

def home(request):
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={

        'A1':Stock.objects.get(bloodgroup="A+"),
        'A2':Stock.objects.get(bloodgroup="A-"),
        'B1':Stock.objects.get(bloodgroup="B+"),
        'B2':Stock.objects.get(bloodgroup="B-"),
        'AB1':Stock.objects.get(bloodgroup="AB+"),
        'AB2':Stock.objects.get(bloodgroup="AB-"),
        'O1':Stock.objects.get(bloodgroup="O+"),
        'O2':Stock.objects.get(bloodgroup="O-"),
        # 'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['unit__sum'],
        # 'totalrequest':BloodRequest.objects.all().count(),
        # 'totalapprovedrequest':BloodRequest.objects.all().filter(status='Approved').count()
    }
    render(request,'siteadmin/home.html',context=dict)



def donors(request):
    donor = Donor.objects.filter(status ='approved')
    return render(request,'siteadmin/donors.html',{'donors_list':donor})

def patients(request):
    patient = Patient.objects.all()
    return render(request,'siteadmin/patients.html',{'patient_list':patient})

def donations(request):
    blooddonate = BloodDonate.objects.filter(status='Pending')
    return render(request,'siteadmin/donations.html',{'blood_donate':blooddonate})

def requests(request):
    bloodrequest = BloodRequest.objects.filter(status="pending")

    return render(request,'siteadmin/blood_requests.html',{'blood_request':bloodrequest})

def blood_stock(request):
    totalunit=Stock.objects.aggregate(Sum('unit'))
    dict={

        'A1':Stock.objects.get(bloodgroup="A+"),
        'A2':Stock.objects.get(bloodgroup="A-"),
        'B1':Stock.objects.get(bloodgroup="B+"),
        'B2':Stock.objects.get(bloodgroup="B-"),
        'AB1':Stock.objects.get(bloodgroup="AB+"),
        'AB2':Stock.objects.get(bloodgroup="AB-"),
        'O1':Stock.objects.get(bloodgroup="O+"),
        'O2':Stock.objects.get(bloodgroup="O-"),
        # 'totaldonors':Donor.objects.all().count(),
        'totalbloodunit':totalunit['unit__sum'],
        # 'totalrequest':BloodRequest.objects.all().count(),
        # 'totalapprovedrequest':BloodRequest.objects.all().filter(status='Approved').count()
    }
    return render(request,'siteadmin/blood_stock.html',context=dict)



def approve_donor(request):
    donors = Donor.objects.filter(status ='pending')
    if request.method =='POST':
        donor_id = request.POST['donor_id']
        donor = Donor.objects.get(id=donor_id)
        
        if 'approve' in request.POST:
        
            password = 'donor-' + str(donor.phone)[5:]

           
            donor.status = 'approved' 
            donor.password = password
            donor.save()
            
            mail_subject = "Account Approval"
            message_body = "Hi your account has been approved by Admin,you can now login with  your email  and temporary password " + password 

           
        if 'reject' in request.POST:
            
            donor.status = 'rejected'
            donor.save()
            mail_subject = 'Account Rejected'
            message_body = 'sorry!we can not approve your request right now'
             

        send_mail(
            subject = mail_subject,
            message = message_body,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [donor.email]
            )

    return render(request,'siteadmin/approve_donor.html',{'donors_list':donors})


def approve_donations(request,d_id):
    donation = BloodDonate.objects.get(id = d_id)
    donation_blood_group=donation.bloodgroup
    donation_blood_unit=donation.unit

    stock=Stock.objects.get(bloodgroup=donation_blood_group)
    stock.unit=stock.unit+donation_blood_unit
    stock.save()
    donation.status='Approved'
    donation.save()
    
    return redirect ('siteadmin:donations')

# def logout(request):
#     del request.session['']
#     request.session.flush()
#     return redirect('blood:index')








