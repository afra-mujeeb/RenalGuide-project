from django.db import models

# Create your models here.

class LoginTable(models.Model):
    username=models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    usertype=models.CharField(max_length=30,null=True,blank=True)

class CaretakerTable(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    sex=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(null=True,blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE, null=True,blank=True)

class DoctorTable(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    sex=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(null=True,blank=True)
    image=models.FileField()
    qualification=models.CharField(max_length=30,null=True,blank=True)
    experience=models.IntegerField(null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE, null=True,blank=True)

class DoctorAvailabilityTable(models.Model):
    doctor = models.ForeignKey(
        DoctorTable,
        on_delete=models.CASCADE
    )
    date = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    status = models.CharField(
        max_length=20,
        default='Available'
    )

class DoctorLeaveTable(models.Model):
    DOCTOR = models.ForeignKey(DoctorTable, on_delete=models.CASCADE)
    leave_from = models.DateField()
    leave_to = models.DateField()
    reason = models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=100,null=True,blank=True)
class NurseTable(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    sex=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(null=True,blank=True)
    qualification=models.CharField(max_length=30,null=True,blank=True)
    experience=models.IntegerField(null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE, null=True,blank=True)

class PatientTable(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    sex=models.CharField(max_length=30,null=True,blank=True)
    bloodgroup=models.CharField(max_length=30,null=True,blank=True)
    diagnosis=models.CharField(max_length=30,null=True,blank=True)
    CARETAKERID=models.ForeignKey(CaretakerTable,on_delete=models.CASCADE, null=True,blank=True)

class PatientRecordsTable(models.Model):
    PATIENTID = models.ForeignKey(CaretakerTable,on_delete=models.CASCADE, null=True,blank=True)
    DoctorName=models.CharField(max_length=30,null=True,blank=True)
    Dateofconsultation=models.DateField(null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    record = models.ImageField(upload_to="patient_records/")
    uploaded_date = models.DateTimeField(auto_now_add=True)


class SlotTable(models.Model):
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    availability=models.CharField(max_length=30,null=True,blank=True)

class SlotBookingTable(models.Model):
    CARETAKERID=models.ForeignKey(CaretakerTable,on_delete=models.CASCADE, null=True,blank=True)
    SLOT=models.ForeignKey(SlotTable,on_delete=models.CASCADE, null=True,blank=True)
    status=models.CharField(max_length=30,null=True,blank=True)
    

class NotificationTable(models.Model):
    notification=models.CharField(max_length=30,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    
class SlotnotificationTable(models.Model):
    SLOTBOOKINGID = models.ForeignKey(SlotBookingTable, on_delete=models.CASCADE, null=True, blank=True)
    slotnotification=models.CharField(max_length=30,null=True,blank=True)

# class DialyzerTable(models.Model):
#     SLOTID = models.For
#     availability=models.CharField(max_length=30,null=True,blank=True)

class CountTable(models.Model):
    PATIENTID = models.ForeignKey(PatientTable, on_delete=models.CASCADE, null=True, blank=True)
    count=models.IntegerField(null=True,blank=True)

class MessageTable(models.Model):
    message=models.CharField(max_length=30,null=True,blank=True)
    CARETAKERID=models.ForeignKey(CaretakerTable,on_delete=models.CASCADE, null=True,blank=True)
    DOCTORID=models.ForeignKey(DoctorTable,on_delete=models.CASCADE, null=True,blank=True)


class DietTable(models.Model):
    PATIENTID = models.ForeignKey(PatientTable, on_delete=models.CASCADE, null=True, blank=True)
    diet=models.CharField(max_length=30,null=True,blank=True)

class AppointmentTable(models.Model):
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    DOCTORID = models.ForeignKey(DoctorTable, on_delete=models.CASCADE, null=True, blank=True)
    PATIENTID=models.ForeignKey(PatientTable,on_delete=models.CASCADE, null=True,blank=True)
    bookingdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=100, null=True, blank=True)


class PrescriptionTable(models.Model):
    prescription=models.CharField(max_length=30,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    APPOINTMENTID=models.ForeignKey(AppointmentTable,on_delete=models.CASCADE, null=True,blank=True)


class PreHDTable(models.Model):
    PATIENTID = models.ForeignKey(PatientTable, on_delete=models.CASCADE, null=True, blank=True)
    date=models.DateField(null=True,blank=True)
    numberofHD=models.IntegerField(null=True,blank=True)
    bloodpressure=models.CharField(null=True,blank=True)
    temperature=models.CharField(null=True,blank=True)
    weight=models.FloatField(null=True,blank=True)
    weightgain=models.FloatField(null=True,blank=True)
    
class PostHDTable(models.Model):
    PATIENTID = models.ForeignKey(PatientTable, on_delete=models.CASCADE, null=True, blank=True)
    date=models.DateField(null=True,blank=True)
    numberofHD=models.IntegerField(null=True,blank=True)
    bloodpressure=models.CharField(null=True,blank=True)
    weight=models.FloatField(null=True,blank=True)
    weightloss=models.FloatField(null=True,blank=True)

    

    
    

    
    
    
    
    
    