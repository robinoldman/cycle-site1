from .models import Comment 
from django import forms
from .models import Event
from .models import own_route


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RouteForm(forms.ModelForm):
    class Meta:
        model = own_route
        fields = '__all__'


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'