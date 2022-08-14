from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def cv(request):
    
    f = open('CV/data.json','r')
    json_data = json.load(f)
    name = json_data.get('personal').get('name')
    surname = json_data.get('personal').get('surname')
    bday = json_data.get('personal').get('bday')
    bplace = json_data.get('personal').get('bplace')
    adress = json_data.get('personal').get('adress')
    pnum = json_data.get('personal').get('pnum')

    context = {'name':name,'surname':surname,'bday':bday,'bplace':bplace,'adress':adress,'pnum':pnum}

    return render(request,"CV/cv.html",context)