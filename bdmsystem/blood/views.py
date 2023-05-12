from django.shortcuts import render,redirect
from .models import Donor,Patient

# Create your views here.

def home(request):
    return render(request,'blood/home.html')

def patient_login(request):
    msg =""
    if request.method =='POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        try:
            patient = Patient.objects.get(user_name = user_name,password = password)
            request.session['patient'] = patient.id
            return redirect('patient:index')
        except Exception  as e:
            msg = 'Email or password incorrect'

    return render(request,'blood/patient_login.html',{'message':msg})




def patient_registration(request):
    if request.method =='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user_name =request.POST['user_name']
        password = request.POST['password']
        blood_group = request.POST['bg']
        age = request.POST['age']
        gender = request.POST['gender']
        disease = request. POST['disease']
        address = request.POST['address']
        district = request.POST['district']
        phone = request.POST['phone']
        patient = Patient(f_name =fname,l_name =lname,user_name =user_name,
                          password = password,blood_group=blood_group,age = age,
                          gender = gender,disease = disease,address=address,
                          district = district,phone = phone
                          )
        patient.save()
        return redirect('blood:patient_login')


    return render(request,'blood/patient_registration.html')



def donor_login(request):
    msg = ''

    if request.method =='POST':
    
        email = request.POST['email']
        password = request.POST['password']
        try:
            donor = Donor.objects.get(email = email,password = password)
            request.session['donor'] = donor.id
            return redirect('donor:index')
        except Exception  as e:
            msg = 'Email or password incorrect'

    return render(request,'blood/donor_login.html',{'message':msg})


def donor_registration(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        blood_group = request.POST['bg']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        district = request.POST['district']
        phone = request.POST['phone']
        if 'image' in request.FILES:
            image = request.FILES['image']
            donor = Donor(f_name = fname, l_name=lname,email = email,blood_group=blood_group,age=age, 
                       gender = gender,address = address, district = district , phone = phone,
                        pic = image)
        else:
             donor = Donor(f_name = fname, l_name=lname,email = email,blood_group=blood_group,age=age, 
                       gender = gender,address = address, district = district , phone = phone)
        donor.save()
        return redirect('blood:donor_login')


    return render(request,'blood/donor_registration.html')





