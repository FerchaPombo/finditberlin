from .models import Comments, Post #UsersPost
from django import forms
from crispy_forms.helper import FormHelper  
from crispy_forms.layout import Layout, Submit
from cloudinary.forms import CloudinaryJsFileField
from cloudinary.models import CloudinaryField as BaseCloudinaryField
from django.utils.text import slugify
from django.core.exceptions import ValidationError


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
    '''Class for Users Post based on my model'''
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'featured_image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write something here!'}),
        }

    def slug_unique(self,title):
        
        slug = slugify(title)
 
        if Post.objects.filter(slug=slug).exist():
            raise ValidationError('A post with this title already exist')

        return title

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

    def save(self, commit=True, author=None):
        userspost = super(UsersPostForm, self).save(commit=False)
        userspost.author = author
        #if commit:
            #userspost.save()
        return userspost


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'status', 'excerpt']

    def __init__(self, *args, author=None, **kwargs):
        super().__init__(*args, **kwargs)

        if author:
            self.fields['author'].queryset = author.blog_posts.all()


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
