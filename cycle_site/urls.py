from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('map/', views.map_view, name='map'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    

]
