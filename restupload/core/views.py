from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


def upload(request):
    print request.FILES
    print request.POST
    return HttpResponseRedirect('/')
