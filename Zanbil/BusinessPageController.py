from django.shortcuts import render

from Zanbil.models import Business, Services
from Zanbil.views import user


class BusinessPageController:

    def Render(requset, business_id):
        business = Business.objects.get(id=business_id)
        services = Services.objects.filter(business__id=business_id)
        return render(requset, 'BusinessPage.html', {'business': business, 'services': services, 'user': user})
