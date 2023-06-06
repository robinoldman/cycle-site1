from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post
from .forms import CommentForm
from .models import Event
from .forms import CreateEventForm
from .forms import CreateEventForm1
from .forms import CreateEventForm2
from .forms import CreateEventForm3
from .models import own_route
from .forms import RouteForm
from django.contrib import messages
from django.views.generic.list import ListView
from .models import Event1
from .models import Event2
from .models import Event3
from .forms import CreateRoute
from .models import Route

def logRoute(request):
    if request.method == 'POST':
        form = CreateRoute(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "This is a success message.")
            return redirect('event_detail')
    else:
        form = CreateRoute()
    
    return render(request, 'route.html', {'form': form})



def millstatt_routes(request):
    mill_routes = Route.objects.filter(route='milstatt')
    return render(request, 'millstatt_routes.html', {'routes': mill_routes})

def millstatt_routes(request):
    mill_routes = Route.objects.filter(route='milstatt')
    return render(request, 'millstatt_routes.html', {'routes': mill_routes})

def millstatt_routes(request):
    mill_routes = Route.objects.filter(route='milstatt')
    return render(request, 'millstatt_routes.html', {'routes': mill_routes})

def millstatt_routes(request):
    mill_routes = Route.objects.filter(route='milstatt')
    return render(request, 'millstatt_routes.html', {'routes': mill_routes})
    
        
def create_event(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "This is a success message.")

            return redirect('event_detail',)
    else:
        form = CreateEventForm()
    return render(request, 'create_event.html', {'form': form})


def create_event1(request):
    if request.method == 'POST':
        form = CreateEventForm1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "This is a success message.")

            return redirect('event_detail1',)
    else:
        form = CreateEventForm1()
    return render(request, 'create_event1.html', {'form': form})


def create_event2(request):
    if request.method == 'POST':
        form = CreateEventForm2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "This is a success message.")

            return redirect('event_detail2',)
    else:
        form = CreateEventForm2()
    return render(request, 'create_event2.html', {'form': form})


def create_event3(request):
    if request.method == 'POST':
        form = CreateEventForm3(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "This is a success message.")

            return redirect('event_detail3',)
    else:
        form = CreateEventForm3()
    return render(request, 'create_event3.html', {'form': form})


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


class own_route_post(ListView):
    model = own_route
    template_name = "own_route_post.html"
    paginate_by = 6


def user_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('own_route_post',)

    form = RouteForm()
    return render(request, 'own_route.html', {'form': form})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def map_view(request):
    return render(request, 'map.html')


def set_routes(request):
    return render(request, 'set_routes.html')


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
