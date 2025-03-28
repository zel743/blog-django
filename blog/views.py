from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Post
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Profile
from django.core.exceptions import PermissionDenied

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

def profile(request):
    return render(request,'profile.html')

@login_required
def editprofile(request):
    # Obtener o crear el perfil
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'edit_profile.html', context)

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            # Obtener la URL de retorno de forma segura
            next_url = request.POST.get('next')  
            if not next_url:  
                next_url = 'index'  # Página por defecto si no hay 'next'

            return redirect(next_url) if next_url.startswith('/') else redirect('index')  # Seguridad

    else:
        form = PostForm()
        next_url = request.GET.get('next', 'index')  

    return render(request, 'posting.html', {'form': form, 'next': next_url})

def linux_posts(request):
    posts = Post.objects.filter(section='linux').order_by('-created_at')
    return render(request, 'linux.html', {'posts': posts})
def windows_posts(request):
    posts = Post.objects.filter(section='windows').order_by('-created_at')
    return render(request, 'windows.html', {'posts': posts})
def macos_posts(request):
    posts = Post.objects.filter(section='macos').order_by('-created_at')
    return render(request, 'macos.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Permite al autor O al admin editar
    if not (request.user == post.author or request.user.is_superuser):
        raise PermissionDenied("No tienes permiso para editar este post")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado correctamente")
            return redirect('linux')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'editpost.html', {
        'form': form,
        'post': post
    })


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Permite al autor O al admin eliminar
    if not (request.user == post.author or request.user.is_superuser):
        raise PermissionDenied("No tienes permiso para eliminar este post")
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'El post se ha eliminado correctamente.')
        return redirect('linux')
    # Si no es POST, muestra una página de confirmación    
    return render(request, 'confirm_delete.html', {'post': post})


#api 
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {
        'user': request.user,
        'profile': profile
    })