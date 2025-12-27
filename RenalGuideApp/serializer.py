from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db.models import Sum

from RenalGuideApp.models import *

class LoginTableSerializer(ModelSerializer):
    class Meta:
        model = LoginTable
        fields=['username', 'password', 'usertype']

class CaretakerTableSerializer(ModelSerializer):
    class Meta:
        model = CaretakerTable
        fields=['name', 'age', 'phonenumber','sex','email']
class DoctorTableSerializer(ModelSerializer):
    class Meta:
        model = DoctorTable
        fields=['id','name','age','phonenumber','sex','email','image','qualification','experience']
class DoctorEditSerializer(ModelSerializer):
    class Meta:
        model = DoctorTable
        fields=['name','age','phonenumber','sex','email','qualification','experience']
class DoctorAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = DoctorTable
        fields=['date','starttime','endtime','status']
class DoctorLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorLeaveTable
        fields = ['DOCTOR','leave_from','leave_to','reason']
class NurseTableSerializer(ModelSerializer):
    class Meta:
        model = NurseTable
        fields=['name', 'age','phonenumber','sex','email','qualification','experience']                  
class PatientTableSerializer(ModelSerializer):
    class Meta:
        model = PatientTable
        fields=['name', 'age','sex', 'bloodgroup', 'diagnosis'] 
class ViewPatientTableSerializer(ModelSerializer):
    class Meta:
        model = PatientTable
        fields=['name', 'age','sex', 'bloodgroup', 'diagnosis','id'] 

class PatientRecordsSerializer(ModelSerializer):

    class Meta:
        model = PatientRecordsTable
        fields = '__all__'


class SlotTableSerializer(ModelSerializer):
    class Meta:
        model = SlotTable
        fields=['id','date','time', 'availability']  

class SlotBookingSerializer(ModelSerializer):
    class Meta:
        model = SlotBookingTable
        fields = '__all__'
 

class SlothistorySerializer(ModelSerializer):
      date=serializers.DateField(source='SLOT.date')
      time=serializers.TimeField(source='SLOT.time')
      class Meta:
        model = SlotBookingTable
        fields=['CARETAKERID','SLOT','status','date','time']   


# class RequestTableForm(ModelForm):
#     class Meta:
#         model = RequestTable
#         fields=['status','time','date']
class NotificationTableSerializer(ModelSerializer):
    class Meta:
        model = NotificationTable
        fields=['notification','date']
        
class SlotnotificationTableSerializer(ModelSerializer):
    class Meta:
        model = SlotnotificationTable
        fields=['slotnotification']

class CountTableSerializer(ModelSerializer):
    class Meta:
        model = CountTable
        fields=['count']
class MessageTableSerializer(ModelSerializer):
    class Meta:
        model = MessageTable
        fields=['message']
class PrescriptionTableSerializer(ModelSerializer):
    class Meta:
        model = PrescriptionTable
        fields=['prescription','date']
class DietTableSerializer(ModelSerializer):
    class Meta:
        model = DietTable
        fields=['diet']
class AppointmentTableSerializer(ModelSerializer):
    class Meta:
        model = AppointmentTable
        fields='__all__'
class PreHDTableSerializer(ModelSerializer):
    class Meta:
        model = PreHDTable
        fields=['date','numberofHD','bloodpressure','temperature','weight','weightgain']
class PostHDTableSerializer(ModelSerializer):
    class Meta:
        model = PostHDTable
        fields=['date','numberofHD','bloodpressure','temperature','weight','weightloss']        

class AppointmentHistory(ModelSerializer):
    doctorname = serializers.CharField(source='DOCTORID.name')
    class Meta:
        model = AppointmentTable
        fields = ['date','time', 'bookingdate','doctorname' ]


class PatientTableCountSerializer(serializers.ModelSerializer):
    dialysis_count = serializers.SerializerMethodField()

    class Meta:
        model = PatientTable
        fields = '__all__'

    def get_dialysis_count(self, obj):
        total = CountTable.objects.filter(
            PATIENTID=obj
        ).aggregate(total=sum('count'))['total']
        return total or 0
    
class CaretakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaretakerTable
        fields = '__all__'

class PatientTableCountSerializer(serializers.ModelSerializer):
    dialysis_count = serializers.SerializerMethodField()

    class Meta:
        model = PatientTable
        fields = '__all__'

    def get_dialysis_count(self, obj):
        total = CountTable.objects.filter(
            PATIENTID=obj
        ).aggregate(total=Sum('count'))['total']
        return total or 0
    
class CountSerializer(ModelSerializer):
    class Meta:
        model = CountTable
        fields = '__all__'

class PatientSerializer(ModelSerializer):
    class Meta:
        model = PatientTable
        fields = "__all__"

class PreHDTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreHDTable
        fields = "__all__"


class PostHDTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHDTable
        fields = "__all__"	