from django import forms
from .models import own_route
from .models import Route
from .models import RouteComment



class CreateRoute(forms.ModelForm):
    """
    Form for creating a Route object.
    """
    start_point = forms.CharField(max_length=100, required=True)
    end_point = forms.CharField(max_length=100, required=True)
    name = forms.CharField(max_length=100, required=True)
    difficulty_rating = forms.CharField(max_length=80)
    description = forms.CharField(max_length=300)
    

    class Meta:
        model = own_route
        fields = ['start_point', 'end_point', 'name', 'description', 'image']
        exclude = ['slug']

class RouteCommentForm(forms.ModelForm):
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
    class Meta:
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

