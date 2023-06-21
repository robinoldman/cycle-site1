from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .forms import RouteComment
from .models import own_route
from .forms import RouteForm
from django.contrib import messages
from django.views.generic.list import ListView
from .forms import CreateRoute
from .models import Route
from .models import RouteComment


def logRoute(request):

    """
    Handles the logging of a route.
    If the request method is POST and the form is valid, saves the form data,
    displays a success message, and redirects to the main page.
    Otherwise, renders the route.html template with the form.
    """

    if request.method == 'POST':
        form = CreateRoute(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "This is a success message.")
            return redirect('main')
    else:
        form = CreateRoute()
    
    return render(request, 'route.html', {'form': form})


def millstatt_routes(request):

    """
    Retrieves Millstatt routes from the Route model
    and renders the millstatt_routes.html template with the routes.
    """

    mill_routes = Route.objects.filter(route='milstatt')
    return render(request, 'millstatt_routes.html', {'routes': mill_routes})

def badkleinkircheim_routes(request):

    """
    Retrieves Bad Kleinkircheim routes from the Route model
    and renders the badkleinkircheim_routes.html template with the routes.
    """

    bad_routes = Route.objects.filter(route='bad_kleikircheim')
    return render(request, 'badkleinkircheim_routes.html', {'routes': bad_routes})

def wortersee_routes(request):

    """
    Retrieves Wörthersee routes from the Route model
    and renders the wortersee_routes.html template with the routes.
    """

    wort_routes = Route.objects.filter(route='wortersee')
    return render(request, 'wortersee_routes.html', {'routes': wort_routes})

def villach_routes(request):

    """
    Retrieves Villach routes from the Route model
    and renders the villach_routes.html template with the routes.
    """

    vill_routes = Route.objects.filter(route='villach')
    return render(request, 'villach_routes.html', {'routes': vill_routes})

def team_page(request):

    """
    Renders the team.html template.
    """

    return render(request, 'team.html')


def create_event(request):

    """
    Redirects to the create_event page.
    """

    return redirect('create_event')


def create_event1(request):

    """
    Redirects to the create_event1 page.
    """

    return redirect('create_event1')
 

def create_event2(request):

    """
    Redirects to the create_event2 page.
    """

    return redirect('create_event2')

def create_event3(request):
     
    """
    Redirects to the create_event3 page.
    """

    return redirect('create_event3')




class own_route_post(ListView):
 
 """
    Displays a paginated list of own_route objects
    using the own_route_post.html template.
    """

model = own_route
template_name = "own_route_post.html"
paginate_by = 6


def user_route(request):

    """
    Handles the creation of a user route.
    If the request method is POST and the form is valid, saves the form data
    and redirects to the own_route_post page.
    Otherwise, renders the own_route.html template with the form.
    """

    if request.method == 'POST':
        form = RouteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('own_route_post',)

    form = RouteForm()
    return render(request, 'own_route.html', {'form': form})


def map_view(request):
 
    """
    Renders the main.html template.
    """

    return render(request, 'main.html')



class PostDetailRoute(View):

    """
    Displays the details of a specific own_route object,
    including associated comments and comment form,
    using the post_comments.html template.
    """

    def get(self, request, slug, *args, **kwargs):
        
        post = get_object_or_404(own_route, slug=slug)
        comments = post.route_comments.filter(approved=True).order_by("-created_on")
        liked = False
        #if post.likes.filter(id=self.request.user.id).exists():
         #   liked = True

        return render(
            request,
            "post_comments.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": RouteComment()
            },
        )
'''
def post(self, request, slug, *args, **kwargs):
        
        submitted_data = request.POST  
        
        
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = get_object_or_404(Post, slug=slug)
            comment.user = request.user
            comment.save()
        
        return redirect("post-detail", slug=slug)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
''''''
class event_detail(ListView):
    model = Event
    template_name = "event_detail.html"


class event_detail1(ListView):
    model = Event1
    template_name = "event_detail1.html"


class event_detail2(ListView):
    model = Event2
    template_name = "event_detail2.html"


class event_detail3(ListView):
    model = Event3
    template_name = "event_detail3.html"
'''
'''
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

'''
#from .models import Post
#from .forms import CommentForm
#from .models import Event
#from .forms import CreateEventForm
#from .forms import CreateEventForm1
#from .forms import CreateEventForm2
#from .forms import CreateEventForm3
#from .models import Event1
#from .models import Event2
#from .models import Event3