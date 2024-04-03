from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comments, Profile
from .forms import CommentsForm, UsersPostForm, EditForm, EditProfileForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.db.models import Q

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 6

def post_detail(request, slug, *args, **kwargs):
    """
    Post detail view
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("created_on")
    comment_count = comments.count()
    liked = False


    if post.likes.filter(id=request.user.id).exists():
        liked = True

    fav = bool # Remove button if post already saved to favourites based on the user id existing already or not 
    if post.favourites.filter(id=request.user.id).exists():
        fav = True

    if request.method == "POST":
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.approved = request.user.is_superuser
            comment.save()
            if not request.user.is_superuser:
                messages.success(request, 'Your comment submitted and awaiting approval')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(request, 'Error submitting comment. Please check the form.')
    else:
        '''
        Exclude the author field from the form, so it doesnt require a filled filed when saving it to the daatabase
        '''
        comment_form = CommentsForm(initial={'author': request.user})
        
    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form,
            'fav': fav
        },
    )


def post_like(request, slug, *args, **kwargs):
    """
    View for updating the likes 
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id, *args, **kwargs):
    """
    View to delete comment
    """

    post = get_object_or_404(Post, slug=slug, status=1)
    comment = post.comments.get(id=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Sorry, but,you can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_edit(request, slug, comment_id, *args, **kwargs):
    """
    View to edit comments
    """

    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comments, pk=comment_id)
        comment_form = CommentsForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post

            if request.user.is_superuser:
                comment.approved = True
                messages.add_message(request, messages.SUCCESS, 'Your comment was Updated!')
            else:
                comment.approved = False
                messages.add_message(request, messages.SUCCESS, 'Your edited comment has been submitted for approval.')

            comment.save()
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only edit your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def userspost_create(request):
    if request.method == 'POST':
        form = UsersPostForm(request.POST, request.FILES)  # Pass request.FILES for file uploads
        if form.is_valid():
            approved = request.user.is_superuser
            post = form.save(commit=False, author=request.user, approved=approved)
            new_post = post.save()
            if not approved:
                messages.success(request, 'Your post was created successfully! It is now waiting for approval.')
            return redirect('home')
        else:
            error_message = ', '.join([f'{field}: {error}' for field, error in form.errors.items()])
            messages.error(request, f'Error creating the post: {error_message}')
    else:
        form = UsersPostForm()
        form.set_user(request.user)  # Set the user for the form

    return render(request, 'users_dashboard.html', {'form': form})


class UsersPostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'users_dashboard.html'
    paginate_by = 6

    def get_queryset(self):
        return UsersPost.objects.filter(author=self.request.user)


 
@login_required
def users_dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    edit_forms = {post.slug: EditForm(instance=post) for post in user_posts}
    form = UsersPostForm()

    return render(request, 'users_dashboard.html', {'user_posts': user_posts, 'form': form, 'edit_forms': edit_forms})
    
@login_required
def edit_post(request, slug):
    '''View for the edit post form that renders in the users_dashboard'''
    post = get_object_or_404(Post, slug=slug)
    user = request.user


    if request.method == 'POST':
        form = EditForm(request.POST, instance=post, user=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully! waiting for aproval...')
            return redirect('users_dashboard')
        else:
            messages.error(request, 'Error updating the post. Please check the form.')
    else:
        form = EditForm(instance=post, user=request.user)

    return render(request, 'edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_slug):

    post = get_object_or_404(Post, slug=post_slug, author=request.user)

    print(f"Post found: {post.title}") 
    '''Trying to find where are my posts'''

    post.delete()
    return redirect('users_dashboard')

    if request.user == post.author:
        post.delete()
        messages.success(request, 'Post deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this post.')


#logic for the search bar, decided to leave it availabel for non logged in users
def search_bar(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()  # Get the searched word from the form
        if searched:  # Check if the search term is not empty
            # Filter posts by searching in multiple fields (title, content, etc.)
            searched_posts = Post.objects.filter(
                Q(title__icontains=searched) |  # Search in title (case-insensitive)
                Q(content__icontains=searched)  # Search in content (case-insensitive)
            ).distinct()  # Ensure distinct results

            return render(request, 'search_bar.html', {
                'searched': searched,
                'searched_posts': searched_posts
            })
        else:
            # If search term is empty, return all posts
            return render(request, 'search_bar.html', {
                'searched': '',
                'searched_posts': Post.objects.all()  # Return all posts
            })
    else:
        return render(request, 'search_bar.html', {})

# logic for adding  a post to a favourite list 

@login_required
def favourite_add(request, slug): #p ass the id of the user 
    post = get_object_or_404(Post, slug=slug) # grab the post object and get its id 
    if post.favourites.filter(id=request.user.id).exists(): #we check to see if the id = request user's id 
        post.favourites.remove(request.user) # if it does exist, we remove user id from the fav field. 
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(reverse('favourite_list'))# refresh page 

@login_required
def favourite_list(request):
    print("Inside favourite_list view function")
    favourites = Post.objects.filter(favourites=request.user)
    return render(request, 'favourites.html', {'favourites': favourites})

@login_required
def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile edited successfully!')
            return redirect('users_dashboard')  # Redirect to dashboard after saving
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def profile_page(request, slug):
    page_user = get_object_or_404(Profile, id=slug)
    return render(request, 'profile_page.html', {'page_user': page_user})


@login_required
def profile_create(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('users_dashboard')  # Redirect to dashboard page
    else:
        form = EditProfileForm()
    return render(request, 'create_profile.html', {'form': form})
