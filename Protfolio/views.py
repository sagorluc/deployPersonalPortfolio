from django.shortcuts import render
from profile_app.models import HomeProfile, MyProfile



def home(request):
    all_obj = HomeProfile.objects.all()
    profile_obj = MyProfile.objects.all()
    
    context = {
        # 'home_profiles' : zip(all_obj, profile_obj)
        'homes': all_obj,
        'profiles': profile_obj,
    }
    return render(request, 'index.html', context)