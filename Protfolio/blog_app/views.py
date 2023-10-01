from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog_app.models import Blog
from blog_app.forms import BlogForm
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.

# =================================== Create Blog ======================================
def create_blog(request):  
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})



# =================================== Update Blog ====================================
def update_blog(request, id):
    get_id = Blog.objects.get(pk= id)
    get_ins = BlogForm(instance= get_id)
     
    is_superuser = request.user.is_authenticated
      
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance= get_id)
        if form.is_valid():
            form.save()
            return redirect('blog-post', id= get_id.id)
    else:
        form = BlogForm(instance=get_id)
        
    context = {
        'form': form,
        'is_authenticated': is_superuser,
    }
    return render(request, 'update_blog.html', context)




# ================================= Delete Blog ======================================
def delete_blog(request, id):
    get_id = Blog.objects.get(pk= id).delete()
    return redirect('blog')
        
        

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


    