from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class OwnRoute(models.Model):
    """
    Represents a user-defined route.
    """
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200, unique=True, null=False)  
    start_point = models.CharField(max_length=80)
    end_point = models.CharField(max_length=80)
    difficulty_rating = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    image = models.ImageField(default='enter image')
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("route_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    

class RouteComment(models.Model):
    """
    Represents a comment on a route.
    """
    post = models.ForeignKey(OwnRoute, on_delete=models.CASCADE, related_name="route_comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns a string representation of the RouteComment object.
        """
        return f"Comment {self.body} by {self.name}"

class Route(models.Model):
    """
    Represents a pre-defined route.
    """
    name = models.CharField(max_length=80, default='enter name')
    slug = models.SlugField(max_length=200, unique=True, null=True) 
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True) 
    
   
    ROUTE_CHOICES = (
        ('milstatt', 'Milstatt'),
        ('bad_kleikircheim', 'Bad Kleikircheim'),
        ('villach', 'Villach'),
        ('wortersee', 'Wortersee'),
    ) 
    
    class Meta:
        ordering = ["created_at"]
    route = models.CharField(max_length=20, choices=ROUTE_CHOICES)

    def __str__(self):
        """
        Returns a string representation of the Route object.
        """
        return self.name

    
class SiteRouteComment(models.Model):
    """
    Represents a comment on a route.
    """
    post = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="route_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().pk)
    name = models.CharField(max_length=80)
    
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns a string representation of the RouteComment object.
        """
        return f"Comment {self.body} by {self.name}"

