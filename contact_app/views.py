from django.shortcuts import render, redirect
from contact_app.forms import ContactForm
from contact_app.models import ContactInformation, SocialMediaLink
from django.contrib import messages


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



def contact(request):     
    social_media = SocialMediaLink.objects.all()  
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
            return redirect('contact')
        else:
            messages.error(request, "Invalid form")
            return redirect('contact')
    else:
        form = ContactForm()
          
    context = {
        "form": form, 
        'socials': social_media
    }
    return render(request, 'contact.html', context)
