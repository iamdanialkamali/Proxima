from django.shortcuts import render
from datetime import timedelta
from .models import Categories, Services, Reserves, Review, Business, Sans, Users , TimeTable
from .forms import serviceForm
from django.shortcuts import redirect
from khayyam import *

from .views import user

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
        print(name)
        print(description)
        print(number)
        print(email)
        print(address)
        print(category)
        business = Business.objects.create(owner=owner,name=name,description=description,phone_number = number,email=email,address = address,category = category)
        business.save()
        # services = Services.objects.filter(business__id=business.id)
        # reviews = Review.objects.filter(business=business.id)
        # categories = Categories.objects.all()
        # listed_reviews = []
        # i = 0
        # while i < len(reviews):
        #     if i % 3 == 0:
        #         if i + 2 < len(reviews):
        #             listed_reviews.append([reviews[i], reviews[i + 1], reviews[i + 2]])
        #             i += 3
        #         elif i + 1 < len(reviews):
        #             listed_reviews.append([reviews[i], reviews[i + 1]])
        #             i += 2
        #         else:
        #             listed_reviews.append([reviews[i]])
        #             i += 1
        return redirect('BusinessPage' , business.id)


    return render(request, 'addBusinessForm.html')
