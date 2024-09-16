from django.shortcuts import render
from .models import Blog
from django.shortcuts import redirect
from .forms import BlogForm
from django.shortcuts import get_object_or_404
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
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
    return render(request, 'home/index.html', {'blogs':blogs})


@login_required
def new_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Associate the blog with the logged-in user
            blog.save()
            return redirect('index')
    else:
        form = BlogForm()
    return render(request, 'home/create.html', {'form': form})

@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, "home/entry.html", {"blog": blog})
    if not blog.is_public and request.user != blog.author:
        return redirect('index')
  
@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post")
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'home/edit.html', {'form': form})

    
@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post")
    
    if request.method == 'POST':
        blog.delete()
        return redirect('index')
    return render(request, 'home/delete.html', {'blog': blog})
