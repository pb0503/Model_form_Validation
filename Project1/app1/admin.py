from django.contrib import admin
from.models import Patient
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display=['f_name','email','l_name', 'age']
admin.site.register(Patient,PatientAdmin)
    
