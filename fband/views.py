from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Album

def homepage(request):
    # Render the homepage template
    return render(request, 'fband/homepage.html')

def register(request):
    # Render the registration template
    return render(request, 'fband/register.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the albums page if login is successful
                return redirect('album_list')
    else:
        form = AuthenticationForm()
    # Render the login template with the form
    return render(request, 'fband/login.html', {'form': form})

@login_required(login_url='login', redirect_field_name=None)
def user_logout(request):
    logout(request)
    # Redirect to the homepage after logout
    return redirect('homepage')

@login_required(login_url='login', redirect_field_name=None)
def album_list(request):
    albums = Album.objects.all()
    # Render the album list template with the albums
    return render(request, 'fband/album_list.html', {'albums': albums})

@login_required(login_url='login', redirect_field_name=None)
def about(request):
    # Render the about template
    return render(request, 'fband/about.html')

@login_required(login_url='login', redirect_field_name=None)
def contact(request):
    # Render the contact template
    return render(request, 'fband/contact.html')
