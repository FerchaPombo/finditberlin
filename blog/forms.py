from .models import Comments, Post, Profile
from django import forms
from crispy_forms.helper import FormHelper  
from crispy_forms.layout import Layout, Submit
from cloudinary.forms import CloudinaryJsFileField
from cloudinary.models import CloudinaryField as BaseCloudinaryField
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.shortcuts import render

STATUS = ((0, "Draft"), (1, "Published"))

class CommentsForm(forms.ModelForm):  
    class Meta:
        model = Comments  
        fields = ['author', 'body']
        widgets = {'author': forms.HiddenInput()}


    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'body',
            Submit('submit', 'Submit', css_class='btn-primary btn-outline-dark btn-sm') 
        )

    def save(self, commit=True):
        comment = super(CommentsForm, self).save(commit=False)
        if not comment.author:
            comment.author = self.initial['author']
        if commit:
            comment.save()
        return comment
 

class CloudinaryField(BaseCloudinaryField):
    def formfield(self, **kwargs):
        return super().formfield(widget=CloudinaryJsFileInput(), **kwargs)

class UsersPostForm(forms.ModelForm):
    '''Class for Users Post based on  model Post'''
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write something here!'}),
        }
#check if a post with the same title exists, if it does, raises validation.
    def clean_title(self):
        title = self.cleaned_data['title']
        slug = slugify(title)
 
        if Post.objects.filter(slug=slug).exists():
            raise ValidationError('A post with this title already exist')

        return title

#slug field populated with the title
    def save(self, commit=True, author=None):
        post = super(UsersPostForm, self).save(commit=False)
        post.author = author
        if not post.slug:
            post.slug = slugify(post.title)
        if commit:
            post.save
        return post

    def __init__(self, *args, **kwargs):
        super(UsersPostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'title',
            'featured_image',
            'content',
            Submit('submit', 'Submit', css_class='btn-primary btn-outline-dark btn-sm')
        )

        # functions added to add status field only if you are the admin 
        def add_status_field(self):
            if self.user_is_admin():
                self.fields['status']= forms.ChoiceField(choices=Post.STATUS)
        def user_is_admin(self):
            return self.user.user_is_admin
        def set_user(self,user):
            self.user = user
            self.add_status_field()


class EditForm(forms.ModelForm):
    '''Form to edit a post'''
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image','excerpt']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user passed as argument
        super().__init__(*args, **kwargs)
        if user and user.is_superuser:  # Check if the user is a superuser (admin)
            self.fields['status'] = forms.ChoiceField(choices=STATUS, initial=self.instance.status)  # Add 'status' field to the form for admins
        else:
            self.fields.pop('status', None)  # Remove 'status' field from the form for non-admins


class UsersPostAdminForm(forms.ModelForm):
    '''Define UsersPostAdmin form so i can see the form in my Admin Panel '''
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'featured_image', 'status']
        widgets ={
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write something here!'}),
        }

    def slug_unique(self,title):
        
        slug = slugify(title)
 
        if Post.objects.filter(slug=slug).exist():
            raise ValidationError('A post with this title already exist')

        return title


'''Class for Edit Profile  based on  model Profile'''
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
        }
