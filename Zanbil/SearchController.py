from django.shortcuts import render

from Zanbil.models import Categories, Users, Business
from Zanbil.views import categories, user


class SearchController:
    categories = Categories.objects.all()
    user = Users.objects.get(id=1)
    def Search(request):
        namefield = request.POST['searchfield']
        founded_Businesses = Business.objects.filter(name__contains=namefield)
        return render(request, 'BusinessSelectPage.html',
                      {'category_businesses': founded_Businesses, 'categories': categories, 'user': user})
