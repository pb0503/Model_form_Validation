from django.contrib import admin
from.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_id','f_name','email','l_name', 'age']
admin.site.register(Employee,EmployeeAdmin)
    