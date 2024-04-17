from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('-update_at')
    blog_post = Blog.objects.filter(is_featured=False, status='Published')
    
    return render(request, 'home.html', {'featured_post':featured_post, 'blog_post':blog_post})