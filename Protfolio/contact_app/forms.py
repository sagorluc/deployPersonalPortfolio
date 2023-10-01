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