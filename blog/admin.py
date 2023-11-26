from django.contrib import admin
from .models import Post, Comments, Location
from django_summernote.admin import SummernoteModelAdmin 
from django import forms


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('street_name', 'street_number', 'city')
    
