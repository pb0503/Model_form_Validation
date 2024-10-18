from django.contrib import admin
from.models import SignIn
# Register your models here.

class SignInAdmin(admin.ModelAdmin):
    list_display=['f_name','email','l_name', 'age']
admin.site.register(SignIn,SignInAdmin)
    