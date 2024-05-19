from django.shortcuts import render, get_object_or_404, redirect
from blog_main.forms import RegistrationForm
from blogs.models import Category, Blog, About
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    
    featured_post = Blog.objects.filter(is_featured=True, status='Published').order_by('-update_at')
    blog_post = Blog.objects.filter(is_featured=False, status='Published').order_by('-update_at')
    about = get_object_or_404(About)
    return render(request, 'home.html', {'featured_post':featured_post, 'blog_post':blog_post, 'about':about})

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
        
    else:

        form = RegistrationForm()

    return render (request, 'register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    else:

        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout(request):

    auth.logout(request)

    return redirect('home')