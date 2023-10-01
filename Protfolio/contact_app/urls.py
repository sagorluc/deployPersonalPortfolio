from django.urls import path
from contact_app.views import contact

urlpatterns = [
    path('', contact, name="contact"), 
]


