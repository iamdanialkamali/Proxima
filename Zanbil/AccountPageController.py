from django.shortcuts import render, redirect

from Zanbil.models import Business, Users, Reserves, Categories
from Zanbil.views import categories
from .forms import BusinessForm


class AccountPageController:
    categories = Categories.objects.all()

    def Render(request, user_id):
        mybusiness = Business.objects.filter(owner__id=user_id)
        user = Users.objects.get(id=user_id)
        history = Reserves.objects.filter(user_id=user_id)
        return render(request, 'AccountPage.html',
                      {'user': user, 'historys': history, 'mybusiness': mybusiness, 'categories': categories,
                       'user': user})


def createBusiness(request, id):
    user = Users.objects.get(pk=id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)

        if form.is_valid():
            business = form.save(commit=False)
            business.owner = user
            business.save()

            return redirect('account', user.id)
    else:
        form = BusinessForm()
    return render(request, 'createComment.html', {'form': form})
