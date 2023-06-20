from django.contrib import admin
from .models import Post, Comment, Event, Event1, Event2, Event3, own_route, Route, RouteComment
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Event)
admin.site.register(Event1)
admin.site.register(Event2)
admin.site.register(Event3)
admin.site.register(Route)
admin.site.register(RouteComment)
admin.site.register(own_route)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


