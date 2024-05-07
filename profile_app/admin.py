from django.contrib import admin
from profile_app.models import MyProfile, HomeProfile, Achivement, MyPortFolio, ResumeDownload

# Register your models here.
admin.site.register(MyProfile)
admin.site.register(HomeProfile)
admin.site.register(Achivement)
admin.site.register(MyPortFolio)
admin.site.register(ResumeDownload)
