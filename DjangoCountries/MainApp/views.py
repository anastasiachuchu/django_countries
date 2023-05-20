from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json 
from MainApp.models import Item
from MainApp.models import Language
from django.core.exceptions import ObjectDoesNotExist
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


# with open('/home/anastasia/Projects3/DjangoCountries/countries.json', 'r') as c:
#     items = json.load(c)

#     for item in items:
#          i= Item()
#          i.country = item['country']
#          i.save()


def countries_list(request):
        items = Item.objects.all()
        context = {
            'items': items
            }
        return render(request,'countries.html',context)


def country_page(request,name):
    try:
        item = Item.objects.get(country=name) 
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'not found {name} name =(')
    
    language = item.language.all()

    context = {
        'item':item,
        'language': language
        }
    return render(request,'country.html',context)

# with open('/home/anastasia/Projects3/DjangoCountries/countries.json', 'r') as c:
#     items = json.load(c)
    
# languages = []
# for item in items:
#       for lang in item['languages']:
#         if lang not in languages:
#             languages.append(lang)
# sorted_languages = sorted(languages)

# for lang_ in sorted_languages:
#     one_lang = Language()
#     one_lang.name = lang_
#     one_lang.save()
    

def languages_list(request):
        items = Language.objects.all()
        context = {
            'items': items
            }
        return render(request,'languages.html',context)


# with open('/home/anastasia/Projects3/DjangoCountries/countries.json', 'r') as c:
#     items = json.load(c)

# for item in items:
#      languages = Language.objects.all()
#      countries = Item.objects.all()
#      for lang in languages:
#           if lang.name in item['languages']:
#                for country in countries:
#                     if country.country == item['country']:
#                          country.language.add(lang)
#                          country.save()
               


        
