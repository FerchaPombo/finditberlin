from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comments
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
    Post detail view 
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("created_on")
    comment_count = comments.count()
    liked = False


    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Youy comment submitted and awaiting approval')
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
            "comment_form": comment_form
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


@login_required

def userspost_create(request):
    '''Decorator to autentificate that only when user is logged in ,they can actually access the dashboard'''
    if request.method == 'POST':
        form = UsersPostForm(request.POST)
        print('form', form)

        if form.is_valid():
            post = form.save(commit=False, author=request.user)
            print('post', post)
            new_post = post.save()
            messages.success(request, 'Your post was created successfully!, now its waiting for aproval')
            return redirect('home')
        else:
            error_message = ', '.join([f'{field}: {error}' for field, error in form.errors.items()])
            messages.error(request, f'Error creating the post: {error_message}')
    else:
        form = UsersPostForm()
        form.set_user(request_user) # only lets admins have the status field when creating a post 
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
    

def edit_post(request, slug):
    '''View for the edit post form that renders in the users_dashboard'''
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

    return render(request, 'edit_post.html', {'edit_form': form, 'post': post})


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
        searched = request.POST['searched'] # Get the searched word from the form
        searched_posts = Post.objects.filter(slug__contains=searched) # Filter posts by the searched word 

        return render(request, 'search_bar.html', 
            {'searched':searched,
            'searched_posts': searched_posts})  # Pass the filtered posts to the template
    else: 
        return render(request, 'search_bar.html', {})

#logic for adding  a post to a favourite list 
