from . import views
from django.urls import path
from .views import event_detail
from .views import set_routes


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('map/', views.map_view, name='map'),
    path('create_event1/', views.create_event1, name='create_event1'),
    path('create_event2/', views.create_event2, name='create_event2'),
    path('create_event3/', views.create_event3, name='create_event3'),
    path('create_event/', views.create_event, name='create_event'),
    path('route/', views.Route, name='route'),
    path('event_detail/', views.event_detail.as_view(), name='event_detail'),
    path('event_detail1/', views.event_detail1.as_view(), name='event_detail1'),
    path('event_detail2/', views.event_detail2.as_view(), name='event_detail2'),
    path('event_detail3/', views.event_detail3.as_view(), name='event_detail3'),
    path('user_route/', views.user_route, name='user_route'),
    path('set_routes/', views.set_routes, name='set_routes'),
    path('own_route_post/', views.own_route_post.as_view(), name='own_route_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),]
