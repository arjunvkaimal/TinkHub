from django.shortcuts import render
from .models import Blog
from django.shortcuts import redirect
from .forms import BlogForm
from django.shortcuts import get_object_or_404
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})


@login_required
def index(request):
    blogs = Blog.objects.filter(author=request.user)  
    return render(request, 'home/index.html', {'blogs': blogs})


def new_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogForm()
    return render(request, "home/create.html", {'form': form})


def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "home/entry.html", {"blog": blog})
  
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view_blog', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, "home/edit.html", {'form': form, 'blog': blog})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect('index')
    return render(request, "home/delete.html", {"blog": blog})

