from .models import Comment 
from django import forms
from .models import Event


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)





class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'