from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories, Services, Reserves, Review, Business, Sans, Users
from django.shortcuts import redirect

# Create your views here.
categories = Categories.objects.all()
user = Users.objects.get(id=1)


def main(request):
    return render(request, 'index.html', {'categories': categories, 'user': user})


def Businessesspage(request, category_id):
    category_Businesses = Business.objects.filter(category_id=category_id)
    return render(request, 'Businesses.html',
                  {'category_businesses': category_Businesses, 'categories': categories, 'user': user})


def search(request):
    namefield = request.POST['searchfield']
    founded_Businesses = Business.objects.filter(name__contains=namefield)
    return render(request, 'Businesses.html',
                  {'category_businesses': founded_Businesses, 'categories': categories, 'user': user})


def showtable(request):
    date = request.POST['date']
    # founded_Businesses = Business.objects.filter(name__contains=namefield)
    return render(request, 'Businesses.html')


def beautysalon(request):
    return render(request, 'Businesses.html')


def account(request, user_id):
    mybusiness = Business.objects.filter(owner__id=user_id)
    user = Users.objects.get(id=user_id)
    history = Reserves.objects.filter(user_id=user_id)
    return render(request, 'accounts.html',
                  {'user': user, 'historys': history, 'mybusiness': mybusiness, 'categories': categories, 'user': user})


def createbusiness(request):
    return render(request, 'createbusiness.html')


def showservice(request, service_id):
    date = '1397/1/13'
    service = Services.objects.get(id=service_id)
    sanes = Sans.objects.filter(time_table__id=service.timetable_id)
    reviews = Review.objects.filter(service_id=service.id)
    return render(request, 'ServicePage.html',
                  {'service': service, 'sanses': sanes, 'reviews': reviews, 'date': date, 'user': user})


def showbusiness(requset, business_id):
    business = Business.objects.get(id=business_id)
    services = Services.objects.filter(business__id=business_id)
    return render(requset, 'businesspage.html', {'business': business, 'services': services, 'user': user})


def rendertimetable(request):
    if request.method == 'POST':
        timetable_id = request.POST.get('time_table', '')
        date = request.POST.get('date', '')
        service_id = int(request.POST.get('service'))
        selected_sanses = Sans.objects.filter(time_table__id=timetable_id)
        reserved = Reserves.objects.filter(date=date)
        reserved = [e.sans for e in reserved]
        selected_sanses = [sans for sans in selected_sanses]
        final = set(selected_sanses).difference(set(reserved))
        service = Services.objects.get(id=service_id)
        reviews = Review.objects.filter(service_id=service.id)
        return render(request, 'ServicePage.html',
                      {'service': service, 'sanses': final, 'reviews': reviews, 'date': date, 'user': user})


def book(request):
    if (request.method == 'POST'):
        date = request.POST.get('date', '')
        sans_id = request.POST.get('sans_id', '')
        description = request.POST.get('description', '')
        user = Users.objects.get(pk=1)
        service = Services.objects.get(id=request.POST.get('service_id', ''))
        sans = Sans.objects.get(pk=sans_id)
        check_obj = Reserves.objects.filter(date=date, service_id=service.id, sans=sans)
        if (len(check_obj) == 0):
            Reserves.objects.create(user=user, sans=sans, date=date, description=description, service_id=service.id)
        else:
            date = '1397/1/13'
            sanes = Sans.objects.filter(time_table__id=service.timetable_id)
            reviews = Review.objects.filter(service_id=service.id)
            return render(request, 'ServicePage.html',
                          {'service': service, 'sanses': sanes, 'reviews': reviews, 'date': date, 'user': user})

        mybusiness = Business.objects.filter(id=service.business.id)
        history = Reserves.objects.filter(user_id=user.id)
        return render(request, 'accounts.html', {'user': user, 'historys': history, 'mybusiness': mybusiness})
