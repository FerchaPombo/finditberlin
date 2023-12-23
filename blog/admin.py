from django.contrib import admin
from .models import Post, Comments, UsersPost #Location
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from .forms import UsersPostAdminForm
#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields


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


@admin.register(UsersPost)
class UsersPostAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)
    list_display = ('title','created_on')
    search_fields = ['title', 'body']
    summernote_fields = ('body',)  
    form = UsersPostAdminForm

    def get_form(self,request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form 




'''
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('street_name', 'street_number', 'city')
    formfield_overrides = {
        map_fields.AddressField: {'widget':
         map_widgets.GoogleMapsAddressWidget(attrs={
            'data-map-type': 'roadmap', 'componentRestrictions' : {'city':'bln' }}
            )},
    
    }
'''
