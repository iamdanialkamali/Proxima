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

    return render(request, 'addServiceForm.html', {'business_id':business_id})
