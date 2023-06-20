from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

'''
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
'''
class own_route(models.Model):
    name = models.CharField(max_length=80, )
    slug = models.SlugField(max_length=200, unique=True, default='new-default') 
    start_point = models.CharField(max_length=80, )
    end_point = models.CharField(max_length=80, )
    difficulty_rating = models.CharField(max_length=80, )
    description = models.TextField(max_length=300,)
    image = models.ImageField(default='enter image')


    def __str__(self):
        return self.name

class RouteComment(models.Model):
    post = models.ForeignKey(own_route, on_delete=models.CASCADE,
                             related_name="route_comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Event(models.Model):
    name = models.CharField(max_length=80, default='enter name')
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_place = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Event1(models.Model):
    name = models.CharField(max_length=80, default='enter name')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Event2(models.Model):
    name = models.CharField(max_length=80, default='enter name')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Event3(models.Model):
    name = models.CharField(max_length=80, default='enter name')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name






class Route(models.Model):
    name = models.CharField(max_length=80, default='enter name')
    start_time = models.TimeField()
    end_time = models.TimeField()
    ROUTE_CHOICES = (
        ('milstatt', 'Milstatt'),
        ('bad_kleikircheim', 'Bad Kleikircheim'),
        ('villach', 'Villach'),
        ('wortersee', 'Wortersee'),
    )
    route = models.CharField(max_length=20, choices=ROUTE_CHOICES)

    def __str__(self):
        return self.name