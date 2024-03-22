from . import views
from django.urls import path
from .views import edit_post , delete_post, users_dashboard, userspost_create, favourite_add, favourite_list


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('users_dashboard/', views.users_dashboard, name='users_dashboard'),
    path('userspostform/', views.userspost_create, name='users_post_form'),
    path('favourites/', views.favourite_list, name='favourite_list'),
    path('search_bar', views.search_bar, name='search_bar'),
    path('fav/<slug:slug>/', views.favourite_add, name='favourite_add'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<slug:slug>', views.post_like, name='post_like'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('edit_post/<slug:slug>/', edit_post, name='edit_post'),
    path('delete_post/<slug:post_slug>/', delete_post, name='delete_post'),
    
    

]

    
