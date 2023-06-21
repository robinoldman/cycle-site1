from django import forms
from .models import own_route
from .models import Route
from .models import RouteComment


class CreateRoute(forms.ModelForm):
    """
    Form for creating a Route object.
    """
    class Meta:
        model = Route
        fields = '__all__'

class RouteComment(forms.ModelForm):
    """
    Form for creating a RouteComment object.
    """
    class Meta:
        model = RouteComment
        fields = ('body',)

class RouteForm(forms.ModelForm):
    """
    Form for creating an own_route object.
    """
    class Meta:
        model = own_route
        fields = '__all__'


#from .models import Comment
#from .models import Event1
#from .models import Event2
#from .models import Event3
'''
class CommentForm(forms.ModelForm):
    class Met#from .models import Eventa:
        model = Comment
        fields = ('body',)
'''

'''
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
'''

