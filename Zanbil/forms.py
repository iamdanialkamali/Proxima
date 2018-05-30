from django.forms import ModelForm
from .models import Review


class CommentForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']
