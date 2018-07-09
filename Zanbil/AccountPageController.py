from django.shortcuts import render, redirect

from Zanbil.models import Business, Users, Reserves, Categories
from Zanbil.views import categories
from .forms import BusinessForm
from .db import cur


class AccountPageController:
    #categories = cur.execute("select * from categories").fetchall()
    def Render(request, user_id):
        cur.execute("select  business.id ,business_name,phone_number,email,score,address,description,category_id,owner_id,name from business join categories on (categories.id = business.category_id) where owner_id = " + str(user_id))
        mybusiness = cur.fetchall()
        print(mybusiness)

        #mybusiness = cur.execute("select * from business where owner_oi = "+ str(user_id)).fetchall()
        cur.execute("select * from users where id=" + str(user_id))
        user = cur.fetchall()[0]

        #history = Reserves.objects.filter(user_id=user_id)
        cur.execute("select * from  reserves  join  services on (services.id = reserves.service_id) join business on (business.id = services.business_id) join sans on (sans.id = reserves.sans_id) where user_id =" + str(user_id))
        cur.execute("select * from test2 where user_id =" + str(user_id))
        history = cur.fetchall()
        cur.execute
        category = cur.fetchall()
        return render(request, 'AccountPage.html',
                      {'user': user, 'historys': history, 'mybusiness': mybusiness, 'categories': categories ,'category':category })


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
