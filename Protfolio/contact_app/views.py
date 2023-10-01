# from django.shortcuts import render
# from contact_app.forms import ContactForm
# from contact_app.models import ContactInformation
# from django.contrib import messages

# # Create your views here.
# def contact(request):   
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
        
#         if name and email and phone and subject and message:
#             new_entry = ContactInformation(name= name, email= email, phone= phone, subject= subject, message= message)
#             print("line 17",new_entry)
#             new_entry.save()
#             print("line 19",new_entry)
#             messages.success(request, "send successfully")
#         else:
#             messages.error(request, "plase fill out all the fields")
#     return render(request, 'contact.html')


from django.shortcuts import render
from contact_app.forms import ContactForm
from contact_app.models import ContactInformation, SocialMediaLink
from django.contrib import messages

def contact(request):   
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
        else:
            messages.error(request, "Please fill out all the fields")
    else:
        form = ContactForm()
    
    social_media = SocialMediaLink.objects.all()  
    return render(request, 'contact.html', {"form": form, 'socials': social_media})
