from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homes(request):
    return render(request, 'home.html',{'name':'elwyn'})