#  from django.shortcuts import render, get_object_or_404, reverse
#  from django.views import generic, View
#  from django.http import HttpResponseRedirect
#  from .models import Post
#  from .forms import CommentsForm
#  from django.shortcuts import get_object_or_404
#  from django.http import JsonResponse
#  from .models import Location
#  from .utils import get_google_maps_data 
#  
#  class PostLocation(View):
#  
#      def post(self, request, slug):
#          # Query the database to get the post with the given slug
#          post = get_object_or_404(Post, slug=slug, status=1)
#  
#          # Get location data from the request
#          city = request.POST.get('city')
#          street_name = request.POST.get('street_name')
#          street_number = request.POST.get('street_number')
#  
#          # Update the location fields of the post
#          post.location.city = city
#          post.location.street_name = street_name
#          post.location.street_number = street_number
#  
#          # Use the Google Maps API to get coordinates based on the entered address
#          formatted_address, latitude, longitude = get_google_maps_data(street_name, street_number, city)
#  
#          # Update the post with the obtained coordinates
#          post.location.formatted_address = formatted_address
#          post.location.latitude = latitude
#          post.location.longitude = longitude
#  
#          # Save the changes to the post
#          post.save()
#  
#          # Return a JSON response indicating success
#          return JsonResponse({"message": "Location updated successfully"})
#  
#  
#  class PostList(generic.ListView):
#      model = Post 
#      queryset = Post.objects.filter(status=1).order_by('-created_on')
#      template_name = 'index.html'
#      paginate_by = 6
#  
#  class PostDetail(View):
#  
#      def get(self, request, slug, *args, **kwargs):
#          queryset = Post.objects.filter(status=1)
#          post = get_object_or_404(queryset, slug=slug)
#          comments = post.comments.filter(approved=True).order_by('created_on')
#          liked = False
#          if post.likes.filter(id=self.request.user.id).exists():
#              liked = True
#  
#          return render(
#              request,
#              'post_detail.html',
#               {
#                  'post': post,
#                  'comments': comments,
#                  'commented': False,
#                  'liked' : liked,
#                  'comments_form' : CommentsForm()
#              },
#          )
#          
#      def post(self, request, slug, *args, **kwargs):
#          queryset = Post.objects.filter(status=1)
#          post = get_object_or_404(queryset, slug=slug)
#          comments = post.comments.filter(approved=True).order_by('created_on')
#          liked = False
#          if post.likes.filter(id=self.request.user.id).exists():
#              liked = True
#  
#          comments_form = CommentsForm(data=request.POST)
#  
#          if comments_form.is_valid() :
#              comments_form.instance.email = request.user.email
#              comments_form.instance.name = request.user.email
#              comments = comments_form.save(commit=False)
#              comments.post = post 
#              comments.save()
#  
#          else:
#              comments_form == CommentsForm()
#  
#          return render(
#              request,
#              'post_detail.html',
#               {
#                  'post': post,
#                  'comment': comments,
#                  'commented' : True,
#                  'liked' : liked,
#                  'comments_form' : CommentsForm()
#  
#              },
#          )
#  class PostLike(View):
#      
#      def post(self, request, slug):
#          post = get_object_or_404(Post, slug=slug)
#          
#          if post.likes.filter(id=request.user.id).exists():
#              post.likes.remove(request.user)
#          else:
#              post.likes.add(request.user)
#  
#          return HttpResponseRedirect(reverse('post_detail', args=[slug]))
#  
#  
#  class PostLocation(View):
#  
#      def post(self, request, slug):
#          # Query the database to get the post with the given slug
#          post = get_object_or_404(Post, slug=slug, status=1)
#  
#          # Get location data from the request
#          city = request.POST.get('city')
#          street_name = request.POST.get('street_name')
#          street_number = request.POST.get('street_number')
#  
#          # Update the location fields of the post
#          post.location.city = city
#          post.location.street_name = street_name
#          post.location.street_number = street_number
#  
#          # Save the changes to the post
#          post.save()
#  
#          # Return a JSON response indicating success
#          return JsonResponse({"message": "Location updated successfully"})

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentsForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Location



class PostList(generic.ListView):
    model = Post 
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
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
                'liked' : liked,
                'comments_form' : CommentsForm()
            },
        )
        
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comments_form = CommentsForm(data=request.POST)

        if comments_form.is_valid() :
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
                'commented' : True,
                'liked' : liked,
                'comments_form' : CommentsForm()

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
