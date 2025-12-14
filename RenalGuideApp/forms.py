
from django.forms import ModelForm

from RenalGuideApp.models import *


class LoginTableForm(ModelForm):
    class Meta:
        model = LoginTable
        fields=['username', 'password', 'usertype']

class CaretakerTableForm(ModelForm):
    class Meta:
        model = CaretakerTable
        fields=['name', 'age', 'phonenumber','sex','email']
class DoctorTableForm(ModelForm):
    class Meta:
        model = DoctorTable
        fields=['name','age','phonenumber','sex','email','image','qualification','experience']
class DoctorEditForm(ModelForm):
    class Meta:
        model = DoctorTable
        fields=['name','age','phonenumber','sex','email','qualification','experience']
class NurseTableForm(ModelForm):
    class Meta:
        model = NurseTable
        fields=['name', 'age','phonenumber','sex','email','qualification','experience']                  
class PatientTableForm(ModelForm):
    class Meta:
        model = PatientTable
        fields=['name', 'age','sex'] 
class PatientRecordsTableForm(ModelForm):
    class Meta:
        model = PatientRecordsTable
        fields=['record'] 



class SlotTableForm(ModelForm):
    class Meta:
        model = SlotTable
        fields=['date','time']  

# class RequestTableForm(ModelForm):
#     class Meta:
#         model = RequestTable
#         fields=['status','time','date']
class NotificationTableForm(ModelForm):
    class Meta:
        model = NotificationTable
        fields=['notification','date']
        
class SlotnotificationTableForm(ModelForm):
    class Meta:
        model = SlotnotificationTable
        fields=['slotnotification']

class CountTableForm(ModelForm):
    class Meta:
        model = CountTable
        fields=['count']
class MessageTableForm(ModelForm):
    class Meta:
        model = MessageTable
        fields=['message']
class PrescriptionTableForm(ModelForm):
    class Meta:
        model = PrescriptionTable
        fields=['prescription','date']
class DietTableForm(ModelForm):
    class Meta:
        model = DietTable
        fields=['diet']
class AppointmentTableForm(ModelForm):
    class Meta:
        model = AppointmentTable
        fields=['date','time']
class PreHDTableForm(ModelForm):
    class Meta:
        model = PreHDTable
        fields=['date','numberofHD','bloodpressure','temperature','weight','weightgain']
class PostHDTableForm(ModelForm):
    class Meta:
        model = PostHDTable
        fields=['date','numberofHD','bloodpressure','temperature','weight','weightloss']        

                                                        

                                 