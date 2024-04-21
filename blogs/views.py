from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.db.models import Q
# Create your views here.

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)

    category = get_object_or_404(Category, pk = category_id)
   
    return render(request, 'post_by_category.html',{'posts':posts, 'category':category})

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    return render(request, 'single_blog.html',{'single_blog':single_blog})

def search(request):
    keyword = request.GET.get('keyword')
    posts = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    print(posts)

    return render(request, 'search.html',{'posts':posts, 'keyword':keyword})