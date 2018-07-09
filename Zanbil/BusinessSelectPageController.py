from django.shortcuts import render

from Zanbil.models import Business, Categories
from Zanbil.views import user, categories
from.db import cur


class BusinessSelectPage:
    def Render(request, category_id):
        cur.execute("SELeCT * from business  where category_id = %s ",(str(category_id)))

        category_Businesses = cur.fetchall()
        cur.execute("SELeCT * from categories  where id = %s ",(str(category_id)))
        category_name =cur.fetchall()

        return render(request, 'BusinessSelectPage.html',
                      {'category_name': category_name, 'category_businesses': category_Businesses,
                       'categories': categories, 'user': user})
