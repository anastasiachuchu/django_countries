from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.

def home(request):
    return render(request,'index.html')