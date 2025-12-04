"""
URL configuration for RenalGuide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from RenalGuideApp.views import *








urlpatterns = [
    path('', LoginPage.as_view(), name="LoginPage"),

    # ////////////////////////////////// ADMIN ///////////////////////////////

    path('AddandManageDoctors', AddandManageDoctors.as_view(), name="AddandManageDoctors"),
    path('Addandmanageslot', Addandmanageslot.as_view(), name="Addandmanageslot"),
    path('AddandManagestaff', AddandManagestaff.as_view(), name="AddandManagestaff"),
    path('doctorappointment', manageappoinment.as_view(), name="doctorappointment"),
    path('acceptAppointment/<int:id>', acceptAppointment.as_view(), name='accepted'),
    path('rejectAppoinment/<int:id>', rejectAppoinment.as_view(), name='rejected'),
    path('AddDoctor', AddDoctor.as_view(), name="AddDoctor"),
    path('AddSlot', AddSlot.as_view(), name="AddSlot"),
    path('AddStaff', AddStaff.as_view(), name="AddStaff"),
    path('EditDoctor/<int:d_id>', EditDoctor.as_view(), name="EditDoctor"),
    path('DeleteDoctor/<int:d_id>', DeleteDoctor.as_view()),
    path('EditSlot/<int:sl_id>', EditSlot.as_view(), name="EditSlot"),
    path('DeleteSlot/<int:d_id>', DeleteSlot.as_view()),
    path('EditStaff/<int:s_id>', EditStaff.as_view(), name="EditStaff"),
    path('DeleteStaff/<int:d_id>', DeleteStaff.as_view()),
    path('ViewPatientRequest', ViewPatientRequest.as_view(), name="ViewPatientRequest"),
    path('accept/<int:id>', accept.as_view(), name='accepted'),
    path('reject/<int:id>', reject.as_view(), name='rejected'),
    path('ViewPatient', ViewPatient.as_view(), name="ViewPatient"),
    path('AddandManagecaretaker', AddandManagecaretaker.as_view(), name="AddandManagecaretaker" ),
    path('AddCaretaker', AddCaretaker.as_view(), name="AddCaretaker"),
    path('EditCaretaker/<int:ct_id>', EditCaretaker.as_view(), name="EditCaretaker"),
    path('DeleteCaretaker/<int:ct_id>', DeleteCaretaker.as_view()),
    path('acceptcaretaker/<int:id>', acceptcaretaker.as_view(), name='accepted'),
    path('rejectcaretaker/<int:id>', rejectcaretaker.as_view(), name='rejected'),
    path('adminhomepage', adminhome.as_view(), name="adminhomepage"),


    # ////////////////////////////// D ////////////////////////////////////////////

    path('Addprescription/<int:p_id>', Addprescription.as_view(), name="Addprescription"),
    path('Viewprescription', Viewprescription.as_view(), name="Viewprescription"),
    path('ViewParameters', ViewParameters.as_view(), name="ViewParameters"),
    path('ViewParameters1', ViewParameters1.as_view(), name="ViewParameters1"),
    path('ViewPatients', ViewPatients.as_view(), name="ViewPatients"),
    path('Appointmentsbooked', Appointmentsbooked.as_view(), name="Appointmentsbooked"),
    path('doctorhomepage', doctorhomepage.as_view(), name="doctorhomepage" ),
    path('Doctorprofile', Doctorprofile.as_view(), name="Doctorprofile" ),


  









]
