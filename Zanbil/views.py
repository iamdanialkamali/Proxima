from django.http import HttpResponse
from django.shortcuts import render
from .models import Categories, Users,Test
categories = Categories.objects.all()
user = Users.objects.get(id=1)

def main(request):
    return render(request, 'index.html', {'categories': categories, 'user': user})

def test(request):
    return render(request,'form2.html')


def imagetest(request,id):
    testt = Test.objects.get(pk=id)
    return render(request,'showtest.html',{'test':testt})