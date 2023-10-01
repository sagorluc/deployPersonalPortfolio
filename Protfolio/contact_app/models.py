from django.db import models
from profile_app.models import MyProfile

# Create your models here.
class ContactInformation(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(max_length= 50)
    phone = models.CharField(max_length= 15, null= True)
    subject = models.CharField(max_length= 100)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class SocialMediaLink(models.Model):
    social = models.ForeignKey(MyProfile, on_delete= models.CASCADE, related_name="social")
    facebook = models.URLField(blank= True)
    x = models.URLField(blank= True) # twitter
    instagram = models.URLField(blank= True, null= True)
    linkdin = models.URLField(blank= True)
    youtube = models.URLField(blank= True)
    github = models.URLField(blank= True)
    
    def __str__(self) -> str:
        return str(self.social)
    
