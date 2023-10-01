from django.shortcuts import render
from profile_app.models import MyProfile, Achivement, MyPortFolio

# Create your views here.
def about_me(request):
    all_obj = MyProfile.objects.all()
    achive = Achivement.objects.all() 
    return render(request, 'about.html', {'profiles': all_obj, 'achives': achive})



def my_protfolio(request):
    portfolio = MyPortFolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolio})