# from django.db import models
# from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# check the location key and how to add it later, part of the Post class


# class Location(models.Model):
    # street_name = models.CharField(max_length=255)
    # street_number = models.CharField(max_length=20)
    # city = models.CharField(max_length=255)

    # def __str__(self):
        # return f"{self.street_number} {self.street_name}, {self.city}"


# class Post(models.Model):
    # title = models.CharField(max_length=100, unique=True, blank=False)
    # slug = models.SlugField(max_length=100, unique=True, null=False)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    # updated_on = models.DateTimeField(auto_now=True)
    # content = models.TextField(max_length=100)
    # featured_image = CloudinaryField('image', default="placeholder", blank=False)
    # created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=STATUS, default=0)
    # likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    # excerpt = models.TextField(blank=True)
    # street_name = models.CharField(max_length=255, blank=True, null=True)
    # street_number = models.CharField(max_length=20, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)
    # formatted_address = models.CharField(max_length=255, blank=True, null=True)

    # class Meta:
        # ordering = ['-created_on']

    # def __str__(self):
        # return self.title

    # def number_of_likes(self):
        # return self.likes.count()


# class Comments(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # name = models.CharField(max_length=50)
   # email = models.EmailField()
    # body = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # approved = models.BooleanField(default=False)

    # class Meta:
        # ordering = ['created_on']

    # def __str__(self):
        # return f"This is {self.name} comment: {self.body}"

# 2ns try 
#  from django.db import models
#  from django.contrib.auth.models import User
#  from cloudinary.models import CloudinaryField


# Model for Post and Comment 

#  class Post(model.Models):
    #  title = models.CharField(max_length=100)
    #  author = models.ForeignKey(User, on_delete=models.CASCADE)
    #  create_date = models.DateTimeField(auto_now_add=True)
    #  update_date = models.DateTimeField(auto_now=True)
    #  featured_image = CloudinaryField('image', default="placeholder", blank=False)
    #  street_name = models.CharField(max_length=100)
    #  street_number = models.CharField(max_length=20)
    #  city = models.CharField(max_length=100)
    #  likes = models.ManyToManyField(User, related_name = 'likes', blank=True)
    #  slug = models.SlugField(unique=True)
    #  approved = models.BooleanField(default=False)

    #  def get_absolute_url(self):
        #  from django.urls import reverse
        #  return reverse ('post_detail', args=[str(self.slug)])

#  class Comment(models.Model):
    #  post = models.ForeignKey(Post, on_delete=models.CASCADE)
#      author = models.CharField(max_length=50)
#      body = models.TextField()
#      approved = models.BooleanField(default=False)

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# check the location key and how to add it later, part of the Post class


class Location(models.Model):
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=20)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street_number} {self.street_name}, {self.city}"


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    slug = models.SlugField(max_length=100, unique=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=100)
    featured_image = CloudinaryField('image', default="placeholder", blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    excerpt = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='post_location')

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    approved = models.BooleanField(default=False)

    #class Meta:
        #ordering = ['created_on']

    def __str__(self):
        return f"This is {self.author} comment: {self.body}"
