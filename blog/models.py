from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))



class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=200)
    featured_image = CloudinaryField(
        'image', default="placeholder", blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    excerpt = models.TextField(blank=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def number_of_likes(self):
        return self.likes.count()

        
class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"This is {self.author} comment: {self.body}"

# create users profile model 

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()

    def __str__(self):
        return str(self.user)

