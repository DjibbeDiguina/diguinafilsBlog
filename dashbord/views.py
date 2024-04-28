from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

from dashbord.forms import Addcategory

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