from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages


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

def edit_post(request):
    return render(request,'editpost.html')

@login_required(login_url='login') # redirige si no eres usuario a pagina de login
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
def windows_posts(request):
    posts = Post.objects.filter(section='windows').order_by('-created_at')
    return render(request, 'windows.html', {'posts': posts})
def macos_posts(request):
    posts = Post.objects.filter(section='macos').order_by('-created_at')
    return render(request, 'macos.html', {'posts': posts})

@login_required  #funcion para editar post
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)  # Solo el autor puede editar
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('linux')  # Redirige a donde quieras después de editar
    else:
        form = PostForm(instance=post)
    
    return render(request, 'editpost.html', {
        'form': form,
        'post': post
    })

@login_required #funcion para eliminar post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'El post se ha eliminado correctamente.')
        return redirect('linux')
    
    # Si no es POST, muestra una página de confirmación
    return render(request, 'confirm_delete.html', {'post': post})