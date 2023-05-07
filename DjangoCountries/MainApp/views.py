from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json 
# Create your views here.



author = {
    'name':'Anastasia',
    'surname':'Chudakova',
    'email':'stychucc@gmail.com'
    }

def home(request):
    return render(request,'index.html')

def about(request):
    context = {
        'author': author
        }
    return render(request,'about.html',context)


with open('countries.json', 'r') as c:
    items = json.load(c)

def countries_list(request):
        context = {
            'items': items
            }
        return render(request,'countries.html',context)

def country_page(request,name):
        for item in items:
            if item['country'] == name:
                context = {
                'item':item
                }
        return render(request,'country.html',context)
    
languages = []
for item in items:
      for lang in item['languages']:
        if lang not in languages:
            languages.append(lang)
       

def languages_list(request):
        context = {
            'items': sorted(languages)
            }
        return render(request,'languages.html',context)



        
