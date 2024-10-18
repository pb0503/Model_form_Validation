from django.shortcuts import render
from.forms import PatientForm
# Create your views here.

def Patient_view(request):
    form=PatientForm()
    if request.method=='POST':
        form= PatientForm(request.POST)
        if form.is_valid():
           form.save()
    return render(request,'app1/Model_Validation.html',context={'form':form})


