from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from RenalGuideApp.serializer import *

from .forms import *

from .models import *

# Create your views here.
class LoginPage(View):
    def get(self, request):
        return render(request, 'administration/login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            obj=LoginTable.objects.get(username=username, password=password)
            request.session['user_id'] = obj.id
            if obj.usertype == 'admin' :
                return HttpResponse('''<script>alert("Login succesful");window.location='/adminhomepage'</script>''')
            elif obj.usertype == 'Doctor' :
                return HttpResponse('''<script>alert("Login succesful");window.location='/doctorhomepage'</script>''')
            else:
                HttpResponse('''<script>alert("invalid user");window.location='/'</script>''')
        except LoginTable.DoesNotExist:
                return HttpResponse('''<script>alert("invalid cradentials");window.location='/'</script>''')
                

    
# ////////////////////////////ADMIN ////////////////////////////////////////
class AddandManageDoctors(View):
    def get(self, request):
        c=DoctorTable.objects.all()
        return render(request, 'administration/AddandManageDoctors.html',{'doctor':c})
    
class Addandmanageslot(View):
     def get(self, request):
        c=SlotTable.objects.all()
        return render(request, 'administration/Addandmanageslot.html',{'slot':c})
     
class AddSlot(View):
    def get(self, request):
        return render(request, 'administration/AddSlot.html')
    def post(self, request):
        c=SlotTableForm(request.POST)
        if c.is_valid():
            c.save()
            return redirect('/Addandmanageslot')
 
class AddandManagestaff(View):
    def get(self, request):
        c=NurseTable.objects.all()
        return render(request, 'administration/AddandManagestaff.html',{'nurse':c})
    
class AddDoctor(View):
    def get(self, request):
        return render(request, 'administration/AddDoctor.html')
    def post(self, request):
        c=DoctorTableForm(request.POST, request.FILES)
        print("------------------->", request.POST)
        if c.is_valid():
            Doctor=c.save(commit=False)
            Doctor.LOGINID =LoginTable.objects.create(username=Doctor.email, password=request.POST['password'], usertype="Doctor")
            Doctor.save()
            return HttpResponse('''<script>alert("Added Succesfully");window.location='/AddandManageDoctors'</script>''')
class AddStaff(View):
    def get(self, request):
        return render(request, 'administration/AddStaff.html')
    def post(self, request):
        c=NurseTableForm(request.POST)
        if c.is_valid():
            Nurse=c.save(commit=False)
          
            Nurse.LOGINID =LoginTable.objects.create(username=Nurse.email, password=Nurse, usertype="Nurse")
            Nurse.save()
            return HttpResponse('''<script>alert("Added Succesfully");window.location='/AddandManagestaff'</script>''')
    
class EditDoctor(View):
    def get(self, request, d_id):
        c=DoctorTable.objects.get(id=d_id)
        return render(request, 'administration/EditDoctor.html', {'doctor':c})
    def post(self, request, d_id):
        c=DoctorTable.objects.get(id=d_id)
        a=DoctorTableForm(request.POST,instance=c)
        if a.is_valid():
            a.save()
            return HttpResponse('''<script>alert("Edited Succesfully");window.location='/AddandManageDoctors'</script>''')
            

class DeleteDoctor(View):
    def get(self, request, d_id):
        c=LoginTable.objects.get(id=d_id)
        c.delete()
        return HttpResponse('''<script>alert("Deleted Succesfully");window.location='/AddandManageDoctors'</script>''')
    
class EditSlot(View):
    def get(self, request, sl_id):
        c=SlotTable.objects.get(id=sl_id)
        return render(request, 'administration/EditSlot.html', {'Slot':c, 'time': str(c.time)})
    def post(self, request, sl_id):
        c=SlotTable.objects.get(id=sl_id)
        a=SlotTableForm(request.POST,instance=c)
        if a.is_valid():
            a.save()
            return HttpResponse('''<script>alert("Edited Succesfully");window.location='/Addandmanageslot'</script>''')

class DeleteSlot(View):
    def get(self, request, d_id):
        c=SlotTable.objects.get(id=d_id)
        c.delete()
        return HttpResponse('''<script>alert("Deleted Succesfully");window.location='/Addandmanageslot'</script>''')           
                 
class EditStaff(View):
    def get(self, request, s_id):
        c=NurseTable.objects.get(id=s_id)
        return render(request, 'administration/EditStaff.html', {'Staff':c})
    def post(self, request, s_id):
        c=NurseTable.objects.get(id=s_id)
        a=NurseTableForm(request.POST,instance=c)
        if a.is_valid():
            a.save()
            return HttpResponse('''<script>alert("Edited Succesfully");window.location='/AddandManagestaff'</script>''')
    
class DeleteStaff(View):
    def get(self, request, s_id):
        c=LoginTable.objects.get(id=s_id)
        c.delete()
        return HttpResponse('''<script>alert("Deleted Succesfully");window.location='/AddandManagestaff'</script>''')    
    
class ViewPatientRequest(View):
    def get(self, request):
        c=SlotBookingTable.objects.all()
        return render(request, 'administration/ViewPatientRequest.html',{'booking':c}) 
    
class accept(View):
    def get(self, request, id):
        c = SlotBookingTable.objects.get(id=id)
        c.status = "Accepted"
        c.save()
        c.SLOT.availability = "Booked"
        c.SLOT.save()
        return redirect('/ViewPatientRequest')


class reject(View):
    def get(self, request, id):
        c = SlotBookingTable.objects.get(id=id)
        c.status = "rejected"
        c.save()
        return redirect('/ViewPatientRequest')    
    
class ViewPatient(View):
    def get(self, request):
        c=PatientTable.objects.all()
        return render(request, 'administration/ViewPatient.html',{'patient':c})  

class adminhome(View):
    def get(self, request):
        return render(request, 'administration/adminhomepage.html')

class manageappoinment(View):
    def get(self, request):
        c = AppointmentTable.objects.all()
        return render(request, 'administration/doctorappointment.html',{'appoinment':c})          


class acceptAppointment(View):
    def get(self, request, id):
        c = AppointmentTable.objects.get(id=id)
        c.status = "Accepted"
        c.save()
        return redirect('/doctorappointment')


class rejectAppoinment(View):
    def get(self, request, id):
        c = AppointmentTable.objects.get(id=id)
        c.status = "rejected"
        c.save()
        return redirect('/doctorappointment') 
    

class DoctorLeave(View):
    def get(self,request):
        c=DoctorLeaveTable.objects.all()
        return render(request,'administration/DoctorLeave.html',{'availability':c})
    # def get(self, request,id):
    #     # get doctor
    #     doctor = get_object_or_404(DoctorTable, id=id)

    #     # get availability of that doctor
    #     availability = DoctorAvailabilityTable.objects.filter(
    #         doctor=doctor
    #     ).order_by('date', 'start_time')

    #     context = {
    #         'doctor': doctor,
    #         'availability': availability
    #     }

    #     return render(
    #         request,
    #         'administration/DoctorAvailability.html',
    #         context
    #     )

class DoctorAvailability(View):
    def get(self,request):
        c=DoctorAvailabilityTable.objects.all()
        return render(request,'administration/DoctorAvailability.html',{'availability':c})

class AvailabilityDoctor(View):
    def get(self,request):
        c=DoctorAvailabilityTable.objects.filter(doctor__LOGINID__id = request.session['user_id'])
        return render(request,'doctor/DoctorAvailability.html',{'availability':c})

class acceptLeave(View):
    def get(self, request, id):
        c = DoctorLeaveTable.objects.get(id=id)
        c.Status = "Accepted"
        c.save()
        return redirect('/DoctorLeave')
    
class rejectLeave(View):
    def get(self, request, id):
        c = DoctorLeaveTable.objects.get(id=id)
        c.Status = "rejected"
        c.save()
        return redirect('/DoctorLeave')


class AddandManagecaretaker(View):
    def get(self, request):
        c = CaretakerTable.objects.all()
        return render(request, 'administration/AddandManagecaretaker.html',{'caretaker':c}) 
    
class AddCaretaker(View):
    def get(self, request):
        return render(request, 'administration/AddCaretaker.html')
    def post(self, request):
        c=CaretakerTableForm(request.POST)
        if c.is_valid():
            caretaker=c.save(commit=False)
          
            caretaker.LOGINID =LoginTable.objects.create(username=caretaker.email, password=request.POST['password'], usertype="caretaker")
            caretaker.save()
            return HttpResponse('''<script>alert("Added Succesfully");window.location='/AddandManagecaretaker'</script>''')
        
class EditCaretaker(View):
    def get(self, request, ct_id):
        c=CaretakerTable.objects.get(id=ct_id)
        return render(request, 'administration/EditCaretaker.html', {'caretaker':c})
    def post(self, request, ct_id):
        c=CaretakerTable.objects.get(id=ct_id)
        a=CaretakerTableForm(request.POST,instance=c)
        if a.is_valid():
            a.save()
            return HttpResponse('''<script>alert("Edited Succesfully");window.location='/AddandManagecaretaker'</script>''')
        
class DeleteCaretaker(View):
    def get(self, request, ct_id):
        c=CaretakerTable.objects.get(id=ct_id)
        c.delete()
        return HttpResponse('''<script>alert("Deleted Succesfully");window.location='/AddandManagecaretaker'</script>''')



class acceptcaretaker(View):
    def get(self, request, id):
        c = CaretakerTable.objects.get(id=id)
        c.status = "Accepted"
        c.save()
        return redirect('/AddandManagecaretaker')


class rejectcaretaker(View):
    def get(self, request, id):
        c = CaretakerTable.objects.get(id=id)
        c.status = "rejected"
        c.save()
        return redirect('/AddandManagecaretaker')       

    # //////////////////////////////// D ////////////////////////////////////////

class Addprescription(View):
    def get(self, request, p_id ):
        c=AppointmentTable.objects.filter(DOCTORID__LOGINID__id = request.session['user_id'])
        return render(request, 'doctor/Addprescription.html', {'caretaker':c})
    def post(self, request, p_id):
        a=PrescriptionTableForm(request.POST)
        if a.is_valid():
            f=a.save(commit=False)
            f.APPOINTMENTID=AppointmentTable.objects.get(id=p_id)
            f.DOCID=DoctorTable.objects.get(LOGINID_id = request.session['user_id'])
            f.save()

            return HttpResponse('''<script>alert("Added Succesfully");window.location='/Viewprescription'</script>''')

class Viewprescription(View):
    def get(self, request):
        c=PrescriptionTable.objects.filter(APPOINTMENTID__DOCTORID__LOGINID__id = request.session['user_id'])
        return render(request, 'doctor/Viewprescription.html', {'prescription':c})

    
    
class ViewParameters(View):
    def get(self, request):
        obj=AppointmentTable.objects.filter(DOCTORID__LOGINID_id=  request.session['user_id'])
        pre = PreHDTable.objects.all().order_by('date')
        post = PostHDTable.objects.all().order_by('date')
        combined = zip(pre, post)
        return render(request, 'doctor/ViewParameters.html',{'obj':obj})
    
class ViewParameters1(View):
    def post(self, request):
        patientid=request.POST['patientid']
        pre = PreHDTable.objects.filter(PATIENTID__id=patientid).order_by('date')
        post = PostHDTable.objects.filter(PATIENTID__id=patientid).order_by('date')
        combined = zip(pre, post)
        return render(request, 'doctor/ViewParameters.html',{'combined':combined})
    
class ViewPatients(View):
    def get(self, request):
        c = AppointmentTable.objects.filter(DOCTORID__LOGINID__id = request.session['user_id'])
        return render(request, 'doctor/ViewPatients.html',{'patients':c}) 
    
class ViewPatientRecords(View):
    def get(self, request):
        c = AppointmentTable.objects.filter(DOCTORID__LOGINID__id = request.session['user_id'])
        return render(request, 'doctor/ViewPatientRecords.html',{'patients':c}) 
    
class SearchRecord(View):
    def post(self, request):
        c = AppointmentTable.objects.filter(DOCTORID__LOGINID__id = request.session['user_id'])
        Patient = request.POST['Patient']
        care = PatientTable.objects.get(id=Patient)
        print('===============', care)
        d = care.CARETAKERID
        print('------------------------',d)
        PatientRecord = PatientRecordsTable.objects.filter(PATIENTID=d)
        return render(request, 'doctor/ViewPatientRecords.html', {'records':PatientRecord, 'patients':c})


class Appointmentsbooked(View):
    def get(self, request):
        c=AppointmentTable.objects.filter(DOCTORID__LOGINID__id = request.session['user_id'])
        return render(request, 'doctor/Appointmentsbooked.html', {'appoinment':c})  

class doctorhomepage(View):
    def get(self, request):
        return render(request, 'doctor/doctorhomepage.html')
    
class InformLeave(View):
    def get(self, request):
        return render(request, 'doctor/InformLeave.html')
    def post(self,request):
        d = DoctorTable.objects.get(LOGINID__id = request.session['user_id'])
        c=DoctorLeaveForm(request.POST)
        if c.is_valid():
            reg = c.save(commit=False)
            reg.DOCTOR = d
            reg.Status = 'pending'
            reg.save()
        return redirect('/LeaveDoctor')
    
class InformAvailability(View):
    def get(self, request):
        return render(request, 'doctor/InformAvailability.html')
    def post(self,request):
        d =DoctorTable.objects.get(LOGINID__id = request.session['user_id'])
        c=DoctorAvailabilityForm(request.POST)
        if c.is_valid():
            reg = c.save(commit=False)
            reg.doctor = d
            reg.save()
        return redirect('/AvailabilityDoctor')

    
class Doctorprofile(View):
    def get(self, request):
        obj=DoctorTable.objects.get(LOGINID_id=request.session['user_id'])
        return render(request, 'doctor/Doctorprofile.html',{'doctor':obj})
    def post(self, request):
            obj=DoctorTable.objects.get(LOGINID_id=request.session['user_id'])
            c=DoctorEditForm(request.POST, instance=obj)
            if c.is_valid():
                c.save()
                return HttpResponse('''<script>alert("Edited Succesfully");window.location='/Doctorprofile'</script>''')
    
# ///////////////////////////////////// API //////////////////////////////////////
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class UserReg_api(APIView):
    def post(self, request):
        print("#########################3", request.data)

        user_serial = CaretakerTableSerializer(data=request.data)
        login_serial= LoginTableSerializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(usertype='Caretaker')

            # Assign the login profile to the UserTable and save UserTable
            user_serial.save(LOGINID=login_profile)

            #Return the serialized user  data in the response
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        
        return Response({
            'login_error' : login_serial.errors if not login_valid else None,
            'user_error' : user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)
    

class LoginPage_api(APIView):
    def post(self,request):
        response_dict = {}

        #get data from the request
        username = request.data.get("username")
        password = request.data.get("password")

        #validate input
        if not username or not password:
            response_dict["message"]="Failed"
            return Response(response_dict,status=status.HTTP_400_BAD_REQUEST)
        

        #fetch the user from LoginTable
        t_user = LoginTable.objects.filter(username=username, password=password).first()


        if not t_user:
            response_dict["message"]="Failed"
            return Response(response_dict,status.HTTP_401_UNAUTHORIZED)
        
        else:
            try:
                obj = PatientTable.objects.get(CARETAKERID__LOGINID_id=t_user.id)
                count_obj=CountTable.objects.get(PATIENTID__id=obj.id)
                response_dict["message"]="success"
                response_dict["count"]=count_obj.count
                response_dict['login_id']=t_user.id
                response_dict["UserType"]=t_user.usertype
                print("------------------->", response_dict)
                return Response(response_dict,status=status.HTTP_200_OK)
            except:
                response_dict["message"]="success"
                response_dict['login_id']=t_user.id
                response_dict["UserType"]=t_user.usertype

                return Response(response_dict,status=status.HTTP_200_OK)
            
# /////////////////////////////////////// STAFF ////////////////////////////////////////

class c(APIView):
    def get(self,request,id):
        d=PatientTable.objects.filter(PATIENT_id=id)
        serializer=PatientTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewPatientsParametersAPI(APIView):
    def get(self,request,id):
        patientid=request.data.get('patientid')
        pre = PreHDTable.objects.filter(PATIENTID__id=patientid).order_by('date')
        post = PostHDTable.objects.filter(PATIENTID__id=patientid).order_by('date')
        combined = zip(pre, post)
        return Response(combined.data, status=status.HTTP_200_OK)
    
class ViewDialysisCountAPI(APIView):
    def get(self,request,id):
        d=CountTable.objects.filter(PATIENT_id=id)
        serializer=CountTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

 # ///////////////////////////////////////// CARETAKER /////////////////////////////////////

class ViewPatientAPI(APIView):
    def get(self,request,id):
        print("------------>--------", id)

        d=PatientTable.objects.filter(CARETAKERID__LOGINID_id=id)
        print("------------------>", d)
        serializer=ViewPatientTableSerializer(d, many=True)
        print('------------->', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class ViewPatientRecordsAPI(APIView):
    def get(self, request, id):
        """
        id → LOGINID of caretaker
        """
        records = PatientRecordsTable.objects.filter(
            PATIENTID__CARETAKERID__LOGINID_id=id
        )

        serializer = PatientRecordsSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
class ViewNotificationAPI(APIView):
    def get(self,request,id):
        d=NotificationTable.objects.filter(CARETAKERID__LOGINID_id=id)
        serializer=NotificationTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewNotificationSlotBookingAPI(APIView):
    def get(self,request,id):
        d=SlotBookingTable.objects.filter(PATIENT_id=id)
        serializer=SlotnotificationTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ViewDialysisCountAPI(APIView):
    def get(self,request,id):
        d=CountTable.objects.filter(PATIENT_id=id)
        serializer=CountTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewDoctorAPI(APIView):
    def get(self,request,id):
        d=DoctorTable.objects.filter(PATIENT_id=id)
        serializer=DoctorTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewSlotAvailabilityAPI(APIView):
    def get(self,request):
        d=SlotTable.objects.all()
        serializer=SlotTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewPrescriptionAPI(APIView):
    def get(self,request,id):
        d=PrescriptionTable.objects.filter(PATIENT_id=id)
        serializer=PrescriptionTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewSlotBookingAPI(APIView):
    def post(self,request,id):
        print(request.data)
        d=CaretakerTable.objects.get(LOGINID__id=id)
        serializer=SlotBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(CARETAKERID=d, status = 'pending')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewDoctorAPI(APIView):
    def get(self,request,id):
        d=DoctorTable.objects.filter(PATIENT_id=id)
        serializer=DoctorTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ViewDoctorAppoinmentAPI(APIView):
    def get(self,request,id):
        d=AppointmentTable.objects.filter(PATIENT_id=id)
        serializer=AppointmentTableSerializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class LeaveDoctor(View):
    def get(self,request):
        c=DoctorLeaveTable.objects.filter(DOCTOR__LOGINID__id = request.session['user_id'])
        return render(request,'doctor/DoctorLeave.html',{'availability':c})
    
class DeleteLeave(View):
    def get(self, request,id):
        c=DoctorLeaveTable.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert("Deleted Succesfully");window.location='/LeaveDoctor'</script>''')  


class AddPatient(APIView):

    def get(self, request, id):
        patients = PatientTable.objects.filter(CARETAKERID__LOGINID_id=id)
        patient_serial = PatientTableSerializer(patients, many=True)
        return Response(patient_serial.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        caretaker = CaretakerTable.objects.get(LOGINID_id=id)

        count = PatientTable.objects.filter(CARETAKERID=caretaker).count()
        if count >= 1:
            return Response(
                {'message': 'Only one patient can be added'},
                status=status.HTTP_400_BAD_REQUEST
            )

        patient_serial = PatientTableSerializer(data=request.data)

        if patient_serial.is_valid():
            patient_serial.save(CARETAKERID=caretaker)  
            return Response(
                {'status': 'Patient added successfully'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'status': 'Failed to add patient',
                    'errors': patient_serial.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class AddPatientRecordsAPI(APIView):
    def post(self, request, id):
        """
        id → LOGINID of caretaker
        """

        try:
            # Get caretaker's patient
            patient = PatientTable.objects.get(
                CARETAKERID__LOGINID_id=id
            )
        except PatientTable.DoesNotExist:
            return Response(
                {'message': 'Patient not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Get multiple images
        images = request.FILES.getlist('record_image')

        if not images:
            return Response(
                {'message': 'No images uploaded'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save each image
        for image in images:
            PatientRecordsTable.objects.create(
                PATIENTID=patient,
                record_image=image
            )

        return Response(
            {'message': 'Patient records added successfully'},
            status=status.HTTP_201_CREATED
        )
# class FeedbackView(APIView):
#     def get(self, request, id):
#         feedbacks = FeedbackTable.objects.filter(userid_loginid=id)
#         feedback_serial = FeedbackSerializer(feedbacks, many=True)
#         return Response(feedback_serial.data, status=status.HTTP_200_OK)

    # def post(self, request, id):
    #     user = UserTable.objects.get(loginid=id)
        


class Deletepatient(APIView):
    def get(self,request,id):
        c=PatientTable.objects.get(id=id)
        c.delete()
        return Response({'message':'deleted succesfully'}, status=200)
    


class ViewSlothistory(APIView):
    def get(self,request,id):
        c=SlotBookingTable.objects.filter(CARETAKERID__LOGINID__id=id)
        serializer=SlothistorySerializer(c, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
class ViewDoctor(APIView):
    def get(self,request):
        c=DoctorTable.objects.all()
        serializer=DoctorTableSerializer(c, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class bookDoctor(APIView):
    def post(self, request, id):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&', request.data)
        c = PatientTable.objects.get(CARETAKERID__LOGINID__id=id)
        serializer = AppointmentTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(PATIENTID=c, status="pending")
            return Response(serializer.data, status=status.HTTP_200_OK)

              

class BookingHistory(APIView):
    def get(self, request, id):
        c = AppointmentTable.objects.filter(PATIENTID__CARETAKERID__LOGINID__id = id)
        serializer = AppointmentHistory(c, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)