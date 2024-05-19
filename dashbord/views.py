from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

from dashbord.forms import Addcategory, AddblogForm
from django.template.defaultfilters import slugify


# Create your views here.

@login_required(login_url='login')
def dashbord(request):
    category_count = Category.objects.all().count()
    post_count = Blog.objects.all().count()
    return render(request, 'dashbord/dashbord.html',{'category_count':category_count, 'post_count':post_count})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'dashbord/categories.html', {'categories':categories})

def add_category(request):
    if request.method == 'POST':
        form = Addcategory(request.POST)
        if form.is_valid():
            form.save()
        return redirect('categories')
    form = Addcategory()
    return render(request, 'dashbord/add_category.html', {'form':form})

def edit_category(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = Addcategory(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return redirect('categories')
    form = Addcategory(instance=category)
    return render (request, 'dashbord/edit_category.html', {'form':form})

def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('categories')


#------------  posts-------------
def posts(request):
    posts  = Blog.objects.all()

    return render(request, 'dashbord/posts.html', {'posts':posts})

def add_post(request):
    if request.method == 'POST':
        form = AddblogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+ '-'+str(post.id)
            post.save()
        return redirect('posts')
    form = AddblogForm()
    return render(request, 'dashbord/add_post.html', {'form':form})

def edit_post(request, id):
    get_post = get_object_or_404(Blog, pk=id)
    if request.method == 'POST':
        form = AddblogForm(request.POST, request.FILES, instance=get_post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+ '-'+str(post.id)
            post.save()
        return redirect('posts')
    form = AddblogForm(instance=get_post)
    return render(request, 'dashbord/edit_post.html',{'get_post':get_post, 'form':form})

def delete_post(request, id):
    post = get_object_or_404(Blog, pk=id)
    post.delete()
    return redirect('posts')