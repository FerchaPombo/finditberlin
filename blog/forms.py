from .models import Comments, UsersPost
from django import forms
from crispy_forms.helper import FormHelper  
from crispy_forms.layout import Layout, Submit
from cloudinary.forms import CloudinaryJsFileField
from cloudinary.models import CloudinaryField as BaseCloudinaryField

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
# create a class for Users Post based on my model 

class CloudinaryField(BaseCloudinaryField):
    def formfield(self, **kwargs):
        return super().formfield(widget=CloudinaryJsFileInput(), **kwargs)

class UsersPostForm(forms.ModelForm):
    class Meta:
        model = UsersPost
        fields = ['title', 'author', 'body', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            #'featured_image': CloudinaryJsFileField(attrs={'placeholder': 'Upload an image here'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write something here!'}),
        }
        '''widget_attrs = {
            'featured_image': {'placeholder': 'Upload an image here'},
        }'''

    def __init__(self, *args, **kwargs):
        super(UsersPostForm, self).__init__(*args, **kwargs)
        self.initial['author'] = kwargs.get('initial', {}).get('author', None)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'title',
            'author',
            'featured_image',
            'body',
            Submit('submit', 'Submit', css_class='btn-primary btn-outline-dark btn-sm')
        )

    def save(self, commit=True):
        userspost = super(UsersPostForm, self).save(commit=False)
        userspost.author = self.initial.get('author', None)
        if commit:
            userspost.save()
        return {{ author.post }}



'''from .models import Comments
from django import forms


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)'''