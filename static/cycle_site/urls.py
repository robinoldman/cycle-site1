from . import views
from django.urls import path
from .views import millstatt_routes, villach_routes, wortersee_routes, badkleinkircheim_routes, team_page, user_route, PostDetailRoute, own_route_post, create_event, create_event1, create_event2, create_event3, SitePostDetailRoute, EditComment, DeleteComment


urlpatterns = [
   #event_detail #PostDetail
   # path("", views.PostList.as_view(), name="home"),
   path("", views.map_view, name='main'),

    path('main/', views.map_view, name='main'),
    path('create_event1/', views.create_event1, name='create_event1'),
    path('create_event2/', views.create_event2, name='create_event2'),
    path('create_event3/', views.create_event3, name='create_event3'),
    path('create_event/', views.create_event, name='create_event'),
    path('route/', views.logRoute, name='route'),
    #path('event_detail/', views.event_detail.as_view(), name='event_detail'),
    #path('event_detail1/', views.event_detail1.as_view(), name='event_detail1'),
    #path('event_detail2/', views.event_detail2.as_view(), name='event_detail2'),
    #path('event_detail3/', views.event_detail3.as_view(), name='event_detail3'),
    path('user_route/', views.user_route, name='user_route'),  
    path('millstatt-routes/', millstatt_routes, name='millstatt_routes'),
    path('villach-routes/', villach_routes, name='villach'),
    path('wortersee-routes/', wortersee_routes, name='wortersee'),
    path('badkleinkircheim-routes/', badkleinkircheim_routes, name='badkleinkircheim'),
    path('team/', team_page, name='team'),
    path('own_route_post/', views.own_route_post.as_view(), name='own_route_post'),
    path('post/<int:pk>/delete/', DeleteComment.as_view(), name='delete_comment'),
    path('post/<int:pk>/edit/', EditComment.as_view(), name='edit_comment'),
    path('postdetailroute/<slug:slug>/', views.PostDetailRoute.as_view(), name ='postdetailroute'),
    path('sitepostdetailroute/<slug:slug>/', views.SitePostDetailRoute.as_view(), name='sitepostdetailroute'),
    #path('postdetail/<slug:slug>/', views.PostDetail.as_view(), name='PostDetail'),
    path('post/<slug:slug>/', SitePostDetailRoute.as_view(), name='own_route_post'),
    
    path('<slug:slug>/', views.PostDetailRoute.as_view(), name='PostDetailRoute'),
    #path('post-detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
    
    ]
