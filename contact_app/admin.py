from django.contrib import admin
from contact_app.models import ContactInformation, SocialMediaLink

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    model = ContactInformation
    list_display = ['name', 'email', 'phone', 'subject']
    
admin.site.register(ContactInformation, ContactAdmin)
admin.site.register(SocialMediaLink)