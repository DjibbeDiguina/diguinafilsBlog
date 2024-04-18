from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
# Create your views here.

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)

    category = get_object_or_404(Category, pk = category_id)
   
    return render(request, 'post_by_category.html',{'posts':posts, 'category':category})

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    return render(request, 'single_blog.html',{'single_blog':single_blog})