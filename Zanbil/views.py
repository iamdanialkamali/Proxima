from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories, Services, Reserves, Review, Business, Sans, Users
from django.shortcuts import redirect
from khayyam import *
from .forms import CommentForm
# Create your views here.
categories = Categories.objects.all()
user = Users.objects.get(id=1)

def main(request):
    return render(request, 'index.html', {'categories': categories, 'user': user})


def comment(request, id):

    service= Services.objects.get(pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.service = service
            comment.save()

            return redirect('main')
    else:
        form = CommentForm()
    return render(request, 'createComment.html', {'form': form})
