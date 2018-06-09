from django.shortcuts import render, redirect

from Zanbil.models import Business, Services, Review ,Categories
from Zanbil.views import user
from .forms import CommentForm


class BusinessPageController:

    def Render(requset, business_id):
        business = Business.objects.get(id=business_id)
        services = Services.objects.filter(business__id=business_id)
        reviews = Review.objects.filter(business=business_id)
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
        categories = Categories.objects.all()
        return render(requset, 'BusinessPage.html',
                      {'business': business, 'services': services, 'reviews': listed_reviews, 'user': user,'categories':categories})


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
