from django.urls import path
from blog_app.views import (
    blog, 
    blog_post, 
    create_blog, 
    update_blog, 
    delete_blog,
    superuser_login,
    log_out,
)

urlpatterns = [
    path('', blog, name="blog"),
    path('login/', superuser_login, name="login_form"),
    path('logout/', log_out, name="logout"),
    path('create_blog/', create_blog, name="create_blog"),
    path('update_blog/<int:id>', update_blog, name="update_blog"),
    path('delete/<int:id>', delete_blog, name="delete_blog"),
    path('blog-post/<int:id>', blog_post, name="blog-post"),
]
