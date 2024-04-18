from django.shortcuts import render, get_object_or_404
from blogs.models import Category, Blog, About

def home(request):
    
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('-update_at')
    blog_post = Blog.objects.filter(is_featured=False, status='Published')
    about = get_object_or_404(About)
    return render(request, 'home.html', {'featured_post':featured_post, 'blog_post':blog_post, 'about':about})