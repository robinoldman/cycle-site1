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
            slug = form.cleaned_data['name']
            route.slug = generate_unique_slug(slug)
            form.save()
            messages.success(request, "This is a success message.")
            return redirect('main')
        else:
            error_messages = form.errors
            print(form.errors)
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
    return render(
        request, 'badkleinkircheim_routes.html', {'routes': bad_routes})


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

    return render(request, 'create_event.html')


@login_required
def create_event1(request):
    return render(request, 'create_event1.html')


@login_required
def create_event2(request):

    """
    Redirects to the create_event2 page.
    """
    return render(request, 'create_event2.html')


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
        print(request.POST)
        form = CreateRoute(request.POST, request.FILES)
        if form.is_valid():
            route = form.save(commit=False)
            slug = form.cleaned_data['name']
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
    Generates a unique slug by appending a number
    to the original slug if it already exists.
    """
    original_slug = slug
    num = 1
    while OwnRoute.objects.filter(slug=slug).exists():
        slug = f'{original_slug}-{num}'
        num += 1
    return slug


class SitePostDetailRoute(View):
    """
    Displays the details of a specific OwnRoute object,
    including associated comments and comment form,
    using the post_comments.html template.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Handles the GET request to display the post details and comments.
        """
        post = get_object_or_404(Route, slug=slug)  # Get the post based on the provided slug
        comments = (
            post.route_comments.filter(approved=True)
            .order_by("-created_on"))  # Retrieve the approved comments associated with the post
        liked = False  # Set the initial liked status to False

        return render(
            request,
            "site_post_comments.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,  # Flag indicating if a comment was submitted
                "liked": liked,  # Flag indicating if the post is liked by the user
                "comment_form": SiteRouteCommentForm()  # Initialize the comment form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handles the POST request to save a new comment for the post.
        """
        post = get_object_or_404(Route, slug=slug)  # Get the post based on the provided slug
        comments = (
            post.route_comments.filter(approved=True)
            .order_by("-created_on"))  # Retrieve the approved comments associated with the post
        liked = False  # Set the initial liked status to False

        comment_form = SiteRouteCommentForm(data=request.POST)  # Create a comment form with the submitted data
        if comment_form.is_valid():
            # If the comment form is valid, create a new comment object and save it to the database
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
                    "commented": True,  # Flag indicating that a comment was successfully submitted
                    "liked": liked,  # Flag indicating if the post is liked by the user
                    "comment_form": SiteRouteCommentForm()  # Initialize a new comment form
                },
            )


class DeleteComment(LoginRequiredMixin, View):
    def post(self, request, pk):
        """
        Handles the POST request to delete a comment.
        """
        comment = get_object_or_404(SiteRouteComment, pk=pk, user=request.user)  # Get the comment based on the provided primary key (pk) and user
        comment.delete()  # Delete the comment
        return redirect("main")  # Redirect to the "main" page after deleting the comment

class EditComment(LoginRequiredMixin, View):
    def post(self, request, pk):
        """
        Handles the POST request to edit/update a comment.
        """
        comment = get_object_or_404(SiteRouteComment, pk=pk, user=request.user)  # Get the comment based on the provided primary key (pk) and user

        if request.method == 'POST':
            form = SiteRouteCommentForm(request.POST, instance=comment)  # Create a form with the submitted data and instance of the comment
            if form.is_valid():
                form.save()  # Save the updated comment
                return redirect("sitepostdetailroute", slug=comment.post.slug)  # Redirect to the post detail page of the updated comment
        else:
            form = SiteRouteCommentForm(instance=comment)  # Create a form with the existing comment instance

        return render(
            request,
            "site_post_comments.html",
            {
                "form": form,  # Pass the form to the template for displaying the comment edit form
                "comment": comment  # Pass the comment object to the template
            },
        )

class PostDetailRoute(View):
    """
    Displays the details of a specific OwnRoute object,
    including associated comments and comment form,
    using the post_comments.html template.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Handles the GET request to display the post details and comments.
        """
        post = get_object_or_404(OwnRoute, slug=slug)  # Get the post based on the provided slug
        comments = (
            post.route_comments
            .filter(approved=True)
            .order_by("-created_on"))  # Retrieve the approved comments associated with the post
        liked = False
        comment_form = RouteCommentForm()  # Create an instance of the comment form

        return render(
            request,
            "post_comments.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,  # Flag indicating if a comment was submitted
                "liked": liked,  # Flag indicating if the post is liked by the user
                "comment_form": comment_form  # Pass the comment form to the template
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(OwnRoute, slug=slug)
        comments = (
            post.route_comments
            .filter(approved=True)
            .order_by("-created_on"))
        liked = False

        comment_form = RouteCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = request.user
            comment.save()
        else:
            comment_form = RouteCommentForm()

        # Redirect to the post detail page after comment submission
        return redirect("own_route_post", slug=slug)
