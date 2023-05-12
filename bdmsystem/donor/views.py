from django.shortcuts import redirect, render
from .models import BloodDonate
from blood.models import BloodRequest,Donor

# Create your views here.

def home(request):
    donor = Donor.objects.get(id=request.session['donor'])
    requestmade = BloodRequest.objects.all().filter(request_by_donor=donor).count()
    pendingrequest = BloodRequest.objects.all().filter(request_by_donor = donor,status='pending').count()
    approvedrequest = BloodRequest.objects.all().filter(request_by_donor = donor,status='approved').count()
    rejectedrequest = BloodRequest.objects.all().filter(request_by_donor=donor,status = 'rejected').count()
    context={
        'requests':requestmade,
        'pendingrequest':pendingrequest,
        'approvedrequest':approvedrequest,
        'rejectedrequest':rejectedrequest

    }
    return render(request,'donor/home.html',context)


def donate_blood(request):
    if request.method=='POST':
        disease = request.POST['disease']
        bloodgroup = request.POST['blood_group']
        unit = request.POST['unit']
        age = request.POST['age']
        blooddonate = BloodDonate(disease = disease,bloodgroup=bloodgroup,unit=unit,age=age,donor_id=request.session['donor'])
        blooddonate.save()
    return render(request,'donor/donate_blood.html')

def request_blood(request):
    if request.method == "POST":
        patient_name = request.POST['pname']
        age = request.POST['age']
        reason = request.POST['reason']
        nature = request.POST['nature']
        blood_group = request.POST['blood_group']
        unit = request.POST['unit']
        bloodrequest = BloodRequest(patient_name = patient_name,patient_age=age,
                                    reason = reason,nature= nature,blood_group=blood_group,
                                    unit=unit,request_by_donor_id = request.session['donor'])
        bloodrequest.save()

    return render(request,'donor/request_blood.html')

def donation_history(request):
    donor= Donor.objects.get(id=request.session['donor'])
    donations=BloodDonate.objects.all().filter(donor=donor)
    return render(request,'donor/donation_history.html',{'donations':donations})

def logout(request):
    del request.session['donor']
    request.session.flush()
    return redirect('blood:index')




def request_history(request):
    donor = Donor.objects.get(id=request.session['donor'])
    requests = BloodRequest.objects.all().filter(request_by_donor=donor)
    return render(request,'donor/request_history.html',{'requests':requests})


