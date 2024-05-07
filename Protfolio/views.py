from django.shortcuts import render
from profile_app.models import HomeProfile


def home(request):
    all_obj = HomeProfile.objects.all()
    return render(request, 'index.html', {'homes': all_obj})