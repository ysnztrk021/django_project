from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def portfolio(request):

    f = open('CV/data.json','r')
    json_data = json.load(f)
    adress = json_data.get('personal').get('adress')
    pnum = json_data.get('personal').get('pnum')

    context = {'adress':adress,'pnum':pnum}

    return render(request,"portfolio/index.html", context)