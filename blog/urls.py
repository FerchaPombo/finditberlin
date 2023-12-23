from . import views
from django.urls import path
from .views import edit_post


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('users_dashboard/', views.userspost_create, name='user_postcreate'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<slug:slug>', views.post_like, name='post_like'),
    #path('location/<slug:slug>', views.PostLocation.as_view(), name= 'post_location'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('edit_post/<slug:slug>/', edit_post, name='edit_post'),
]

    
