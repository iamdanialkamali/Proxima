from django.shortcuts import render
from .models import Categories, Services, Reserves, Review, Business,Sans

# Create your views here.
categories = Categories.objects.all()


def main(request):
    return render(request, 'index.html', {'categories': categories})


def Businessesspage(request, category_id):
    category_Businesses = Business.objects.filter(category_id=category_id)
    return render(request, 'Businesses.html', {'category_businesses': category_Businesses, 'categories': categories})


def search(request):
    namefield = request.POST['searchfield']
    founded_Businesses = Business.objects.filter(name__contains=namefield)
    return render(request, 'Businesses.html', {'category_businesses': founded_Businesses, 'categories': categories})

def showtable(request):
    date = request.POST['date']
    #founded_Businesses = Business.objects.filter(name__contains=namefield)
    return render(request, 'Businesses.html')


def beautysalon(request):
    return render(request, 'Businesses.html')


def account(request):
    return render(request, 'accounts.html')


def createbusiness(request):
    return render(request, 'createbusiness.html')


def showservice(request, service_id):
    service = Services.objects.get(id=service_id)
    sanes = Sans.objects.filter(time_table__id=service.timetable_id)
    reviews = Review.objects.filter(service_id=service.id)
    return render(request, 'ServicePage.html', {'service': service, 'sanses': sanes, 'reviews': reviews})


def showbusiness(requset, business_id):
    business = Business.objects.get(id=business_id)
    services = Services.objects.filter(business__id=business_id)
    return render(requset, 'businesspage.html', {'business': business, 'services': services})
