from django.contrib import admin
from .models import Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ("patient_num", "firstname", "lastname",)

admin.site.register(Patient, PatientAdmin)
