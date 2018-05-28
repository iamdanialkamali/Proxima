from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories, Services, Reserves, Review, Business, Sans, Users

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
    # founded_Businesses = Business.objects.filter(name__contains=namefield)
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


def rendertimetable(request):
    print(request.method)

    if request.method == 'GET':
        timetable_id = request.GET.get('timetable_id')
        date = request.GET.get('date')
        print(timetable_id)
        print(date)
        selected_sanses = Sans.objects.filter(time_table__id=timetable_id)
        reserved = Reserves.objects.filter(date=date).all()
        reserved = [e.sans for e in reserved]
        selected_sanses = [sans for sans in selected_sanses]
        final = set(selected_sanses).difference(set(reserved))
        print(reserved)
        data = ""
        for i in final:
            data += ' <div class=" time mt-md-3 mt-sm-2"><button  class="btn2 btn btn-outline-secondary  w-75" data-toggle="modal" data-target="#myModal"  id=' + str(
                i.id) + '>' + str(i.start_time) + 'to' + str(i.end_time) + '</button></div>'
        return HttpResponse(data)


def book(request, sansId, date):
    user = Users.objects.get(pk=1)
    sans = Sans.objects.get(pk=sansId)
    reserve = Reserves.objects.create(user=user, sans=sans, date=date)
    return render(request,'reserveSucces.html',{'sans':sans})