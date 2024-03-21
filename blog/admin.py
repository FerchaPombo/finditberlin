from django.contrib import admin
from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from .forms import UsersPostAdminForm



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):

    list_display = ('body', 'post', 'approved')
    list_filter = ('approved', 'author')
    search_fields = ['author', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

