from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


def index(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'register.html', context)

def windows(request):
    return render(request, 'windows.html' )

def macos(request):
    return render(request, 'macos.html' )

def posting(request):
    form = PostForm()  # 
    return render(request, 'posting.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('linux')  # Redirige a la lista de posts
    else:
        form = PostForm()
    return render(request, 'posting.html', {'form': form})

def linux_posts(request):
    posts = Post.objects.filter(section='linux').order_by('-created_at')
    return render(request, 'linux.html', {'posts': posts})