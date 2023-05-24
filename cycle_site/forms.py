from .models import Comment
from django import forms
from .models import Event
from .models import own_route
from .models import Event1
from .models import Event2
from .models import Event3


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


class CreateEventForm1(forms.ModelForm):
    class Meta:
        model = Event1
        fields = '__all__'


class CreateEventForm2(forms.ModelForm):
    class Meta:
        model = Event2
        fields = '__all__'


class CreateEventForm3(forms.ModelForm):
    class Meta:
        model = Event3
        fields = '__all__'
