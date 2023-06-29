from django.contrib import admin
from .models import   OwnRoute, Route, RouteComment, SiteRouteComment
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Route)
admin.site.register(RouteComment)
admin.site.register(OwnRoute)
admin.site.register(SiteRouteComment)


