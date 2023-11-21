from .models import Comments, Place
from django import forms

class CommentsForm(forms.ModelForm):
    class Meta :
        model = Comments
        fields = ('body',)

