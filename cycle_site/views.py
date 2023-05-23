from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post
from .forms import CommentForm
from .models import Event
from .forms import CreateEventForm
from .models import own_route
from .forms import RouteForm
from django.contrib import messages


def create_event(request):
    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "This is a success message.")

            return redirect('event_detail')
    else:
        form = CreateEventForm()
    return render(request, 'create_event.html', {'form': form})


class event_detail(View):
    def get(self, request, event_id, *args, **kwargs):
        event = get_object_or_404(Event, id=event_id)

        return render(
            request,
            "event_detail.html",
            {
                'name': name,
                'start_time': start_time,
                'end_time': end_time,
                'start_place': start_place
            },
        )


def own_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'own_route.html')

    form = RouteForm()
    return render(request, 'own_route.html', {'form': form})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def map_view(request):
    return render(request, 'map.html')


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
