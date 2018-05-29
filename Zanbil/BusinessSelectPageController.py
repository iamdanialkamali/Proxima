from django.shortcuts import render

from Zanbil.models import Business
from Zanbil.views import user, categories


class BusinessSelectPage:
    def Render(request, category_id):
        category_Businesses = Business.objects.filter(category_id=category_id)
        return render(request, 'BusinessSelectPage.html',
                      {'category_businesses': category_Businesses, 'categories': categories, 'user': user})
