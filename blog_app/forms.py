from django import forms
from django.contrib.auth.models import User
from blog_app.models import Blog

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username name', 'class': 'form-control'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter passeword', 'class': 'form-control'}),

        }
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.render_value = True
        

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [ 
                  'writer_name', 'blog_type', 
                  'image', 'title', 
                  'short_text', 'description'
                ]
        
        labels = {
            'writer_name': 'Writer name'
        }
        
        widgets = {
            'writer_name': forms.TextInput(attrs={'placeholder': 'Enter writer name..'}),
            'blog_type': forms.TextInput(attrs={'placeholder': 'Enter blog type'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title'}),
            'short_text': forms.TextInput(attrs={'placeholder': 'Enter short text'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your description here...'}),
        }