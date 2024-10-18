from django.shortcuts import render
from.forms import ResidentForm
# Create your views here.

def Resident_view(request):
    form=ResidentForm()
    if request.method=='POST':
        form= ResidentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app5/modelform.html',context={'form':form})


