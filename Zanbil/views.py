from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories, Services, Reserves, Review, Business, Sans, Users
from django.shortcuts import redirect
from khayyam import *
# Create your views here.
categories = Categories.objects.all()
user = Users.objects.get(id=1)

def main(request):
    return render(request, 'index.html', {'categories': categories, 'user': user})

def test(request):
    return render(request,'form2.html')
