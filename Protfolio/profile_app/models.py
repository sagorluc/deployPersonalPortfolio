from django.db import models

# Create your models here.

class MyProfile(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField(max_length= 50)
    age = models.IntegerField()
    nationality = models.CharField(max_length= 50)
    freelance = models.CharField(max_length= 50, null= True, default= 'NOT')
    address = models.TextField(max_length= 200)
    phone = models.CharField(max_length= 14)
    languages = models.CharField(max_length= 100, default='Bangla, English')
    skype = models.CharField(max_length= 50, null= True)
    instagrame = models.CharField(max_length= 50, null= True, default= 'sagor_luc')
    image = models.ImageField(upload_to='photos/myPhotos', blank= True)
    created_date = models.DateTimeField(auto_now_add= True)
    modify_date = models.DateTimeField(auto_now= True)
    
    
    def __str__(self) -> str:
        return self.first_name
    
class ResumeDownload(models.Model):
    user = models.ForeignKey(MyProfile, on_delete= models.CASCADE, related_name="user_resume")
    download_resume = models.URLField(blank= True)
    
    
    
class HomeProfile(models.Model):
    home_obj = models.ForeignKey(MyProfile, on_delete=models.CASCADE, related_name="home_obj")
    work_as = models.CharField(max_length= 100, default='Software Engineer')
    description = models.TextField(max_length= 250,  null= True)
    
    def __str__(self) -> str:
        return str(self.home_obj)
    
    
class Achivement(models.Model):
    profile = models.ForeignKey(MyProfile, on_delete=models.CASCADE, related_name='profile')
    experience = models.CharField(max_length= 50)
    complate_project = models.CharField(max_length= 50)
    happy_customer = models.CharField(max_length= 50)
    award_won = models.CharField(max_length= 50)
    
    def __str__(self) -> str:
        return str(self.profile)
    

class MyPortFolio(models.Model):
    portfolio = models.ForeignKey(MyProfile, on_delete=models.CASCADE, related_name="my_portfolio")
    title = models.CharField(max_length=100, null= True)
    project = models.CharField(max_length= 100, null= True)
    client = models.CharField(max_length= 100)
    languages = models.CharField(max_length= 100)
    preview = models.URLField()
    image1 = models.ImageField(upload_to="photos/portfolio1")
    image2 = models.ImageField(upload_to= "photos/portfolio2")
    created_date = models.DateTimeField(auto_now_add= True)
    modify_date = models.DateTimeField(auto_now= True)
    
    def __str__(self) -> str:
        return self.title
    