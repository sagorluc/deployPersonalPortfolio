from django.shortcuts import render
from profile_app.models import MyProfile, Achivement, MyPortFolio, ResumeDownload

# Create your views here.
def about_me(request):
    resume_obj = ResumeDownload.objects.all()
    all_obj = MyProfile.objects.all()
    achive = Achivement.objects.all() 
    
    context = {
        'resume_profile': zip(resume_obj, all_obj),
        # 'resume_profile': all_obj,
        'achive_obj': achive
    }
    
    return render(request, 'about.html', context)



def my_protfolio(request):
    portfolio = MyPortFolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolio})



# def resume(request):
#     resume_download = ResumeDownload.objects.all()
    
#     context = {
#         'resume' : resume_download,
#     }
    
#     return render(request, 'about.html', context)