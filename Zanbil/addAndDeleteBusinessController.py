from django.shortcuts import render
from datetime import timedelta
from .models import Categories, Services, Reserves, Review, Business, Sans, Users , TimeTable
from .forms import serviceForm
from django.shortcuts import redirect
from khayyam import *
from .views import user,categories

def addBusiness(request):
    owner = user
    if request.method == 'POST':
    
        print('method is post')
        name = request.POST['BusinessName']
        description = request.POST['Description']
        number = request.POST['number']
        email = request.POST['email']
        address = request.POST['address']
        category_name = request.POST['category']
        category = Categories.objects.filter(name = category_name)[0]
        business = Business.objects.create(owner=owner,name=name,description=description,phone_number = number,email=email,address = address,category = category)
        business.save()
        return redirect('BusinessPage' , business.id)


    return render(request, 'addBusinessForm.html',{'categories':categories})
