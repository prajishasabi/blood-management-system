from django.db import models

# Create your models here.

class Donor(models.Model):
    f_name = models.CharField(max_length = 50)
    l_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 30)
    blood_group = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=400)
    district = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length = 40,default ='')
    pic = models.ImageField(upload_to = 'donor/' ,default='static/images/defaulimage.png')

    status = models.CharField(max_length = 30, default = 'pending')

    class Meta:
        db_table = 'donor'
    
class Patient(models.Model):
    f_name = models.CharField(max_length = 50)
    l_name = models.CharField(max_length = 50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length = 50)
    blood_group = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    disease = models.CharField(max_length=500)
    address = models.CharField(max_length=400)
    district = models.CharField(max_length=100)
    phone = models.BigIntegerField()

    class Meta:
        db_table ='patient'


class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(Patient,null=True,on_delete=models.CASCADE)
    request_by_donor = models.ForeignKey(Donor,null=True,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=20)
    nature = models.CharField(max_length=50)
    unit = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=50,default="pending")
    date = models.DateField(auto_now=True)


    class Meta:
        db_table = 'blood_request'
        