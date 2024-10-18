from django.shortcuts import render
from.forms import SignInForm
# Create your views here.

def SignIn_view(request):
    form=SignInForm()
    if request.method=='POST':
        form= SignInForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'app3/modelform.html',context={'form':form})


