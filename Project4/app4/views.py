from django.shortcuts import render
from.forms import StudentForm
# Create your views here.

def Student_view(request):
    form=StudentForm()
    if request.method=='POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            si=form.cleaned_data['stu_id']
            form.save()
    return render(request,'app4/modelform.html',context={'form':form})


