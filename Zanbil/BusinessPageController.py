from django.shortcuts import render, redirect

from Zanbil.models import Business, Services, Review ,Categories
from Zanbil.views import user
from .forms import CommentForm
from .db import cur


class BusinessPageController:

    def Render(requset, business_id):
        #business = Business.objects.get(id=business_id)
        cur.execute("SELECT * FROM business WHERE id = %s ", (str(business_id),))
        business = cur.fetchall()
        cur.execute("SELECT * FROM services WHERE business_id = %s ", (str(business_id),))
        services = cur.fetchall()
        cur.execute("SELECT * FROM review  WHERE business_id = %s ", (str(business_id),))
        reviews = cur.fetchall()
        listed_reviews = []
        i = 0
        while i < len(reviews):
            if i % 3 == 0:
                if i + 2 < len(reviews):
                    listed_reviews.append([reviews[i], reviews[i + 1], reviews[i + 2]])
                    i += 3
                elif i + 1 < len(reviews):
                    listed_reviews.append([reviews[i], reviews[i + 1]])
                    i += 2
                else:
                    listed_reviews.append([reviews[i]])
                    i += 1
        cur.execute("select * from categories")
        categories = cur.fetchall()
        print(business)
        print(services)
        print(reviews)
        return render(requset, 'BusinessPage.html',
                      {'id' : business_id,'business': business[0], 'services': services, 'reviews': listed_reviews, 'user': user,'categories':categories})


def comment(request, id):
    business = Business.objects.get(pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.business = business
            business.score = business.calculateScore(comment.rating)
            comment.save()
            business.save()

            return redirect('BusinessPage', id)
    else:
        form = CommentForm()
    return render(request, 'createComment.html', {'form': form})
