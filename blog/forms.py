from .models import Comments
from django import forms
from crispy_forms.helper import FormHelper  
from crispy_forms.layout import Layout, Submit

class CommentsForm(forms.ModelForm):  
    class Meta:
        model = Comments  
        fields = ['author', 'body']


    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'body',
            Submit('submit', 'Submit', css_class='btn-primary') 
        )
