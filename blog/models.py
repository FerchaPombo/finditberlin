from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"),(1, "Published"))

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_lenth = 100, unique=True)
    slug = models.SlugField(max_lenth= 100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    updated_on = models.DateTimeField(author_now=True)
    content = models.TextField(max_lenth=100)
    featured_image = CloudinaryField('image', default="placeholder")
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(autor_now_add=True)
    status = models.IntegerField(choices=Status, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    location = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post_location")
    