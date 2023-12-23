from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comments, UsersPost
from .forms import CommentsForm, UsersPostForm, EditForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 6

def post_detail(request, slug, *args, **kwargs):
    """
    A function-based view to view the detail of a post.
    Largely the same as the class-based, but we don't have
    different methods for GET and POST. Because it's not a
    class, all of the extra "self" stuff is removed too.

    Functionally, it's the same, but it is a bit clearer
    what's going on. To differentiate between request methods,
    we use request.method == "GET" or request.method == "POST"
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved = True).count()
    liked = False
    commented = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment awaiting approval')
        else:
            comment_form = CommentsForm()
    else:
        comment_form = CommentsForm()

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
    )


def post_like(request, slug, *args, **kwargs):
    """
    The view to update the likes. Although it should always be
    called using the POST method, we have still added some
    defensive programming to make sure.
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
    view to delete comment
    """
    # queryset = Post.objects.filter(status=1)
    # post = get_object_or_404(queryset)
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = post.comments.get(id=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))



'''
def comment_edit(request, slug, comment_id, *args, **kwargs):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comments.filter(id=comment_id).first()

        comment_form = CommentsForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user.username:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))'''

def comment_edit(request, slug, comment_id, *args, **kwargs):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comments, pk=comment_id)
        comment_form = CommentsForm(data=request.POST, instance=comment)

        # Check if the user is authenticated and the comment author
        if request.user.is_authenticated and comment.author == request.user.username:
            comment_form = CommentsForm(data=request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.approved = False
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'Your comment was Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating comment!')
        else:
            messages.add_message(request, messages.ERROR, 'You can only edit your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

'''#create views for userspost_create

class UsersPostCreate(generic.ListView):
    model = UsersPost
    queryset = Post.objects.filter(status=1)
    template_name = 'users_dashboard.html'
    paginate_by = 6

    def userspost_create(request):
        if request.method == 'POST':
            form = UsersPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.author
                post.save()
                messages.success(request, 'Your post was created succesfully!')
                return redirect(post.get_absolute_url())
            else:
                message.error(request, 'Error creating the post')
        else:
            form = UsersPostForm()
        return render(request, 'users_dashboard.html', {'form': form}) '''

# create a decorator to autentificate that only when user is logged in , they can actually access the dashboard

@login_required
def userspost_create(request):
    if request.method == 'POST':
        form = UsersPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post was created successfully!')
            return redirect(post.get_absolute_url())
        else:
            messages.error(request, 'Error creating the post')
    else:
        form = UsersPostForm()
    return render(request, 'users_dashboard.html', {'form': form})

class UsersPostList(generic.ListView):
    model = UsersPost
    queryset = UsersPost.objects.all()
    template_name = 'users_dashboard.html'
    paginate_by = 6

    def get_queryset(self):
        return UsersPost.objects.filter(author=self.request.user)


#another aproach for the users dashboard 
@login_required
def user_dashboard(request):
    user_posts = Post.objects.filter(author=request.user)
    form = UsersPostForm()

    return render(request, 'users_dashboard.html', {'user_posts': user_posts, 'form': form})

# Create a view for the edit post form that renders in the users_dashboard
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', slug=slug)
        else:
            messages.error(request, 'Error updating the post. Please check the form.')
    else:
        form = EditForm(instance=post, author=request.user)

    return render(request, 'edit_post.html', {'form': form, 'post': post})

'''class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comments_form': CommentsForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comments_form = CommentsForm(data=request.POST)

        if comments_form.is_valid():
            comments_form.instance.email = request.user.email
            comments_form.instance.name = request.user.email
            comments = comments_form.save(commit=False)
            comments.post = post
            comments.save()

        else:
            comments_form == CommentsForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comment': comments,
                'commented': True,
                'liked': liked,
                'comments_form': CommentsForm()

            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLocation(View):

    def post(self, request, slug):
        # Query the database to get the post with the given slug
        post = get_object_or_404(Post, slug=slug, status=1)

        # Get location data from the request
        city = request.POST.get('city')
        street_name = request.POST.get('street_name')
        street_number = request.POST.get('street_number')

        # Update the location fields of the post
        post.location.city = city
        post.location.street_name = street_name
        post.location.street_number = street_number

        # Save the changes to the post
        post.save()

        # Return a JSON response indicating success
        return JsonResponse({"message": "Location updated successfully"})
'''