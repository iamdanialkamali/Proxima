from django.http import HttpResponse
from django.shortcuts import render
from .forms import testForm
from .models import Categories, Services, Reserves, Review, Business, Sans, Users ,Test
from django.shortcuts import redirect
from khayyam import *

# Create your views here.

categories = Categories.objects.all()
user = Users.objects.get(id=1)

def main(request):
    return render(request, 'index.html', {'categories': categories, 'user': user})

def test(request):
    return render(request,'service.html')



def imagetest(request,id):
    testt = Test.objects.get(pk=id)
    return render(request,'showtest.html',{'test':testt})