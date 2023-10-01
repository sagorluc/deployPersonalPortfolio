from django.urls import path
from profile_app.views import about_me, my_protfolio

urlpatterns = [
    path('', about_me, name="about"),
    path('portfolio/', my_protfolio, name="portfolio"),
]
