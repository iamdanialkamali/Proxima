from django.shortcuts import render
from datetime import timedelta
from .models import Categories, Services, Reserves, Review, Business, Sans, Users , TimeTable
from .forms import serviceForm
from django.shortcuts import redirect
from khayyam import *
from .forms import testForm
# Create your views here.

categories = Categories.objects.all()
user = Users.objects.get(id=1)

def render_dashboard(request , business_id):
        business = Business.objects.get(id=business_id)
        services = Services.objects.filter(business__id=business_id)
        reviews = Review.objects.filter(business=business_id)
        reserves=[]
        date = JalaliDate.today().__str__().replace('-', '/')
        week_start_date = JalaliDate.today()-timedelta(days=JalaliDate.today().weekday())
        weekday_date=week_start_date
        this_week_days = []
        for i in range(7):
            weekday_date.__str__().replace('-','/')
            this_week_days.append(weekday_date.__str__().replace('-','/'))
            weekday_date = weekday_date + timedelta(1)

       # reserves = []
       # for date in this_week_days:
       #     reserves.append(len(Reserves.objects.filter(date = date)))
        reserves = getReservePerDate(this_week_days)
        total_count = sum(reserves)

        categories = Categories.objects.all()
        
        return render(request , 'dashboard.html',{'business': business, 'services': services,
         'reviews': reviews, 'user': user,'categories':categories ,'dates':this_week_days , 'reserves_count' : reserves , 'total_reserves_count': total_count})

def addService(request , business_id):
    business = Business.objects.get(pk=business_id)
    timetable = TimeTable.objects.create(sans_count=10 , work_days=[0],rest_times=[1])

    if request.method == 'POST':
    
        print('method is post')
        name = request.POST['ServiceName']
        description = request.POST['Description']
        fee = request.POST['Fee']
        capacity = request.POST['Capacity']
        firstSans = request.POST['firstSans']
        lastSans = request.POST['lastSans']
        restTimeStart = request.POST['restTimeStart']
        restTimeEnd = request.POST['restTimeEnd']
        service = Services.objects.create(name=name,description=description,fee=fee,capacity=capacity,business = business,timetable =timetable, firstSans = firstSans , lastSans = lastSans , restTimeStart = restTimeStart , restTimeEnd = restTimeEnd)
        service.save()
        return redirect('buildTimeTable', service.id)

    return render(request, 'addServiceForm.html', {'business_id':business_id ,'categories':categories})


def changePhoto (request,id):
    if request.method == 'POST':
        form = testForm(request.POST, request.FILES)
        if form.is_valid():
            savedBusiness = Business.objects.get(pk=id) 
            business = form.save(commit=False)
            savedBusiness.image = business.image
            savedBusiness.save()
            return redirect('BusinessPage', id)
        else:
            print('ridi')
    else:
        form = testForm()
    return render(request,'uploadPhotoForm.html', {'id':id })
def getReservePerDate(weekday):
        reserves = []
        for date in weekday:
            reserves.append(len(Reserves.objects.filter(date = date)))
        return reserves

def editBusiness(request , business_id):
    business = Business.objects.get(pk = business_id)
    if request.method == 'POST':
    
        print('method is post')
        
        description = request.POST['Description']
        number = request.POST['number']
        email = request.POST['email']
        address = request.POST['address']
        business.description = description
        business.phone_number = number
        business.email = email
        business.address = address
        business.save()
        return redirect('dashboard' , business.id)


    return render(request, 'editBusiness.html',{'categories':categories , 'business' : business})

    