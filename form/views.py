from django.shortcuts import render
from .usrform import usrform
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    submitted = False
    if request.method == "POST":
        form = usrform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = usrform
        if 'submitted' in request.GET:
            submitted=True

        

    return render(request,'form/home.html',{'forms':form,'submitted':submitted})