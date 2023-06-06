from django.http import JsonResponse
from django.shortcuts import redirect, render
from blood.models import BloodRequest, Donor, Patient

# Create your views here.


def home(request):
    patient = Patient.objects.get(id=request.session['patient'])
    requestmade = BloodRequest.objects.all().filter(request_by_patient = patient ).count()
    pendingrequest = BloodRequest.objects.all().filter(request_by_patient = patient,status = 'pending').count()
    approvedrequest = BloodRequest.objects.all().filter(request_by_patient = patient,status = 'approved').count()
    rejectedrequest = BloodRequest.objects.all().filter(request_by_patient = patient,status = 'rejected').count()
    context = {
        'requests':requestmade,
        'pendingrequest':pendingrequest,
        'approvedrequest': approvedrequest,
        'rejectedrequest' : rejectedrequest

    }
    
    return render(request,'patient/home.html',context)

def blood_request(request):
    if request.method == "POST":
        patient_name = request.POST['pname']
        age = request.POST['age']
        reason = request.POST['reason']
        nature = request.POST['nature']
        blood_group = request.POST['blood_group']
        unit = request.POST['unit']
        bloodrequest = BloodRequest(patient_name = patient_name,patient_age=age,
                                    reason = reason,nature= nature,blood_group=blood_group,
                                    unit=unit,request_by_patient_id = request.session['patient'])
        bloodrequest.save()
    return render(request,'patient/blood_request.html')

def request_history(request):
    return render(request,'patient/request_history.html')

def logout(request):
    del request.session['patient']
    request.session.flush()
    return redirect('blood:index')

def show_donors(request):
    print(request)
    if request.method == 'POST':
        district = request.POST['district']
        donors = Donor.objects.filter(district = district)
        
        
        donors_list =[ {
            'name': donor.f_name,
            'email': donor.email,
            'blood_group': donor.blood_group,
            'gender': donor.gender,
            'address': donor.address,
            'phone': donor.phone
        }for donor in donors]
            # donors_list.append(donor_dict)

    return JsonResponse({'donors_list': donors_list})