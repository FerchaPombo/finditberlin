from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
from location_field.models import PlainLocationField


STATUS = ((0, "Draft"),(1, "Published"))

# Create your models here.
# check the location key and how to add it later, part of the Post class 

class Post(models.Model):
    title = models.CharField(max_length = 100, unique=True)
    slug = models.SlugField(max_length= 100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=100)
    featured_image = CloudinaryField('image', default="placeholder")
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    city = models.CharField(max_length=250)
    location_field = models.LocationField(based_fields=['city'], zoom=7)

    class Meta: 
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"This is {self.name} comment: {self.body}"

class Place(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)