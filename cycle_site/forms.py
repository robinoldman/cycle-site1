from django import forms
from .models import OwnRoute
from .models import Route
from .models import RouteComment
from .models import SiteRouteComment



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
        model = OwnRoute
        fields = ['start_point', 'end_point', 'name', 'description', 'image']
        exclude = ['slug']

class RouteCommentForm(forms.ModelForm):
    """
    Form for creating a RouteComment object.
    """
    class Meta:
        model = RouteComment
        fields = ('body',)


class SiteRouteCommentForm(forms.ModelForm):
    """
    Form for creating a RouteComment object.
    """
    class Meta:
        model = SiteRouteComment
        fields = ('body',)

class RouteForm(forms.ModelForm):
    """
    Form for creating an OwnRoute object.
    """
    class Meta:
        model = OwnRoute
        fields = '__all__'


class SiteRouteForm(forms.ModelForm):
    """
    Form for creating a Route object.
    """

    route = forms.ChoiceField(choices=Route.ROUTE_CHOICES)

    class Meta:
        model = Route
        fields = ['name', 'start_time', 'end_time', 'route']
        exclude = ['slug']



