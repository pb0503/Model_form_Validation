from django.shortcuts import render
from.forms import EmployeeForm
# Create your views here.

def Employee_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form= EmployeeForm(request.POST)
        if form.is_valid():
           form.save()
    return render(request,'app2/modelform.html',context={'form':form})


