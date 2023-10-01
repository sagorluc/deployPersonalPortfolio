from django.shortcuts import render
from profile_app.models import MyProfile, Achivement, MyPortFolio, ResumeDownload

# Create your views here.
def about_me(request):
    all_obj = MyProfile.objects.all()
    achive = Achivement.objects.all() 
    
    context = {
        'profiles': all_obj,
         'achives': achive
    }
    
    return render(request, 'about.html')



def my_protfolio(request):
    portfolio = MyPortFolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolio})



# def resume(request):
#     resume_download = ResumeDownload.objects.all()
    
#     context = {
#         'resume' : resume_download,
#     }
    
#     return render(request, 'about.html', context)