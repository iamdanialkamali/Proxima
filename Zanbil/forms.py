from django.forms import ModelForm

from .models import Review, Business, Test , Services


class CommentForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'category', 'email', 'phone_number', 'address']

class testForm(ModelForm):
    class Meta:
        model = Business
        fields = ['image']

class serviceForm(ModelForm):
    class Meta :
        model = Services
        fields = ['name','description','fee','capacity']