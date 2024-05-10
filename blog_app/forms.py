from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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
            'password': forms.TextInput(attrs={'placeholder': 'Enter passeword', 'class': 'form-control', 'type': 'password'}),

        }
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password'].required = False
        
    def clean(self):
        clean_d = super().clean()
        
        username = clean_d.get('username')
        password = clean_d.get('password')
        
        if not username:
            self.add_error('username', 'Username should not be empty')
        if not password:
            self.add_error('username', 'Password should not be empty')
            
        return clean_d
        

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
    
    # Overridden    
    def clean(self):
        clean_d = super().clean()
        writer_name = clean_d.get('writer_name')
        blog_type = clean_d.get('blog_type')
        image = clean_d.get('image')
        title = clean_d.get('title')
        short_text = clean_d.get('short_text')
        description = clean_d.get('description')
        
        if not writer_name:
            self.add_error('writer_name', 'Writer name should not be empty')
        if not blog_type:
            self.add_error('blog_type', 'Blog type should not be empty')
        if not image:
            self.add_error('image', 'Image should not be empty')
        if not title:
            self.add_error('writer_name', 'Title should not be empty')
        if not short_text:
            self.add_error('writer_name', 'Short text should not be empty')
        if not description:
            self.add_error('writer_name', 'Description should not be empty')
            
        return clean_d

     
    # # Overridden    
    # def save(self, commit=True):  
    #     if not self.cleaned_data['writer_name']:
    #         raise ValidationError("Writer name are required.")
    #     if not self.cleaned_data['blog_type']:
    #         raise ValidationError("Blog type are required.")
    #     if not self.cleaned_data['title']:
    #         raise ValidationError("Title are required.")
    #     if not self.cleaned_data['short_text']:
    #         raise ValidationError("Short text are required.")
    #     if not self.cleaned_data['description']:
    #         raise ValidationError("Description are required.")

    #     return super().save(commit=commit)