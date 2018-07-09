from django.shortcuts import render

from Zanbil.models import Business, Categories
from Zanbil.views import user, categories


class BusinessSelectPage:
    def Render(request, category_id):
        category_Businesses = Business.objects.filter(category_id=category_id).order_by('-score')
        top_three = []
        top_three.append(category_Businesses[0])
        top_three.append(category_Businesses[1])
        top_three.append(category_Businesses[2])
        top_three.append(category_Businesses[3])

        remaining_businesess = []
        
        for i in range(4,len(category_Businesses)):
            remaining_businesess.append(category_Businesses[i])

        category_name = Categories.objects.get(pk=category_id).name
        return render(request, 'BusinessSelectPage.html',
                      {'category_name': category_name, 'top_three': top_three,
                      'remaining_businesess':remaining_businesess,'categories': categories,
                       'user': user})
