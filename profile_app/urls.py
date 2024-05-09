from django.urls import path
from profile_app.views import about_me, my_protfolio # resume

urlpatterns = [
    path('about_me/', about_me, name="about"),
    path('portfolio/', my_protfolio, name="portfolio"),
    
]  # path('resume/', resume, name="resume"),
