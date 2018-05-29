from django.shortcuts import render

from Zanbil.models import Business, Users, Reserves, Categories
from Zanbil.views import categories


class AccountPageController:
    categories = Categories.objects.all()
    def Render(request, user_id):
        mybusiness = Business.objects.filter(owner__id=user_id)
        user = Users.objects.get(id=user_id)
        history = Reserves.objects.filter(user_id=user_id)
        return render(request, 'AccountPage.html',
                      {'user': user, 'historys': history, 'mybusiness': mybusiness, 'categories': categories, 'user': user})
