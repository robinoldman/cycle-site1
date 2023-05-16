from .models import Comment, Route
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['distance', 'duration', 'user_data']
