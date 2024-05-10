from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog_app.models import Blog
from blog_app.forms import BlogForm, UserForm
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.

# =================================== Login superuser ==================================
def superuser_login(request):   
    user_obj = User.objects.all()
    user_id = 0
    db_username = None
    db_password = None
    
    for us in user_obj:
        user_id = us.id
        db_username = us.username
        db_password = us.password
        
    # print(user_id, 'line 20')  
    user_ins = User.objects.get(pk=user_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
                
        print(db_username, 'line 32')
        print(db_password, 'line 32')
        if not username and not password:
            messages.error(request, 'Username and password should not be empty')
            return redirect('login_form')
        
        if db_username != username:
            messages.error(request, 'Username not found in database')
            return redirect('login_form')
        
        if not user_ins.check_password(password):
            messages.error(request, 'Password not found in database')
            return redirect('login_form')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, 'Superuser login successfully')
            return redirect('blog')
        else:
            messages.error(request, 'User not founded')
            return redirect('login_form')

    form = UserForm(request.POST)
    if not form.is_valid():
        return render(request, 'login.html', {'form': form}) # will throw the form validation error
    
    context = {
        'form': form,
    }
    template = 'login.html'
    return render(request, template, context)

# =================================== Logout superuser ==================================
def log_out(request):
    user_obj = User.objects.all()
    user_id = 0  
    for us in user_obj:
        user_id = us.id

    user_ins = User.objects.get(pk=user_id)
    
    if request.user.is_superuser and request.user.is_authenticated and user_ins:
       logout(request)
       messages.success(request, 'User logout successfully')
       return redirect('blog') 
            
            
           
# =================================== Create Blog ======================================
def create_blog(request):  
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your blog is created successfully.')
            return redirect('blog')
        else:
            # messages.error(request, 'Invalid form')
            # return redirect('create_blog')
            return render(request, 'create_blog.html', {'form': form}) # will throw the form validation error
    else:
        form = BlogForm()
        
    context = {
        'form': form,
    }
    return render(request, 'create_blog.html', context)



# =================================== Update Blog ====================================
def update_blog(request, id):
    get_id = Blog.objects.get(pk= id)
    
    if request.user.is_superuser and request.user.is_authenticated:    
        if request.method == 'POST':            
            form = BlogForm(request.POST, request.FILES, instance= get_id)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your blog is updated successfully')
                return redirect('blog-post', id= get_id.id)
            else:
                # messages.error(request, 'Invalid form')
                # return redirect('update_blog', id=id)
                return render(request, 'update_blog.html', {'form': form}) # will throw the form validation error
        else:
            form = BlogForm(instance=get_id)
            
        context = {
            'form': form,
        }
        return render(request, 'update_blog.html', context)
    
    else:
        messages.error(request, 'Not allowed !!')
        return redirect('blog-post', id= get_id.id)




# ================================= Delete Blog ======================================
def delete_blog(request, id):
    if request.user.is_authenticated and request.user.is_superuser:
        get_id = Blog.objects.get(pk= id).delete()
        messages.success(request, 'Your blog is deleted successfully.')
        return redirect('blog')
    else:
        messages.error(request, 'Not Allowed !!')
        return redirect('blog-post', id=id)
        
        

# ================================== Blog ============================================
def blog(request):
    blogs = Blog.objects.all()
    
    paginator = Paginator(blogs, 3) # will show 2 content per page
    page = request.GET.get('page') # get the page
    page_obj = paginator.get_page(page)
    
    
    context = {
        # 'blogs' : blogs,
        'page_obj' : page_obj
    }
    return render(request, 'blog.html' , context)



# ===================================== Blog Post =====================================
def blog_post(request, id):
    get_obj = get_object_or_404(Blog, pk= id)
    is_superuser = request.user.is_authenticated
    
    context = {
        'obj' : get_obj,
        'is_authenticated': is_superuser,
    }
    
    return render(request, 'blog-post.html', context)


    