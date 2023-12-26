from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField
from django.urls import reverse




STATUS = ((0, "Draft"), (1, "Published"))



class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=100)
    featured_image = CloudinaryField(
        'image', default="placeholder", blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f" {self.title} | written by {self.author}"

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

class UsersPost(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    featured_image = CloudinaryField('image', default="placeholder", blank=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"This post: {self.body} {self.featured_image} is created by {self.author}"
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.slug)])


