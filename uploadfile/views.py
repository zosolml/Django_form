from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def getquote(request):
    return render(request,'get.html')

def uploadstp(request):
    if request.method=='POST':
        return redirect('uploadstp')
    else:
        return render(request,'upload.html')
