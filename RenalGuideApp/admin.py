from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(CaretakerTable)
admin.site.register(DoctorTable)
admin.site.register(NurseTable)
admin.site.register(SlotTable)
admin.site.register(SlotBookingTable)
admin.site.register(PatientTable)
admin.site.register(NotificationTable)
admin.site.register(SlotnotificationTable)
# admin.site.register(DialyzerTable)
admin.site.register(CountTable)
admin.site.register(MessageTable)
admin.site.register(PrescriptionTable)
admin.site.register(DietTable)
admin.site.register(AppointmentTable)
admin.site.register(PreHDTable)
admin.site.register(PostHDTable)
