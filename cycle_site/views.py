from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .forms import RouteCommentForm
from .models import OwnRoute
from .forms import RouteForm, SiteRouteCommentForm
from django.contrib import messages
from django.views.generic.list import ListView
from .forms import CreateRoute, SiteRouteForm
from .models import Route
from .models import RouteComment, SiteRouteComment
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def logRoute(request):

    """
    Handles the logging of a route.
    If the request method is POST and the form is valid, saves the form data,
    displays a success message, and redirects to the main page.
    Otherwise, renders the route.html template with the form.
    """

    if request.method == 'POST':
        form = SiteRouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            slug = form.cleaned_data['name']  # Generate slug based on the name field
            route.slug = generate_unique_slug(slug)
            form.save()
            messages.success(request, "This is a success message.")
            return redirect('main')
        else:
            # Retrieve and display the specific error messages
            error_messages = form.errors
            print (form.errors)
            for field, errors in error_messages.items():
                for error in errors:
                    messages.error(request, f"Error in field {field}: {error}")
    else:
        form = CreateRoute()

    
    return render(request, 'route.html', {'form': form})

@login_required
def millstatt_routes(request):

    """
    Retrieves Millstatt routes from the Route model
    and renders the millstatt_routes.html template with the routes.
    """

    mill_routes = Route.objects.filter(route='milstatt')
    return render(request, 'millstatt_routes.html', {'routes': mill_routes})

@login_required
def badkleinkircheim_routes(request):

    """
    Retrieves Bad Kleinkircheim routes from the Route model
    and renders the badkleinkircheim_routes.html template with the routes.
    """

    bad_routes = Route.objects.filter(route='bad_kleikircheim')
    return render(request, 'badkleinkircheim_routes.html', {'routes': bad_routes})

@login_required
def wortersee_routes(request):

    """
    Retrieves Wörthersee routes from the Route model
    and renders the wortersee_routes.html template with the routes.
    """

    wort_routes = Route.objects.filter(route='wortersee')
    return render(request, 'wortersee_routes.html', {'routes': wort_routes})

@login_required
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

@login_required
def create_event(request):

    """
    Renders to the create_event page.
    """

    return render (request, 'create_event.html')
    
@login_required
def create_event1(request):
    return render(request, 'create_event1.html')



 
@login_required
def create_event2(request):

    """
    Redirects to the create_event2 page.
    """

    return render( request, 'create_event2.html')

@login_required
def create_event3(request):
     
    """
    Redirects to the create_event3 page.
    """

    return render(request,  'create_event3.html')




class own_route_post(LoginRequiredMixin, ListView):
 
    """
    Displays a paginated list of OwnRoute objects
    using the own_route_post.html template.
    """

    model = OwnRoute
    template_name = "own_route_post.html"
    paginate_by = 6


def user_route(request):

    """
    Handles the creation of a user route.
    If request method is POST and the form is valid, saves the form data
    and redirects to the own_route_post page.
    Otherwise, renders the own_route.html template with the form.
    """

    if request.method == 'POST':
        print (request.POST)
        form = CreateRoute(request.POST, request.FILES)
        if form.is_valid():
            route = form.save(commit=False)
            slug = form.cleaned_data['name']  # Generate slug based on the name field
            route.slug = generate_unique_slug(slug) 
            route.save()
            return redirect('own_route_post')
        else:
            print(form.errors)

    form = CreateRoute()
    return render(request, 'own_route.html', {'form': form})


def map_view(request):
 
    """
    Renders the main.html template.
    """

    return render(request, 'main.html')


def generate_unique_slug(slug):
    """
    Generates a unique slug by appending a number to the original slug if it already exists.
    """
    original_slug = slug
    num = 1
    while OwnRoute.objects.filter(slug=slug).exists():
        slug = f'{original_slug}-{num}'
        num += 1
    return slug


class SitePostDetailRoute(LoginRequiredMixin, View):
    """
    Displays the details of a specific OwnRoute object,
    including associated comments and comment form,
    using the post_comments.html template.
    """

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Route, slug=slug)
        comments = post.route_comments.filter(approved=True).order_by("-created_on")
        liked = False

        return render(
            request,
            "site_post_comments.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": SiteRouteCommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Route, slug=slug)
        comments = post.route_comments.filter(approved=True).order_by("-created_on")
        liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        comment_form = SiteRouteCommentForm(data=request.POST)
        if comment_form.is_valid():
            
            comment = comment_form.save(commit=False)
            
            comment.post = post
            comment.name = request.user
            comment.user = request.user
            comment.save()

            return render(
                request,
                "site_post_comments.html",
                {
                    "post": post,
                    "comments": comments,
                    "commented": True,
                    "liked": liked,
                    "comment_form": SiteRouteCommentForm()
                },
            )

class DeleteComment(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(SiteRouteComment, pk=pk, user=request.user)
        comment.delete()
        return redirect("own_route_post")

class EditComment(LoginRequiredMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(SiteRouteComment, pk=pk, user=request.user)
        if request.method == 'POST':
            form = SiteRouteCommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect("sitepostdetailroute", slug=comment.post.slug)
        else:
            form = SiteRouteCommentForm(instance=comment)
        return render(request, "site_post_comments.html", {"form": form, "comment": comment})




class PostDetailRoute(View):
    """
    Displays the details of a specific OwnRoute object,
    including associated comments and comment form,
    using the post_comments.html template.
    """

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(OwnRoute, slug=slug)
        comments = post.route_comments.filter(approved=True).order_by("-created_on")
        liked = False
        comment_form = RouteCommentForm()  # Define the comment_form variable

        if comment_form.is_valid():
            return render(
                request,
                "post_comments.html",
                {
                    "post": post,
                    "comments": comments,
                    "commented": True,
                    "liked": liked,
                    "comment_form": RouteCommentForm()
                },
            )
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(OwnRoute, slug=slug)
        comments = post.route_comments.filter(approved=True).order_by("-created_on")
        liked = False
        # if post.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        comment_form = RouteCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = get_object_or_404(OwnRoute, slug=slug)
            comment.name = request.user
            comment.save()
        else:
            comment_form = RouteCommentForm()

        # Redirect to the post detail page after comment submission
        return redirect("own_route_post", slug=slug)


        










      
