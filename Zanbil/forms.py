from django.forms import ModelForm

from .models import Review, Business


class CommentForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'category', 'email', 'phone_number', 'address']
