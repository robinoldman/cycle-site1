from . import views
from django.urls import path



    

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('map/', views.map_view, name='map'),
    path('create_event/', views.create_event, name='create_event'),
    path('own_route/', views.own_route, name='own_route'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
