from typing import Any
from contact_app.models import ContactInformation
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'YOUR NAME'}),
            'email': forms.EmailInput(attrs={'placeholder': 'YOUR EMAIL'}),
            'phone': forms.TextInput(attrs={'placeholder': 'YOUR PHONE'}),
            'subject': forms.TextInput(attrs={'placeholder': 'YOUR SUBJECT'}),
            'message': forms.Textarea(attrs={'placeholder': 'YOUR MESSAGE...'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['email'].required = False
        self.fields['phone'].required = False
        self.fields['subject'].required = False
        self.fields['message'].required = False
        
    def clean(self):
        clean_d = super().clean()
        name = clean_d.get('name')
        email = clean_d.get('email')
        phone = clean_d.get('phone')
        subject = clean_d.get('subject')
        message = clean_d.get('message')
        
        if not name:
            self.add_error('name', 'Name is required')
        if not email:
            self.add_error('email', 'Email is required')
        if not phone:
            self.add_error('phone', 'Phone is required')
        if not subject:
            self.add_error('subject', 'Subject is required')
        if not message:
            self.add_error('message', 'Message is required')
            
        return clean_d