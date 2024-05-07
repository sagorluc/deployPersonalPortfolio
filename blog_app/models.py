from django.db import models
from profile_app.models import MyProfile

# Create your models here.
class Blog(models.Model):
      user        = models.ForeignKey(MyProfile, on_delete=models.CASCADE, related_name="user")
      id          = models.AutoField(unique=True, primary_key= True)
      blog_type   = models.CharField(max_length= 50)
      image       = models.ImageField(upload_to='photos/blog_image', blank=True)
      title       = models.CharField(max_length= 50)
      short_text  = models.CharField(max_length= 150, null= True)
      description = models.TextField()
      create_date = models.DateTimeField(auto_now_add= True)
      modify_date = models.DateTimeField(auto_now= True)
      
      def __str__(self) -> str:
            return self.title
      
